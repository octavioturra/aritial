#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re



#entrada = raw_input()
entrada = "Oi, sou Octo tudo bom? Tenho 12 anos, como você está?"

getNome = "(?<=sou )[A-Z]\S+[^., ?]"
getApelido = "\S{3}"

getIdade ="((?<=enho )\d+|\d+(?=anos))|\d{1,2}"


nome = re.findall(getNome, entrada)
apelido = re.search(getApelido, nome[0])
apelido = apelido.group(0)


nome = apelido if re.search("a|e|i|o|u|n$",apelido) else nome[0]

idade = re.findall(getIdade,entrada)
idade = int(idade[0])

print "Oi",nome
print "Nossa você é novo!" if idade<18 else "Já tem carta?"

personalide = "Sou extrovertido, brincalhão, nao sou timido, sou estressado, baixinho, muito irrigado, inflexível, perfeccionista, gosto das coisas do jeito que têm que ser, mas gosto de ajudar."
