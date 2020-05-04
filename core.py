import requests

from flask import Flask, request, jsonify
from bot_request_manager import BotRequestManager

from process_manager import ProcessManager

app = Flask(__name__)

process_manager = ProcessManager()

@app.route('/webhook', methods=['POST'])
def index():

  req = request.get_json()

  request_manager = BotRequestManager(req)

  success = request_manager.get_result(process_manager)

  return jsonify(success = success)

""" Initializes the webhook
Args:
  url:str -> Provides the telegram server with a endpoint for webhook data """
def init_webhook(url):    

  requests.get(url)