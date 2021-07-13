from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
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
    database_uri='sqlite:///db.sqlite3',
  
)


# def Train():
#     input_file = open('./data_train_jarvis.txt', "r")  
#     data_talk = input_file.readlines()
#     # print(data_talk)
#     list_trainer = ListTrainer(jarvis)
#     list_trainer.train(data_talk)
#     input_file.close()
                                


# def EnToVi(text):
#     text = translator.translate(text, src='en', dest='vi')
#     return text.text

# def ViToEn(text):
#     text = translator.translate(text, src='vi', dest='en')
#     return text.text

# def Chat():
#     reply = input("Reply: ")
#     i= ViToEn(reply)
#     jarvis_rep = jarvis.get_response(i)
#     t = EnToVi(jarvis_rep)
#     # print(t)
#     # print("Jarvis: ", t, "   ("+i+") (",jarvis_rep,")")
#     print("Jarvis: ", t)


def InputChat(message):
    # i= ViToEn(message)
    jarvis_rep = jarvis.get_response(message)
    # t = EnToVi(jarvis_rep)
    return jarvis_rep


# def Start():
#     print("Jarvis: Xin chào")
#     while 1==1:
#         Chat()

# Start()
# Train()
# print(jarvis.get_response("who are you?"))
# print(translator.translate("xin chào.", src='vi', dest='en'))