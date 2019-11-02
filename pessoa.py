class Pessoa: 
    
    
    def cadastrar_pessoa(self): 
        nome = input ('Digite seu nome:' '\n')
        sobrenome = input ('Digite o seu sobrenome' '\n')
        Email = input ('Digite o seu Email' '\n')
        Data_de_nascimento = input ('Digite a sua data de nascimento' '\n')
        Senha = input ('Digite a sua senha' '\n')
        return f'Nome:{nome} Sobremoe:{sobrenome} DtNasc{Data_de_nascimento} E-mail{Email} Senha{Senha}'
    
  