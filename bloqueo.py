#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from asterisk.agi import AGI
agi = AGI()

#print("Lista de argumentos: ", sys.argv[1])

CALLER_ID = sys.argv[1]
#print(CALLER_ID)

def inBlacklList(EXTEN):
    file_blacklist = '/var/lib/asterisk/agi-bin/blacklist-asterisk/blacklist.txt'
    with open(file_blacklist, 'r') as fp:
        lineas = set(fp.readlines())

    for i in lineas:
        print("--->", i)
        if i.rstrip() == EXTEN || i.lstrip() == EXTEN:
            return True
        else:
            return False
bloqueado = inBlacklList(CALLER_ID)
#print(bloqueado)
agi.set_variable("IN_BLACKLIST", bloqueado)
