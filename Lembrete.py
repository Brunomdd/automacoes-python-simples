import pyttsx3
from time import sleep
voz = pyttsx3.init()
cont = 0
limite = 3
while True:
    voz.say('Chega de jogar por hoje!')
    voz.runAndWait()
    cont +=1
    if cont >= limite:
        break
    sleep(3600)