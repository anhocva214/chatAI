from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# from googletrans import Translator
# import chatterbot
# from chatterbot.comparisons import LevenshteinDistance
# from chatterbot.response_selection import get_first_response


# translator = Translator()

jarvis = ChatBot(
    name='Jarvis', 
    read_only=True,
    ogic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'

    ],
    # database_uri='sqlite:///db.sqlite3',
  
)


def Train():
    input_file = open('./data_train_jarvis.txt', "r")  
    data_talk = input_file.readlines()
    # print(data_talk)
    list_trainer = ListTrainer(jarvis)
    list_trainer.train(data_talk)
    input_file.close()
                                

Train()
