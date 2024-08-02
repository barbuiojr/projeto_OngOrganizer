import os
from classes import *
from views import *
from time import sleep

caes = []
pessoas = []
def cria_cachorro():
    nome = input('Digite o nome do cachorro: ')
    raca = input('Digite a raça do cachorro: ')
    tam = int(input('Digite o tamanho do cachorro em centímetros: '))
    cor = input('Digite a cor do cachorro: ')
    sexo = input('Infome o sexo do cachorro: ')
    dog = Cachorro(nome, raca, tam, cor, sexo)
    caes.append(dog)
    print(30*'-')
    print('Objeto criado com sucesso!')
    print(30*'-')
    sleep(2)
    os.system("cls")
def cria_pessoa():
    nome = input('Digite o nome da pessoa: ')
    tam = int(input('Digite a altura da pessoa em centímetros: '))
    sexo = input('Digite o sexo da pessoa: ')
    pessoa = Humano(nome, tam, sexo)
    pessoas.append(pessoa)
    print(30*'-')
    print('Objeto criado com sucesso!')
    print(30*'-')
    sleep(2)
    os.system("cls")