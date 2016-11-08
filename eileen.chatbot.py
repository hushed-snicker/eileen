# Eileen Chatbot


# ChatterBot Imports
from chatterbot import ChatBot
#from chatterbot.trainers import 

chatbot = ChatBot(

                   # Name

                   'Eileen',


                   # Storage Adapter init

                   storage_adapter = 'chatterbot.adapters.storage.JsonFileStorageAdapter',
                   database = '../eileen.chatterbot.database.json',


                   # I/O Adapter init

                   input_adapter = 'chatterbot.adapters.input.TerminalAdapter',
                   output_adapter = 'chatterbot.adapters.output.TerminalAdapter',

                   # Logic Adapter init
                   logic_adapters = [
                                    'chatterbot.adapters.logic.MathematicalEvaluation',
                                    'chatterbot.adapters.logic.TimeLogicAdapter',
                                    'chatterbot.adapters.logic.ClosestMatchAdapter'
                                    ]

                 )

# Training Function

# Get Response Function
### Returns response
###### From chatterbot import ChatBot
######### eileen.chatbot = ChatBot('Eileen')
######### eileen.chatbot.getresponse()

def print_response():
  response = chatbot.get_response(None)
  return response





# Pre-Main Print
print('Please tell Eileen "Hello!"')
chatbot.get_response('Hello')

# Main Loop

while True:
  try:

    # Input code here

    # Some garbage test code
    print_response()

  except(KeyboardInterrupt, EOFError, SystemExit):
    break
