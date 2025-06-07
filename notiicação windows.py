from time import sleep
from plyer import notification
from datetime import datetime
from time import  sleep
hora_agendada = '02:05'
while True:
    hora_atual = datetime.now().strftime('%H:%M')
    print(f'Agora são {hora_atual}...')
    sleep(30)
    if hora_atual == hora_agendada:
        notification.notify (
            title = 'Lembrete',
            message = 'Teste ',
            timeout = 10
        )
        break



