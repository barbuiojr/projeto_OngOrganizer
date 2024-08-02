from classes import *
from time import sleep
from views import *
from coleta_dados import *
from listagens import *
op = 0
while op != 4:
    op = menu_inicial()
    if op == 1:
        cria_cachorro()
        
    if op == 2:
        cria_pessoa()

    if op == 3:

        op1 = menu_secundario()
        if op1 == 1:
            lista_cachorros()

        if op1 == 2:
            lista_pessoas()
        flag = input('Tecle algo para continuar--->')
        