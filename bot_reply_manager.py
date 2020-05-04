import requests

from config import TELEGRAM_ADMIN_CHAT_ID as id_admin
from config import BASE_TELEGRAM_URL as url_base
from config import TELEGRAM_SEND_MESSAGE_URL as url_send_message
from config import MESSAGE_PHOTO_EDITED as message_photo_edited

class BotReplyManager:

  def __init__(self, chat_id):
    self.chat_id = chat_id

  """ This method is used to send the processed image,
   back to the user"""
  def sendImageWithCaption(self, file_path):

    url = url_base + "/" + "sendPhoto"
    files = {'photo': open(file_path, 'rb')}
    data = {'chat_id': self.chat_id, 'caption': message_photo_edited}
      
    res = requests.post(url, files=files, data=data)

    return res.status_code == 200 

  """ Just simply sends a message to the user """
  def sendTextMessage(self, message):

    res = requests.get(url_send_message.format(self.chat_id, message))

    return res.status_code == 200

