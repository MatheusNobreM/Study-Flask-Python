# ESTE É SÓ O CÓDIGO UTILIZADO PARA À API MAS FOI FEITO NO "replit.com"

import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
  return 'Api no ar.'

@app.route('/totaldevendas')
def totaldevendas():
  df = pd.read_csv("API_Python.csv")
  total_vendas = df["Vendas"].sum()
  res = {"total_vendas": total_vendas}
  return jsonify(res)

# rodar a api
app.run(host='0.0.0.0')