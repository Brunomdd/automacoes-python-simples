import os
from time import sleep
while True:
    print('\t[1] Desligamento de computador 🔋')
    print('\t[2] Reiniciar PC 🔁')
    print('\t[3] Cancelar desligamento ⏲️')
    print('\t[4] Sair 🚪')
    opcao = int(input('\tDigite uma opção 🔘:  '))
    if opcao == 1:
        tempo = int(input('Em quantos segundos deseja desligar o PC ?:  🖥️'))
        opr = ''
        while opr != 'S' and opr != 'N':
            opr = str(input('Tem certeza que deseja desligar o computador?  [S/N]:')).upper().strip()
        if opr == 'S':
            print(f'o pc vai desligar em {tempo} segundos')
            os.system(f'shutdown /s /t {tempo}')
        else:
            print('desligamento cancelado')
    elif opcao == 2:
        tempo = int(input('Em quantos segundos deseja reinciar o PC ?: '))
        opr = ''
        while opr != 'S' and opr != 'N':
           opr = str(input('Tem certeza que deseja desligar o computador?  [S/N]:')).upper().strip()
        if opr == 'S':
            print(f'o pc vai reiniciar em {tempo}')
            os.system(f'shutdown /r /t {tempo}')
    elif opcao == 3:
        print('CANCELANDO AGENDAMENTO')
        os.system(f'shutdown /a ')
    elif opcao == 4:
        print('SAINDO . . .')
        break
    else:
        print('\t opção invalida!')