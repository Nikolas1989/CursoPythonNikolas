
from flask import Flask, render_template
from aluno import aluno
from avaliacoes import Avaliacoes

aluno1 = aluno('Nikolas', 'Roger', 'nik', '12345')

aluno2 = aluno('Greice', 'Berto','Gre','6789')
aluno2.nome = 'Greice'
aluno2.sobrenome = 'Berto'
aluno2.usuario = 'Gre'
aluno2.senha = '6789'

avaliacoes1 = Avaliacoes('12-11-2011', 'Provinha', '8')
avaliacoes2 = Avaliacoes('08-04-2011', 'provao', '4')

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
