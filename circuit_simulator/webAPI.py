#!/usr/bin/env python3
from flask import Flask, render_template, session, request, redirect, url_for, jsonify, send_file
from flask_cors import CORS
from urllib.parse import unquote

import json
import subprocess
import time
import os
import logging
import threading
import pprint

import circuit_simulator

sim = None
thread = None
stop_threads = False
steps_counter = 0

#webserver
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
CORS(app)

#http calls
@app.route('/', methods = ['GET'])
def index():
  return render_template('index.html')


@app.route('/init', methods = ['GET'])
def init():
  global sim

  scd = request.args.get("scd")
  if not scd is str:
    scd = "../scd/open_substation.scd"

  if sim == None:
    sim = circuit_simulator.circuit_simulator(scd,"../schema/SCL.xsd")
  return { 'init' : 'ok' }


@app.route('/reinit', methods = ['GET'])
def reinit():
  global sim

  scd = request.args.get("scd")
  if not scd is str:
    scd = "../scd/open_substation.scd"

  if sim == None:
    sim = circuit_simulator.circuit_simulator(scd,"../schema/SCL.xsd")
  else:
    sim.init_simulator()
  return { 'reinit' : 'ok' }


@app.route('/circuit', methods = ['GET'])
def circuit():
  global sim
  if sim == None:
    return { 'circuit' : 'none' }
  return sim.circuit


@app.route('/simulation_nodes', methods = ['GET'])
def simulation_nodes():
  global sim
  if sim == None:
    return { 'nodes' : 'none' }
  return sim.simulation_nodes 


@app.route('/simulation_node', methods = ['GET','POST'])
def simulation_node():
  global sim
  global thread
  if sim == None:
    return { 'node' : 'none' }

  if request.method == 'POST':  #this block is only entered when the form is submitted
    node = request.form.get('node')
    value = request.form.get('value')
    #set node value
    command = "alter " + node + "=" + value
    #sim.que_commands("alter @r.xs12_e1_w1_bb1_load.r1[r]=0")
    if thread is None:
      result = sim.ngspice_shared.exec_command(command)
      logger.debug(result)
    else:
      sim.que_commands(command)
    return {"node" : "post ok"}
  else:
    #sim.que_commands("print @r.xs12_e1_w1_bb1_load.r1[r]")
    url_encoded = request.args.get("node")
    node = unquote(url_encoded)
    val = sim.simulation_node(node)
    val = val.replace(node + " = ","")
    return { node : val }


@app.route('/simulation_settings', methods = ['GET','POST'])
def simulation_settings():
  global sim
  if sim == None:
    return { 'settings' : 'none' }

  if request.method == 'POST':  #this block is only entered when the form is submitted
    sim.title = request.form.get('title')
    sim.options = request.form.get('options')
    sim.tran = request.form.get('tran')

  return { 'title' : sim.title, 'options' : sim.options, 'tran' : sim.tran }


@app.route('/run_simulation', methods = ['GET'])
def run_simulation():
  global sim
  if sim == None:
    return { 'run' : 'none' }
  try:
    steps = int(request.args.get("steps"))
  except:
    return { 'run' : 'error' }
  try:
    step = int(request.args.get("step"))
  except:
    step = 10

  for _ in range(steps):
    sim.simulation_step(step)
  return { 'run' : 'ok' }


@app.route('/play_simulation', methods = ['GET'])
def play_simulation():
  global sim
  global thread
  global stop_threads 
  if sim == None:
    return { 'run' : 'none' }

  if thread is None:
    try:
      step = int(request.args.get("step"))
    except:
      step = 10

    try:
      delay = int(request.args.get("delay"))
    except:
      delay = 0.001

    stop_threads = False
    thread = threading.Thread(target=worker,args=(step,delay))
    thread.start()
    return { 'run' : 'started' }
  else:
    stop_threads = True
    thread.join()
    thread = None
    return { 'run' : 'stop', 'steps' : steps_counter }


#background simulation thread
def worker(step, delay):
  global stop_threads 
  global steps_counter
  steps_counter = 0
  while True:   
    sim.simulation_step(step)
    steps_counter += 1
    if stop_threads: 
      break
    time.sleep(delay)


@app.route('/plot_simulation', methods = ['GET'])
def plot_simulation():
  global sim
  if sim == None:
    return { 'plot' : 'none' }
  try:
    plot = int(request.args.get("plot"))
  except:
    return { 'plot' : 'error' }

  sim.plot_simulation(plot)
  #send_file("plot.png", mimetype='image/png')
  return  { 'plot' : 'ok' }


@app.route('/clear_plot', methods = ['GET'])
def clear_plot():
  global sim
  if sim == None:
    return { 'plot' : 'none' }
  sim.clear_plot()
  return { 'plot' : 'clear' }


@app.route('/quit', methods = ['GET'])
def quit():
  func = request.environ.get('werkzeug.server.shutdown')
  if func is None:
    raise RuntimeError('Not running with the Werkzeug Server')
  func()
  return { 'quit' : 'ok' }


if __name__ == '__main__':
  logger = logging.getLogger('webserver')
  logging.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    level=logging.INFO)
	# note the `logger` from above is now properly configured
  logger.debug("started")
  app.run(host="0.0.0.0",port=5010)
