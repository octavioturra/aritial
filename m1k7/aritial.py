#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response, get_list_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest

from google.appengine.api import users
from google.appengine.ext import db

from datetime import datetime

from m1k7.models import *

import re

def fillProfile(content):
    c = Cliente()
    user = users.get_current_user()
    client = db.GqlQuery("SELECT * FROM Cliente WHERE user = :1", user)
    c = client[0]
    retorno = ""
    if c.nome is None:
        nome = re.findall("(?<=ou )[A-Z]\S+[^., ?]", content)
        if nome:
            c.nome = nome[0]
            r = nome[0]
            apelido = re.findall("[A-Z]\S{1}[aeioun]",nome[0])
            if apelido:
                c.apelido = apelido[0]
                r = apelido[0]
        retorno = retorno + r + ", gostei!! "
        c.put()
    else:
        retorno = "Entao "+ c.nome
    if c.idade is None:
        idade = re.findall("\d{2}|\d{4}", content)
        if idade and len(idade[0])<=2:
            idade = int(idade[0])
            c.idade = idade
            if idade==18:
                retorno = retorno + "Ahh, já pode ir pra cadeia ein, cuidado!!"
            elif idade>18:
                retorno = retorno + " Uia!!"
            else:
                retorno = retorno + "Nossa, joven ahn!"
        else:
            retorno = " Quantos anos você tem? "
        c.put()
    if c.profissao is None and c.nome is not None:
        pro = re.findall("(?<=ou )|(?<=a.o )\S+[^., ?]", content)
        if pro:
            pro = pro[0]
            c.profissao = pro
            retorno = retorno + " %s, hum, bela profiss&atildeo!" % pro
            c.put()
        else:
            retorno = retorno + " O que faz da vida?"
#    if c.profissao is not None and c.nome is not None and c.idade is not None:
#        retorno = '''<br /><ul>
#            <li>Nome: %s</li>
#            <li>Apelido: %s</li>
#            <li>Idade: %s</li>
#            <li>Profissao: %s</li>
#        </ul><small>DESCULPE, A VERSÃO DE TESTES TERMINA AQUI..ESTAMOS TRABALHANDO PARA DESENVOLVE-LA</small><a href='#contato'>Entre em contato e saiba mais.</a>''' %(c.nome, c.apelido, c.idade, c.profissao)
    return retorno

def getContent(request):
    user = users.get_current_user()
    cliente = db.GqlQuery("SELECT * FROM Cliente WHERE user = :1",user)
    try:
        content = request.POST["content"]
        clienteContent = "<small>%s</small><q>%s</q>" % (datetime.today(), content)
        #value = "%s %s" % (fillProfile(content), clienteContent)
        value = "<small>%s</small><q>%s</q><small>%s</small><q>%s</q>" % (datetime.today(), 'Conteúdo escrito pelo usuário', datetime.today(), fillProfile(content))
        #value = content
    except:
        if cliente[0].nome is not None:
            value = "<small>%s</small><q>Oi %s.</q>" %(datetime.today(),cliente[0].nome)
        else:
            value = "<small>%s</small><q>Oie, sou Aritial, quem &eacute; você?</q>" %(datetime.today())
    return HttpResponse(value)

def study(request):
    user = users.get_current_user()
    k = Knowledge()

    l = KnowLib()
    content = request.FILES['livro'].read()
    l.value = db.Blob( content )
    l.put()

    frases = re.findall("[^\.\,\?]\S+[^\.\?]+.",content)
    if frases:
        k.sender = user
        i = 0
        for item in frases:
            i = i+1
            if i>50:
                break
            k.frase = unicode(item, 'utf8')
            k.put()
    return HttpResponseRedirect("/#aritial")
#    return HttpResponse()
