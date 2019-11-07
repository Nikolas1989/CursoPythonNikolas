
from flask import Flask, render_template
from aluno import aluno
from avaliacoes import Avaliacoes

aluno1 = aluno()
aluno1.nome = 'Nikolas'
aluno1.sobrenome = 'Roger'
aluno1.usuario = 'nik'
aluno1.senha = '12345'

aluno2 = aluno()
aluno2.nome = 'Greice'
aluno2.sobrenome = 'Berto'
aluno2.usuario = 'Gre'
aluno2.senha = '6789'

avaliacoes1 = Avaliacoes()
avaliacoes1.data = '12-11-2011'
avaliacoes1.avaliacao = 'Provinha'
avaliacoes1.nota = '8'

avaliacoes2 = Avaliacoes()
avaliacoes2.data = '08-04-2011'
avaliacoes2.avaliacao = 'provao'
avaliacoes2.nota = '4'


app = Flask(__name__)

nome_pagina = 'Página do Joao'
lista = [aluno1, aluno2]
lista2 = [avaliacoes1, avaliacoes2]

# lista = [' Joao','Maria', 'Flavio','Olga', 'Greice', 'Dasha', 'Bruna']



@app.route('/')
def inicio():
    return render_template('home.html', nome = nome_pagina, lista = lista)

@app.route('/contato')
def contatos():
    return render_template('contato.html', nome = nome_pagina, nome_avaliacoes = lista2)

app.run()
