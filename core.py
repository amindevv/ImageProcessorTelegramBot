import requests

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def index():

  req = request.get_json()

  # Temp
  success = True

  return jsonify(success = success)

""" Initializes the webhook
Args:
  url:str -> Provides the telegram server with a endpoint for webhook data """
def init_webhook(url):    

  requests.get(url)