import pyttsx3
import os
from datetime import  datetime
from time import sleep
hora_desligar = '01:56'
voz = pyttsx3.init()
print(f'o pc sera desligado automaticamente as {hora_desligar} 🖥️')
while True:
    agora = datetime.now().strftime('%H:%M')
    if agora == hora_desligar:
        atencao = 'O computador será desligado em 1 minuto ☠️!'
        print(atencao)
        voz.say(atencao)
        voz.runAndWait()
        sleep(60)
        if os.name=='nt':
            os.system('shutdown /s /t 0 ')
        else:
            os.system('shutdown now')
        break
    else:
        print(f'aguardando.... hora atual: {agora}')
        sleep(30)










