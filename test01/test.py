#!/usr/bin/env python3

a = 5
b = 12

if a == b:
    print ("a = b")
elif a > b:
    print("a > b")
else:
    print("a < b")

a = 1
while a < 10:
    if a == 5:
        break
    if a ==3:
        a +=1
        continue
    print(a)
    a +=1


for x in range(10):
    print(x)

a = "ciao mondo"
for x in a:
    print(x)

a = [1,2,3,4,5]
for x in a:
    print("===", x)

dct = {"a":1, "b":2, "c":3}
for x in dct:
    print("DCT: ", x, dct[x])