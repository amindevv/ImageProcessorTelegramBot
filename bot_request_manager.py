from utils import Utils

from bot_reply_manager import BotReplyManager

TYPE_PHOTO = 0
TYPE_TEXT = 1
TYPE_WELCOME = 2

class BotRequestManager:

  def __init__(self, request):

    # This guy defines the type of reply bot should send
    self.type = None
    self.request = request

    # Parse the request from Telegram
    self.__parse_request_data()

  """ Parses Telegram JSON request from webhook 
  and sets fields for conditional actions. Most importantly,
  it defines the Type of the message which is later used for
  specific actions based on the Type """
  def __parse_request_data(self):

    Utils.print_json(self.request)

    request = self.request

    keys = request["message"].keys()

    message = request['message']
    
    if ("caption" in keys or "photo" in keys):
      
      self.type = TYPE_PHOTO
      
    elif ("text" in keys):          
      self.type = TYPE_TEXT

      # If it was the user's first message
      if message['text'] == "/start":
        self.type = TYPE_WELCOME              

    self.chat_id = message['chat']['id']
    self.first_name = message['from']['first_name']    

  """ Does different task based on Type returns success
  which will tell telegram that the message is received """
  def get_result(self, processor):

    reply_manager = BotReplyManager(self.chat_id)

    success = None 

    if self.type == TYPE_PHOTO:

      message = self.request

      # Start Photo processing
      processor.addJob({
        "messageId": message['message_id'], 
        "isQueued": False,
        "isFinished": False,
        "message": message
      })

      success = True

    elif self.type == TYPE_WELCOME:
      success = reply_manager.send_welcome_message()

    else:
      success = reply_manager.send_photo_error_message()  

    if success == None:
      success = reply_manager.send_error_message()

    return success

