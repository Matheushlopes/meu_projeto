import requests

def dol_real():
    real = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    real = real.json()
    real = real['USDBRL']
    real = real['bid']
    real = float(real)

    return real

def bit_real():
    bitcoin = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    bitcoin = bitcoin.json()
    bitcoin = bitcoin['BTCBRL']
    bitcoin = bitcoin['bid']
    bitcoin = float(bitcoin)

    return bitcoin

def eur_real():
    euro = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    euro = euro.json()
    euro = euro['EURBRL']
    euro = euro['bid']
    euro = float(euro)

    return euro
