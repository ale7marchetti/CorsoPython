#!/usr/bin/env python3


# https://learngitbranching.js.org/

tpl = (
    ("+", 1, 2, 3, 4, 5),
    ("*", 5, 4, 3),
    ("-", 100, 20, 30),
    ("/", 120, 5),
    ("/", 100, 20, 30, 10, 5),
)


def somma(numeri):
    risultato = 0
    for numero in numeri:
        risultato += numero
    return risultato


def molt(numeri):
    risultato = 1
    for numero in numeri:
        risultato = risultato * numero
    return risultato


def sottrazione(numeri):
    risultato = numeri[0]
    for numero in numeri[1:]:
        risultato = risultato - numero
    return risultato


def divisione(numeri):
    risultato = numeri[0]
    for numero in numeri[1:]:
        risultato = risultato / numero
    return risultato


i = 0
i2 = 1

for i in range(len(tpl)):
    operazione = tpl[i][0]
    if operazione == "+":
        numeri = tpl[i][1:]
        risultato = somma(numeri)
        print(f"risultato somma : {risultato}")
    if operazione == "*":
        numeri = tpl[i][1:]
        risultato = molt(numeri)
        print(f"risultato moltiplicazione : {risultato}")
    if operazione == "-":
        numeri = tpl[i][1:]
        risultato = sottrazione(numeri)
        print(f"risultato sottrazione : {risultato}")
    if operazione == "/":
        numeri = tpl[i][1:]
        risultato = divisione(numeri)
        print(f"risultato divisione : {risultato}")
