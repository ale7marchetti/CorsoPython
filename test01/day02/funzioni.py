#!/usr/bin/env python3

# def nome_funzione(parametri):
#     #codice
#     return valore

def f1(a,b):
    return a+b

def f2(a,b=10):
    return a+b

def f3(*args):
    #args = nome convenzionale
    print ("=== ARGS: ", args)
    return sum(args)

def f4(a,b ,**kwargs):
    return a+ b + sum(kwargs.values())
print()
