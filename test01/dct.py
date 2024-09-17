#!/usr/bin/env python3

dct = {}
dct = {"a": 1}

#aggiungo una chiave 
dct["b"] = 2

x = "c"
dct[x] = 3

try:
    print ("=== X:", dct["x"])
except KeyError:
    print("chiave non trovata")
except Exception as e:
    print("errore generio ", e)
finally:
    print("fine try")

#elenco le chiavi
print("Chiavi : ", dct.keys())
#elenco i valori
print("Valori : ", dct.values())

#cancello
del dct["c"]
print(dct)

print(len(dct))

dct2 = {}
if not dct2:
    print("dizionario vuoto")

if "a" in dct:
    print("chiave presente")
else:
    print("chiave non presente")

    