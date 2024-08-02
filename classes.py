class Animal():
    nome:str
    tamanho:int
    cor:str
    sexo:str
    racionalidade:bool
    coracao:bool
    instinto:bool
    def __init__(self, nome, tamanho, sexo):
        self.nome = nome
        self.tamanho = tamanho
        self.sexo = sexo
        self.coracao = True

class Humano(Animal):
    def __init__(self, nome, tamanho, sexo):
        super().__init__(nome, tamanho, sexo)
        self.consciencia = True
        self.racionalidade = True
        self.coracao = True
        self.instinto = True

class Cachorro(Animal):
    raca:str
   
    def __init__(self, nome, raca, tamanho, cor, sexo):
        super().__init__(nome, tamanho, sexo)
        self.raca = raca
        self.cor = cor
        self.coracao = True
        self.instinto = True
        self.racionalidade = False
    def latir():
        print("au-au")