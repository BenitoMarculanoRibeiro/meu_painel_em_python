from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
print('oi')


def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('Microfone...')
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
    except sr.UnknownValueError:
        print('bot: Isso não funcionou!')
    return frase

def cria_audio(audio):
    tts = gTTS(audio, language='pt-BR')
    tts.save('bot.mp3')
    playsound('bot.mp3')
bot = ChatBot("Chatbot")
print('oi')

conversa = ['Oi',
            'Ola',
            'Tudo bem?',
            'Tudo bem, e você?',
            'Eu estou bem',
            'Que bom.',
            'Qual o melhor sistema?',
            'O melhor sistema é o Linux.']

trainer = ListTrainer(bot)
trainer.train(conversa)
while True:
    quest = ouvir_microfone()
    resposta = bot.get_response(quest)
    cria_audio(str(resposta))
    print('Bot: ', resposta)