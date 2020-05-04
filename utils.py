import json
import requests

from config import TELEGRAM_ADMIN_CHAT_ID as id_admin
from config import TELEGRAM_SEND_MESSAGE_URL as url_send_message

class Utils:

  @staticmethod
  def messageAdmin(message):

    res = requests.get(url_send_message.format(id_admin, f"New photo from {message}"))

    return res.status_code == 200

  @staticmethod
  def print_json(message):

    print("*****************************")
    print(json.dumps(message, sort_keys= True, indent= 4))
    print("*****************************")

