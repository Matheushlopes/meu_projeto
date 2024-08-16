from flask import Blueprint,render_template,url_for
from functions.api_moedas import *


home_route = Blueprint('home',__name__)

@home_route.route('/')
def home():
    rl = dol_real()
    bit = bit_real()
    eur = eur_real()
    eur = float(f'{eur:.3f}')
    bit = float(f'{bit:.3f}')
    rl = float(f'{rl:.3f}')
    return render_template('index.html', bit=bit, rl=rl, euro=eur)





    