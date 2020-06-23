#!/usr/bin/env python3
from flask import Flask, render_template, session, request, redirect, url_for, jsonify
from urllib.parse import unquote

import json
import subprocess
import time
import os
import logging
import pprint

import circuit_simulator

sim = None

#webserver
app = Flask(__name__, template_folder='templates', static_folder='static')

#http calls
@app.route('/', methods = ['GET'])
def index():
  return render_template('index.html')


@app.route('/init', methods = ['GET'])
def init():
  global sim
  if sim != None:
    return { 'init' : 'done' }

  scd = request.args.get("scd")
  if not scd is str:
    scd = "../open_substation.scd"

  sim = circuit_simulator.circuit_simulator(scd,"../schema/SCL.xsd")
  return { 'init' : 'ok' }

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
  return json.dumps(sim.simulation_nodes)


@app.route('/simulation_node', methods = ['GET','POST'])
def simulation_node():
  global sim
  if sim == None:
    return { 'node' : 'none' }

  if request.method == 'POST':  #this block is only entered when the form is submitted
    node = request.form.get('node')
    value = request.form.get('value')
    #set node value
    command = "alter " + node + "=" + value
    #sim.que_commands("alter @r.xs12_e1_w1_bb1_load.r1[r]=0")
    sim.que_commands(command)
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
    sim.title = request.form.get('language')
    sim.options = request.form.get('framework')
    sim.tran = request.form.get('framework')

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
  return { 'plot' : 'ok' }


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
  app.run()
