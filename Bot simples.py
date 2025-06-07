# Bot Interativo Básico
falas = 0
from random import choice
resposta = ['Oi','Salve irmãozinho!!','Eai...','Opa mano']


while True:
    pergunta = str(input('Você: ')).lower()
    if 'oi' in pergunta:
        falas+=1
        if falas >=3:
            print("você fala mt kkkkk ")
        else:
            escolha = choice(resposta)
            print('Bot: {}'.format(escolha))
    elif 'tchau' in pergunta:
        print('Bot: Até mais')
        break
    else:
        print('Não entendi nada que você falou . . .')




