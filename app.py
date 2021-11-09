from logging import debug
from flask import Flask;
from flask import jsonify;
from flask import request;
from flask_cors import CORS, cross_origin;
import runge_kutta as rungK
import numpy as np

import json;
import interpolacion as lang;


app = Flask(__name__)
CORS(app)

@app.route('/')
@cross_origin()
def index():
    return 'hola'

@app.route('/lagrangreParams', methods=['POST'])
@cross_origin()
def resultado_lagrange():

    #Recibimos el request por el body y lo volvemos un json
    datos = json.loads(request.data)
    #Llamamos el metodos de lagrange
    resultado = lang.lagrange_general(datos['x'], datos['y'],datos['busq'])
    return str(resultado)


@app.route('/newton', methods=['POST'])
@cross_origin()
def resultado_newton():

    #Recibimos el request por el body y lo volvemos un json
    datos = json.loads(request.data)
    #Llamamos el metodos de lagrange
    resultado = lang.polinomio_newton(datos['grado'], datos['x'],datos['y'],datos['X'])
    return str(resultado)

@app.route('/runge', methods=['POST'])
@cross_origin()
def resultado_runge_kutta():

    #Recibimos el request por el body y lo volvemos un json
    datos = json.loads(request.data)
    funcion = lambda x, y: eval(datos['funcion']) 
    #Llamamos el metodos de runge kutta 
    x, y, err = rungK.runge_kutta_4(funcion, datos['x'], datos['y'], datos['xf'], datos['h'])
    return jsonify({"x":x,"y":y,"error":err})

@app.route('/runge_orderS', methods=['POST'])
@cross_origin()
def resultado_runge_kutta_ordenS():

    #Recibimos el request por el body y lo volvemos un json
    datos = json.loads(request.data)
    funcion = lambda x, y: eval(datos['funcion']) 
    #Llamamos el metodos de runge kutta 
    x, y, err = rungK.runge_kutta_ordenS(funcion, datos['x'], datos['y'], datos['xf'], datos['h'])
    return jsonify({"x":x,"y":y,"error":err})