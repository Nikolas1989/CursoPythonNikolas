class Pessoa: 
    nome =''
    sobrenome = ''
    Email = ''
    Data_de_nascimento = ''
    Senha = ''

    
    def cadastrar_pessoa(self): 
        self.nome = input ('Digite seu nome:' '\n')
        self.sobrenome = input ('Digite o seu sobrenome' '\n')
        self.Email = input ('Digite o seu Email' '\n')
        self.Data_de_nascimento = input ('Digite a sua data de nascimento' '\n')
        self.Senha = input ('Digite a sua senha' '\n')
        return f'Nome:{self.nome} Sobremoe:{self.sobrenome} E-mail{self.Email} Data_de_nascimento{self.Data_de_nascimento} Senha{self.Senha}'
    
  