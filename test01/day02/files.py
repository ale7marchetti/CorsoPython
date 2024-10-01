#!/usr/bin/env python3

# file binario / file di testo

# file_txt = open("nome file","r") 
# file_txt = open("nome file","rb") binario


filein = open("txt1.txt","r")
content = filein.read()

filein = open("txt1.txt","r")
for line in filein:
    line = line.strip()
    print("LINE: ", line)


# file_txt = open("nome file","w") 
# file_txt = open("nome file","wb") binario

fileout = open("output.txt","w")
fileout.write("ciao mamma\n")

dct = {
    "a":1,
    "b":2,
    "c":3
}

import json
fileout = open("dct.json", "w")
fileout.write(json.dumps(dct, indent=4))
fileout.close()

dct2 = json.loads(open("dct.json","r").read())
print(dct2)

import datetime

d = datetime.datetime.now()
dct = {"date": d}
fileout = open("dct-date.json", "w")
fileout.write(json.dumps(dct, indent=4,default=str))
fileout.close()





