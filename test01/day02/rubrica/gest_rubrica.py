#!/usr/bin/env python3

import json
import sys

from rubrica import Rubrica


def menu():
    print("1 - Nuovo contatto")
    print("2 - Visualizza contatti")
    print("3 - Modifica contatto")
    print("4 - Elimina contatto")
    print("5 - Trova contatti")
    print("x - Esci")

    while True:
        scelta = input("Scegliere un opzione: ")
        scelta = scelta.lower().strip()
        if len(scelta) > 1:
            scelta = scelta[0]
        if scelta in ["1", "2", "3", "4", "5", "x"]:
            return scelta
        else:
            print("scelta non valida")


def aggiungiContatto():
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    telefono = input("Telefono: ")

    rub.add(nome, cognome, telefono)
    rub.save("rubrica.json")


def visualizzaContatti():
    rub.lista(False)


def eliminaContatto():
    rub.lista(True)
    indice = input("Che contatto vuoi eliminare (indice): ")
    if indice == "":
        return
    indice = int(indice)
    if indice >= len(rub.contatti):
        print("contatto inesistente")
    else:
        rub.remove(indice)
        print("contatto eliminato con successo")


def modificaContatto():
    rub.lista(True)
    indice = input("Che contatto vuoi modifica (indice): ")
    if indice == "":
        return
    indice = int(indice)
    if indice >= len(rub.contatti):
        print("contatto inesistente")
        return
    nome = input("Nome (" + f"{rub.contatti[indice].nome}" + ") : ")
    if nome == "":
        nome = rub.contatti[indice].nome
    cognome = input("Cognome (" + f"{rub.contatti[indice].cognome}" + ") : ")
    if cognome == "":
        cognome = rub.contatti[indice].cognome
    telefono = input("Telefono (" + f"{rub.contatti[indice].telefono}" + ") : ")
    if telefono == "":
        telefono = rub.contatti[indice].telefono
    rub.modifica(indice, nome, cognome, telefono)


def trovaContatti():
    cercaStr = input("Stringa da cercare: ")
    if cercaStr == "":
        return
    rub.cercaStringa(cercaStr)


#########################################
# Inizio Programma

rub = Rubrica()
rub.load("rubrica.json")

while True:
    scelta = menu()
    if scelta == "x":
        break
    elif scelta == "1":
        aggiungiContatto()
    elif scelta == "2":
        visualizzaContatti()
    elif scelta == "3":
        modificaContatto()
    elif scelta == "4":
        eliminaContatto()
    elif scelta == "5":
        trovaContatti()
