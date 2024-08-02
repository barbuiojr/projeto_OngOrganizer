import os
from classes import *
from coleta_dados import *

def menu_inicial():
    os.system("cls")
    print("""1 - Criar objeto CACHORRO
2 - Criar objeto HUMANO
3 - Imprimir objetos criados
4 - Sair""")
    op = input('---> ')
    while not op.isnumeric():
        op = input('Opção inválida.\nVocê deve escolher um número do menu.')
        print(op)
    while int(op)<1 or int(op)>4:
        op = input('Opção inválida\nAs opções disponíveis vão de 1 a 4:')
    os.system("cls")
    return int(op)

def menu_secundario():
    print("""1 - Imprimir cachorros
2 - Imprimir pessoas""")
    op = input('---> ')
    while not op.isnumeric():
        op = input('Opção inválida.\nVocê deve escolher um número do menu.')
        print(op)
    while int(op)<1 or int(op)>2:
        op = input('Opção inválida\nAs opções disponíveis são 1 e 2:')
    os.system("cls")
    return int(op)