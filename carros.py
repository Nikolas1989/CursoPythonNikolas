class Carro:
    def __init__(self, marca ='', modelo='', categoria='', ano=0):
        self.marca = marca
        self.modelo = modelo 
        self.categoria = categoria
        self.ano = ano

    def lista_todos(self):
        lista_carros = []
        with open ('carros.txt', 'r') as arquivo :
            for l in arquivo:
                cl = l.strip().split(';')
                carro = Carro (cl[0], cl[1], cl[2], cl[3])
                lista_carros.append(carro)
        return lista_carros

        #--Método para cadastro em arquivo texto

    def cadastrar_carro(self, carro):
        with open ('carros.txt', 'a') as arquivo :
        #-- Ao gravar a linha no arquivo texto f' {self}\n', o self, que é a própria classe
        #-- é convertida em string, a ao ser convertida, é chamado o método __str__ declarado abaixo
            arquivo.write (f'{self}\n')

        #-- Método de conversão da classe para string
        #-- Sempre que a classe for convertida para string (ste()) este método será chamado
    def __str__(self):
        return f'{self.marca};{self.modelo};{self.categoria};{self.ano}'

    
        # self.marca = input ('Digite sua marca' '\n')
        # self.modelo = input ('Digite o modelo' '\n')
        # self.categoria = input ('Digite a categoria''\n')
        # self.ano = input ('Digite o ano''\n')
        # return f'marca:{self.marca} modelo:{self.modelo} categoria = {self.categoria} ano = {self.ano}' 


         


