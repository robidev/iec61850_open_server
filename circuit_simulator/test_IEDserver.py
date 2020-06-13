#!/usr/bin/env python3
import socketserver
from threading import Thread
import numpy
import matplotlib.pyplot as plt

arrA = {}

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        while 1:
          # self.request is the TCP socket connected to the client
          self.data = self.request.recv(1024).strip()
          if not self.data:
              break
          #print("{} wrote:".format(self.client_address[0]))
          #print(self.data[0:4])
          if self.data[0:2] == b'i ':
              print("init command")
              self.request.sendall(b"OK\n")
          elif self.data[0:2] == b's ':
              #print("set command:" + str(self.data[4:]))
              cmd = self.data[2:].decode("utf-8")
              key,val = cmd.split(' ', 1)
              if not key in arrA:
                  arrA[key] = numpy.array([])
              arrA[key] = numpy.append(arrA[key], float(val))
              self.request.sendall(b"OK\n")
              #if arrA[key].size > 199:
              #    print("done")
              #    figure = plt.figure(1, (20, 10))
              #    axe = plt.subplot(111)
              #    plt.title('')
              #    plt.xlabel('Time [s]')
              #    plt.ylabel('Voltage [V]')
              #    plt.grid()

              #    for key in arrA:
              #    plt.plot(arrA[key])

              #    plt.legend(('v1','v2','v3','a1','a2','a3'), loc=(.05,.1))

              #    plt.tight_layout()
              #    plt.show()
              #    exit(0)
          elif self.data[0:2] == b'g ':
              #print("get command:" + str(self.data[4:]))
              self.request.sendall(b"10.0\n")
          else:
              print("cannot decode command:" + str(self.data))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 65000
    # Create the server, binding to localhost on port 9999
    with ThreadedTCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()