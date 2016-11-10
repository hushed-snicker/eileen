# Eileen Chatbot


# ChatterBot Imports
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(

                   # Name

                   'Eileen',


                   # Storage Adapter init

                   storage_adapter = 'chatterbot.adapters.storage.JsonFileStorageAdapter',
                   database = './eileen.chatterbot.database.json',


                   # I/O Adapter init

                   input_adapter = 'chatterbot.adapters.input.TerminalAdapter',
                   output_adapter = 'chatterbot.adapters.output.TerminalAdapter',

                   # Logic Adapter init
                   logic_adapters = [
                                    'chatterbot.adapters.logic.MathematicalEvaluation',
                                    'chatterbot.adapters.logic.TimeLogicAdapter',
##                                    'chatterbot.adapters.logic.ApproximateSentenceMatchAdapter',  # Missing english stopwords corpus
##                                    'chatterbot.adapters.logic.ClosestMeaningAdapter',            # Missing english stopwords corpus
##                                    'chatterbot.adapters.logic.MultiLogicAdapter',                # Not sure if needed. Crashes with an error when used
##                                    'chatterbot.adapters.logic.SentimentAdapter',                 # Makes her only respond with, "Can I have a cup of sugar?"
                                    'chatterbot.adapters.logic.ClosestMatchAdapter'
                                    ]

                 )

# Training Functions

# Trains the chatbot in English
def train_in_english():
  chatbot.set_trainer(ChatterBotCorpusTrainer)
  chatbot.train('chatterbot.corpus.english')

# Get Response Function
### Returns response
###### From chatterbot import ChatBot
######### chatbot = ChatBot('Eileen')
######### chatbot.get_response()

def print_response():
  response = chatbot.get_response(None)
  return response


# Train
train_in_english()

# Pre-Main Print
print('Please tell Eileen "Hello!"')

# Main Loop

while True:
  try:

    print_response()

  except(KeyboardInterrupt, EOFError, SystemExit):
    break
