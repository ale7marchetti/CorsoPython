#!/usr/bin/env python3

import json

from contatto import Contatto


class Rubrica:
    def __init__(self):
        self.contatti = []

    def add(self, nome="", cognome="", telefono=""):
        cont = Contatto(nome, cognome, telefono)
        self.contatti.append(cont)

    def modifica(self, pos, nome, cognome, telefono):
        cont = Contatto(nome, cognome, telefono)
        self.contatti[pos] = cont

    def lista(self, show_pos=False):
        for i, cont in enumerate(self.contatti):
            if show_pos:
                print(f"{i}: {cont}")
            else:
                print(cont)

    def remove(self, pos):
        self.contatti.pop(pos)

    def save(self, filename):
        out = []
        for cont in self.contatti:
            out.append(cont.to_json())

        fout = open(filename, "w")
        fout.write(json.dumps(out, indent=2, default=str))

    def load(self, filename):
        self.contatti = []
        data = json.loads(open(filename).read())
        for cont in data:
            c = Contatto("", "", "")
            c.from_json(cont)
            self.contatti.append(c)

    def cercaStringa(self, strcerca):
        filtri = []
        for cont in self.contatti:
            if cont.match(strcerca):
                filtri.append(cont.to_json())
                print(cont)
        return filtri
