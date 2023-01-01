# --------------------Imports------------------------------- #
import requests;
import json;


# --------------------Code-------------------------------- #
requisitos = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL,EUR-BRL')

quotes = requisitos.json()
quotes
#--DOLAR--#
print('DOLAR: R$' + quotes['USD']['bid'])
#--EURO--#
print('EURO: R$' + quotes['EUR']['bid'])
