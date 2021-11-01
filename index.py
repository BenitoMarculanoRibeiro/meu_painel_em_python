import gtts
from pydub import AudioSegment
from pydub.playback import play
from pygame import mixer

with open('frase.txt', 'r') as arquivo:
    cont = 0
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='pt-br')
        frase.save('frase.wav')
        mixer.init()  # initiate the mixer instance
        mixer.music.load('frase.wav')  # loads the music, can be also mp3 file.
        mixer.music.play()  # plays the music
        cont += 1
