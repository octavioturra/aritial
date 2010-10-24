#!/usr/bin/env python
#-*- coding:utf-8 -*-

from appengine_django.models import BaseModel
from google.appengine.ext import db
from google.appengine.api import users

#class Visitor(db.Model):
#    user = db.StringProperty()
#    added_on = db.DateTimeProperty(auto_now_add=True)
#    message = db.StringProperty()

class Cliente(db.Model):
    '''
        Cliente

        Entidade do usuário do Aritial
            user = usuário logado
            nome = nome a ser descoberto pelo Aritial
            apelido = caso a terceira letra do nome seja uma vogal, as 3 primeiras
            serão o apelido
            cidade = (DESENVOLVER!!!)
            profissao = (CORRITIR!!!)
            idade = o Aritial tentará identificar sua idade

    '''
    user = db.UserProperty()
    nome = db.StringProperty()
    apelido = db.StringProperty()
    cidade = db.StringProperty()
    profissao = db.StringProperty()
    idade = db.IntegerProperty()

class Knowledge(db.Model):
    '''
        Knowledge

        Base de conhecimento que será complementada com os livros enviados
        e com os textos escritos pelos usuários.
    '''
    sent_on = db.DateTimeProperty(auto_now_add=True)
    sender = db.UserProperty()
    frases = db.ListProperty(str)

class KnowLib(db.Model):
    '''
        KnowLib

        Biblioteca do aritial.

        PLAN:
            O Aritial não leria os livros assim que enviados, mas sim através
            de tarefa Cron, no período da noite.
            Selecionaria somente os autorizados pelos professores dele.
    '''
    sent_on = db.DateTimeProperty(auto_now_add=True)
    sender = db.UserProperty()
    value = db.BlobProperty()
