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
    user = db.UserProperty()
    nome = db.StringProperty()
    apelido = db.StringProperty()
    cidade = db.StringProperty()
    profissao = db.StringProperty()
    idade = db.IntegerProperty()

class Knowledge(db.Model):
    sent_on = db.DateTimeProperty(auto_now_add=True)
    sender = db.UserProperty()
    frase = db.TextProperty()

class KnowLib(db.Model):
    sent_on = db.DateTimeProperty(auto_now_add=True)
    sender = db.UserProperty()
    value = db.BlobProperty()
