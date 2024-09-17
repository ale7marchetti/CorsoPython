#!/usr/bin/env python3

#lst2 = list()

lst = []

# aggiungo un elemento in fondo
lst.append(1)
lst.append(2)
lst.append(3)

print(lst)

# aggiunto un elemento a inizio lista
lst.insert(0,0)
print(lst)

lst = ["a", "b", "c"]
# aggiungo ciao a inizio lista
lst.insert(0, "ciao")
print(lst)

lst = [1,2,3,4,5]
n = lst.pop()
n = lst.pop()
n = lst.pop()

#del lst[3]

#ricerco un elemento nella lista
lst = ["novara","milano","varese","cremona","napoli"]

#cerco elemento con val = varese
n = lst.index("varese")
print(n)

if "to" in lst:
    print("torino è presente")
else:
    print("torino non è presente")

#primo elemento della lista
print(lst[0])

#ultimo elemento della lista 
print(lst[-1])

#dal secondo elemento della lista fino alla fine 
print(lst[1:])

#ordinamento
lst = [4,7,9,6,2,1,8,7,1,0]
a = lst.sort()
print(a)
print(lst)


#split e join
a = "ciao sdjdsns    dfjdhfj    fjkej   klf"
res =[]
for s in a.split():
    if s:
        res.append(s)

print(" ".join(res))

x = [s for s in a.split() if s]
print(" ".join(x))