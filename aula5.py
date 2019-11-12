#1 - Criar Classe Carro (Marca, Modelo, Categoria, Ano)
#2 - Criar uma pagina que realiza o cadastro de carro
#3 - Salvar o cadastro em arquivo texto 
#4 - Criar tela que lista os carros cadastrados
#5 - Criar logica que le a lista do arqeuivo texto

from flask import Flask, render_template, request
from carros

nome_pagina = "Carros Usados"
app = Flask(__name__)

@app.route('/')
def inicio():
    lista_carros = []
    with open ('carros.txt', 'r') as arquivo :
        for l in arquivo:
            cl = l.strip()split(';')
            carro = Carro (cl[0], cl[1, cl[2]])
    return render_template('index2.html', lista = lista_carros)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar2', nome = nome_pagina)

@app.route('/salvar')
def salvar():
    marca = request.args["marca"]
    modelo = request.args["modelo"]
    categoria = categora.args ["categoria"]
    ano = ano.args ["ano"]

    carro = Carro(marca, modelo, categoria, ano)
    with open ('carros.txt, a') as arquivo :
        arquivo.write (f'{carro.marca};{carro.modelo};{carro.categoria};{carro.ano}\n')

app.run(debug=True)
