import os
from classes import *
from coleta_dados import *

def lista_cachorros():
    for c in caes:
        print(30*'-')
        print(f'Nome do cachorro: {c.nome}')
        print(f'Raça: {c.raca}')
        print(f'Tamanho: {c.tamanho} cm')
        print(f'Cor: {c.cor}')
        print(f'Sexo: {c.sexo}')
        print(30*'-')
def lista_pessoas():
    for p in pessoas:
        print(30*'-')
        print(f'Nome da pessoa: {p.nome}')
        alt = float(p.tamanho)/100
        print('Altura: {:.2f} m '.format(alt))
        print(f'Sexo: {p.sexo}')
        print(30*'-')