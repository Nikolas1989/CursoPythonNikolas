class Endereco:
    logradouro = ''
    numero = ''
    complemento = ''
    bairro = ''
    cidade = ''
    CEP = ''
    
    
    
    def cadastrar_endereco(self): 
        self.logradouro = input ('Digite seu logradouro:' '\n')
        self.numero = input ('Digite o numero da casa/apartamento' '\n')
        self.complemento = input ('Digite o complemento' '\n')
        self.bairro = input ('Digite o bairro' '\n')
        self.cidade = input ('Digite a cidade' '\n')
        self.CEP = input ('Digite o CEP''\n')
        return f'logradouro:{self.logradouro} numero:{self.numero} complemento{self.complemento} bairro{self.bairro} cidade{self.cidade} CEP{self.CEP}'