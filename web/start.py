from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return '<h1> Python </h1>'

@app.route('/cerveja')
def cerveja():
    return '<h1> Cerveja </h1>'

app.run()



