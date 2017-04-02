# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------------------
# Archivo: gui.py
# Capitulo: 5 Patrón Micro Servicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.1 Marzo 2017
# Descripción:
#
#   Este archivo define la interfaz gráfica del usuario. Recibe dos parámetros que posteriormente son enviados
#   a micro servicios que la interfaz consume.
#   
#   
#
#                                             gui.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Porporcionar la in-  | - Consume micro servi- |
#           |          GUI          |    terfaz gráfica con la|   cios para proporcio- |        |
#           |                       |    que el usuario hará  |   nar información al u-|
#           |                       |    uso del sistema.     |   suario.              |
#           +-----------------------+-------------------------+------------------------+
#
import os
from flask import Flask, render_template, request
import urllib, json
import requests
app = Flask (__name__)

@app.route("/")
def index():
	# Método que muestra el index del sistema
	return render_template("index.html")

@app.route("/analysis/sentiment", methods=['GET'])
def sentiment_analysis():
	# Método que realiza el análisis de sentimientos
	# Se obtienen los parámetros que nos permitirán realizar la consulta y el análisis de sentimientos
	title = request.args.get("t")
	twitter_user = request.args.get("u")
	# Se definen e inicializan las variables que contabilizarán los reviews tuiteados
	total_reviews = 0
	positive_reviews = 0
	negative_reviews = 0
	neutral_reviews = 0
	url_omdb = urllib.urlopen("https://uaz.cloud.tyk.io/content/api/v1/information?t=" + title)
	# Se lee la respuesta de OMDB
	json_omdb = url_omdb.read()
	# Se convierte en un JSON la respuesta leída
	omdb = json.loads(json_omdb)
	# Se llena el JSON que se enviará a la interfaz gráfica para mostrársela al usuario
	json_result['positive'] = positive_reviews
	json_result['negative'] = negative_reviews
	json_result['total'] = total_reviews
	json_result['neutral'] = neutral_reviews
	json_result['omdb'] = omdb
	# Se regresa el template de la interfaz gráfica predefinido así como los datos que deberá cargar
	return render_template("status.html", result=json_result)
	

if __name__ == '__main__':
	# Se define el puerto del sistema operativo que utiliza el sistema de análisis de sentimientos de Netflix
	port = int(os.environ.get('PORT', 8000))
	# Se habilita el modo debug para visualizar errores
	app.debug = True
	# Se ejecuta el sistema con un host definido cómo '0.0.0.0' para que pueda ser accedido desde cualquier IP
	app.run(host='0.0.0.0', port=port)
