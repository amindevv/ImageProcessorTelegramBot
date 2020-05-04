
import urllib.request
import requests

from image_processor import ImageProcessor

from config import TELEGRAM_GET_FILE_PATH_URL as url_file_path
from config import TELEGRAM_GET_FILE_URL as url_file
from config import FILE_SAVE_PATH as url_file_output

class FileDownloader:

  def __init__(self, message, processor):

    self.chat_id = message['chat']['id']
    self.message_id = message['message_id']
    self.file_id = message['photo'][1]['file_id'] if len(message['photo']) > 1 else message['photo'][0]['file_id']
    self.username = message['from']['username'] if "username" in message['from'] else "NoUserName"
    self.processor = processor

  # This guy send's a request to telegram to fetch the file path
  def get_file_path(self):

    url = url_file_path.format(self.file_id)

    response = requests.get(url)

    response_json = response.json()

    file_path = response_json['result']['file_path']

    self.download_file(file_path)      

  # Download's the file using the file_path
  def download_file(self, file_path):

    file_name = self.get_file_name() + ".jpg"
 
    file_path_url = url_file.format(file_path)

    file_save_path = url_file_output + file_name

    urllib.request.urlretrieve(file_path_url, file_save_path)

    self.send_to_file_processor(file_name)

  # Send the file using local file path to apply the frame
  def send_to_file_processor(self, downloaded_path):

    # Image processor automatically starts the process
    ImageProcessor(downloaded_path, self.chat_id, self.message_id, self.processor)

  # Saves the file to a JPEG 
  def get_file_name(self):

    # user_name + _ + message_id + _ + chat_id
    return f"{self.username}_{self.message_id}_{self.chat_id}"
      