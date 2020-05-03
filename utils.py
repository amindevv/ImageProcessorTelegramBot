import json

class Utils:

  def __init__(self):
    
    pass

  @staticmethod
  def print_json(message):

    print("*****************************")
    print(json.dumps(message, sort_keys= True, indent= 4))
    print("*****************************")

