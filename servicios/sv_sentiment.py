# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: sv_sentiment.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): David Reyes, Sandy de la Rosa, Jose Rodriguez, Manuel Peralta
# Version: 1 Octubre 2018
# Descripción:
#
#   Este archivo define el rol de un servicio. Su función general es porporcionar en un objeto JSON
#   información estadistica acerca de los comentarios sobre una pelicula o serie en la red social twitter
#   mediante el uso de un API para el analisis de sentimientos.
#   ('https://twitter.com/').
#   ('https://www.paralleldots.com/').
#
#
#
#                                        sv_sentimiento.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Ofrecer un JSON con  |- Utiliza el API de     |
#           |    Procesador de      |    en analisis estadis- |  paralleldots y Twitter|
#           |comentarios de Twitter |    tico de sentimientos | - Devuelve un JSON con |
#           |para analisis de senti-|    en comentarios.      |   datos estadisticos   |
#           |mientos usando el API  |                         |   Pisitivo, negativo y |
#           |paralleldots.          |                         |   neutral.             |
#           +-----------------------+-------------------------+------------------------+
#
#	Ejemplo de uso: Abrir navegador e ingresar a http://localhost:8083/api/v1/information?t=matrix
#

import os
from flask import Flask, abort, render_template, request
import twitter
import time
from DataBaseSentiments import DataBaseSentiments
import paralleldots
import urllib, json

app = Flask(__name__)

@app.route("/api/v1/information")
def get_information():
  title = request.args.get("t")

  paralleldots.set_api_key('OzYex2DYIcftU7fsLB88ED59l1GkY5YPV4cEVVENs3o')

  consumer_key = 'xyVgIeD2xGGyCdp4zO76I9KoU'
  consumer_secret = 'z0NiiFmBkgvclvZqgdEPvtbF0sJLy9KbyGzRFO20Lw3JROLkwK'
  access_token = '3949707372-bZ5BGtQU6mpoj7nwqfQivVsyhjUkhyWRi0dM2Tq'
  access_token_secret = 'hLl6qzUILerHgEjTZtHpEfbQF7blHdB89IuJGtOSuRBEw'

  apiTweeter = twitter.Api(consumer_key,consumer_secret,access_token,access_token_secret)
  tweets = apiTweeter.GetSearch(title, count=50)

  date = time.strftime("%c")
  positiveTweets = 0
  negativeTweets = 0
  neutralTweets = 0

  for tweet in tweets:
    
    probabilities =  paralleldots.sentiment( tweet.text )
    response = json.loads(json.dumps(probabilities))

    if response['sentiment'] == 'positive':
      positiveTweets += 1
    elif response['sentiment'] == 'negative':
      negativeTweets += 1
    else:
      neutralTweets += 1
  
  dbs = DataBaseSentiments()

  idrow = dbs.create_request(
    dbs.create_connection(), 
    (
      title,
      date, 
      format(100*positiveTweets/len(tweets)), 
      format(100*negativeTweets/len(tweets)), 
      format(100*neutralTweets/len(tweets))
    )
  )

  data = {}
  data["id"] = idrow
  data["title"] = title
  data["date"] = date
  data['positive'] = format(100*positiveTweets/len(tweets))
  data['negative'] = format(100*negativeTweets/len(tweets))
  data['neutral'] = format(100*neutralTweets/len(tweets))

  json_data = json.dumps(data)
  print(data)
  return json_data

if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8083))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)