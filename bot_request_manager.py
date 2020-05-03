from utils import Utils

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

    

    pass

  """ Does different task based on Type """
  def get_result(self):

    success = None 

    return success

