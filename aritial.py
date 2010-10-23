#!/usr/bin/env python
#-*- coding:utf-8 -*-

#Aritial

import re

#ese = open("/home/fraguto/Web/aritial/ESE.db")
#ese_r = ese.read()
#ese.close()

ruleFrase = "\S+[^\.\,\?]+"
ruleNome = "[A-Z]\S+[^\,\.\ \?]"

a = "Oi sou Octávio, quem é voce?"

#b = re.findall("\S{3,9}",a)

#    print(b)

#b = re.findall(ruleFrase,ese_r)

import sqlite3

db = sqlite3.connect("./frases.dbpy")

cr = db.cursor()

#cr.execute("create table if not exists frases(id integer primary Key autoincrement, frase varchar(512))")

#for item in b:
#    try:
#        cr.execute("insert into frases(frase) values('"+item+"')")
#    except:
#        print("erro na frase:"+item)

#db.commit()

fooregex = r'aa.[0-9]'
cr.execute("select frase from frases where frase regex %s", tuple( fooregex ))

for item in cr:
    print item

import os
print os.getcwd()

cr.close()
