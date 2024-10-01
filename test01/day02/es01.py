#!/usr/bin/env python3

import json
import sys

"""Rubrica 
contatto: nome, cognome, telefono
1 - aggiungi contatto
2 - visualizza contatto
3 - cerca contatto
4 - elimina contatto
x - esci

modifiche dati su file json
ricerca solo su nome
la funzione è input("inserisci nome:")
"""

def nuovo(dct_rub):
    dct_rub[0] = input("Nome: ")
    dct_rub[1] = input("Cognome: ")
    dct_rub[2] = input("Telefono: ")
    return dct_rub

def esci():
    sys.exit(0)


menu = {
    "1": nuovo,
    # "2": visualizza,
    # "3": elimina,
    "x": esci
}

dct_rub = {}

rubrica = open("rubrica.json","w")

print("1 = nuovo\nx = esci")
scelta = input("scelta menu: ")

fn = menu[scelta]
fn(dct_rub)


rubrica.write(json.dumps(dct_rub, indent=4))






