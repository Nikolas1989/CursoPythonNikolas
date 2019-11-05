
from pessoa import Pessoa
from cadastro_endereco import Endereco

print('=' *50)
print('\n' *3)
#print(pessoa)#

p1 = Pessoa()
print(p1.cadastrar_pessoa())
end = Endereco()
print(end.cadastrar_endereco())
 
print( p1.nome )
print( end.logradouro) 

#print ('Nome:{}'.format (nome)) 

print('\n' *2)
print('=' *50)