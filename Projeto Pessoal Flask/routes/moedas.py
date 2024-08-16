from flask import Blueprint,render_template
from functions.api_moedas import *

moeda_route = Blueprint('moeda',__name__)

@moeda_route.route('/')
def dolar():

    real = dol_real()
    real = float(f'{real:.3f}')
    return render_template('dolar.html', real=real)


@moeda_route.route('/bitcoin')
def bitcoin():

    btc = bit_real()
    btc = float(f'{btc:.3f}')
    return render_template('bitcoin.html', bitcoin=btc)

@moeda_route.route('/euro')
def euro():

    euro = eur_real()
    euro = float(f'{euro:.3f}')
    return render_template('euro.html', euro=euro)