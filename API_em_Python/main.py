import pandas as pd
from flask import Flask

app = Flask(__name__)

#contruir as funcionalidades
@app.route('/')
def homepage():
  return 'ESSA É A HOMEPAGE DO NOSSO SITE'

@app.route('/Contatos')
def homepage():
    return 'Contatos'
  
#rodar a API
app.run(host='0.0.0.0')
  
#tabela = pd.read_csv('advertisment.csv')
#total_vendas = tabela['Vendas'].sum()
#print(total_vendas)