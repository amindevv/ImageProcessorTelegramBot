from utils import Utils

TYPE_PHOTO = 0
TYPE_TEXT = 1
TYPE_WELCOME = 2

class BotRequestManager:

  def __init__(self, request):

    # This guy defines the type of reply bot should send
    self.type = None
    self.request = request

  """ Parses Telegram JSON request from webhook 
  and sets fields for conditional actions. Most importantly,
  it defines the Type of the message which is later used for
  specific actions based on the Type """
  def parse_request_data(self):

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

  """ Does different task based on Type """
  def get_result(self):

    success = None 

    return success

