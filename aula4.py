#abertura do arqeuivo texto para gravação

arquivo = open('alunos.txt', 'r',)
for d in arquivo: 
    print(d)
arquivo.close()

 #abertura do arquivo texto para leitura
arquivo = open('alunos.txt','a')
arquivo.write('Testando insercao\n')

#abertura do arqeuivo para gravação com fechamento automático
with open ('alunos.txt', 'a') as arquivo :
    arquivo.write('testando fechamento automatico\n')


@app.route('/salvar')
def salvar():
    return 'salvo'

app.run (debug=True)