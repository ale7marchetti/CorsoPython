#!/usr/bin/env python3

"""rifare rubrica con classi
   fare una classe money che gestisce numeri con 2 cifre decimali, mette la virgola al posto del punto e formatta il numero"""


class Contatto:
    def __init__(self, nome, cognome, telefono):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono
        self.eta = 0

    def __str__(self):
        return f"{self.nome} {self.cognome} {self.telefono}"
    
    def match(self, val):
        """restituisce true se val è contenuto in nome, cognome o telefono"""
        return (val in self.nome) or (val in self.cognome) or (val in self.telefono)
    
    def to_json(self):
        return {
            "nome": self.nome,
            "cognome": self.cognome,
            "telefono": self.telefono,
        }

    def from_json(self, data):
        self.nome = data["nome"]
        self.cognome = data["cognome"]
        self.telefono = data["telefono"]

if __name__ == "__main__":
    c1 = Contatto("Mario", "Rossi", "3333562985")
    print(c1)