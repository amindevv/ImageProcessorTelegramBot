
import urllib.request
import requests

from config import TELEGRAM_GET_FILE_PATH_URL
from config import TELEGRAM_GET_FILE_URL
from config import FILE_SAVE_PATH

class FileDownloader:

  def __init__(self, message, processor):

    self.chat_id = message['chat']['id']
    self.message_id = message['message_id']
    self.file_id = message['photo'][1]['file_id'] if len(message['photo']) > 1 else message['photo'][0]['file_id']
    self.username = message['from']['username'] if "username" in message['from'] else "NoUserName"
    self.processor = processor

  # This guy send's a request to telegram to fetch the file path
  def getFilePath(self):

    url = TELEGRAM_GET_FILE_PATH_URL.format(self.file_id)

    response = requests.get(url)

    response_json = response.json()

    file_path = response_json['result']['file_path']

    self.downloadFile(file_path)      

  # Download's the file using the file_path
  def downloadFile(self, file_path):

    file_name = self.getFileName() + ".jpg"
 
    file_path_url = TELEGRAM_GET_FILE_URL.format(file_path)

    file_save_path = FILE_SAVE_PATH + file_name

    urllib.request.urlretrieve(file_path_url, file_save_path)

    self.sendToFileProcessor(file_name)

  # Send the file using local file path to apply the frame
  def sendToFileProcessor(self, downloaded_path):

    # Image processor automatically starts the process
    pass

  # Saves the file to a JPEG 
  def getFileName(self):

    # user_name + _ + message_id + _ + chat_id
    return f"{self.username}_{self.message_id}_{self.chat_id}"
      