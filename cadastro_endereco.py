def endereco(): 
    logradouro = input ('Digite seu logradouro:' '\n')
    numero = input ('Digite o numero da casa/apartamento' '\n')
    complemento = input ('Digite o complemento' '\n')
    bairro = input ('Digite o bairro' '\n')
    cidade = input ('Digite a cidade' '\n')
    CEP = input ('Digite o CEP''\n')
    return f'logradouro:{logradouro} numero:{numero} complemento{complemento} bairro{bairro} cidade{cidade} CEP{CEP}'