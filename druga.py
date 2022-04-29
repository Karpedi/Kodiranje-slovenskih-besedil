'''
* Copyright (c) 2021 University of Ljubljana, Faculty of Electrical Engineering.
* All rights reserved. Licensed under the Academic Free License version 3.0.
* 
'''

import math
import time
import sys
#navodila za delo s programom pogledamo tako, da preprosto zazenemo datoteko druga.py
if len(sys.argv[0])!=0:
 print("NAVODILA:\nsys.argv[1]-> datoteka ki jo odpremo\nsys.argv[2]-> kodiranje datoteke\nsys.argv[3]-> željeno kodiranje izhodne datoteke\nMOŽNi KODI:Cp1250,Cp852,ISO8859_2,UTF-8,UTF-16BE,UTF-16LE, mac_latin2")
 print("sumniki: Č, Š, Ž, č, š, ž")
 
f = open(sys.argv[1], "r", encoding=sys.argv[2])
text = f.read()
f.close()
zapisi = open("Zapisano-V-" + sys.argv[3] + "-IZ_DAT-" + sys.argv[1], mode="w", encoding=sys.argv[3])
zapisi.write(text)
zapisi.close()

sumniki = ["Č","Š","Ž","č","š","ž"]
kodiena = ["Cp1250","Cp852","ISO8859_2","mac_latin2"]
kodidva = ["UTF-8","UTF-16BE", "UTF-16LE"]
for kod in kodiena :
    #sestavim tabelo encoded sumnikov za vse sumnike
    encodedSumniki = list(map(lambda s: s.encode(kod), sumniki)) 
    desetiski = [ord(s) for s in encodedSumniki]
    dvojiski = [bin(s) for s in desetiski]
    sestnajstiski = [hex(s) for s in desetiski]

    print('\n KODIRANJE: ', kod)
    print("DEC: ", desetiski)
    print("BIN: ", dvojiski)
    print("HEX: ", sestnajstiski)


for kodT in kodidva :
    #sestavim tabelo encoded sumnikov za vse sumnike
    encodedSumnikiT = list(map(lambda sT: sT.encode(kodT), sumniki)) 
    desetiskiT = [int.from_bytes(sT, 'big') for sT in encodedSumnikiT] #iz vec bytov naredi intiger
    dvojsikiT = [bin(sT) for sT in desetiskiT]
    sestnajstiskiT = [hex(sT) for sT in desetiskiT]

    print('\n KODIRANJE: ', kodT)
    print("DEC_T: ",desetiskiT)
    print("BIN_T: ",dvojsikiT)
    print("HEX_T: ",sestnajstiskiT)