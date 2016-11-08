# Eileen Chatbot


# ChatterBot Imports
from chatterbot import ChatBot
#from chatterbot.trainers import 

chatbot = ChatBot(

                   # Name

                   'Eileen',


                   # Storage Adapter init

                   storage_adapter = 'chatterbot.adapters.storage.jsonfile',
                   database = './eileen.chatterbot.database.json',


                   # I/O Adapter init

                   input_adapter = 'chatterbot.adapters.input.terminal',
                   output_adapter = 'chatterbot.adapters.output.terminal',

                   # Logic Adapter init
                   logic_adapters = [
                                    'chatterbot.adapter.logic.mathematical_evaluation'
                                    'chatterbot.adapter.logic.time_adapter'
                                    ]

                 )

# Training Function

# Get Response Function
### Returns response
###### From chatterbot import ChatBot
######### eileen.chatbot = ChatBot('Eileen')
######### eileen.chatbot.getresponse()

def get_response():
  response = chatbot.getresponse()
  return response





# Pre-Main Print
print('Eileen was told "Hello!"')
chatbot.getresponse('Hello!')

# Main Loop

while True:
  try:

    # Input code here

    # Some garbage test code
    # Eileen v 0.0.1; I guess...
    response = get_response()
    print response

  except(KeyboardInterupt, EOFError, SystemExit):
    break
