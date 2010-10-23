#-*- coding:utf-8 -*-

# Create your views here.

#from django.template import Context, loader
from google.appengine.api import users
from google.appengine.ext import db

from google.appengine.api import mail

from django.shortcuts import render_to_response, get_list_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django import forms

from m1k7.models import Cliente

import md5

def main(request):
    user = users.get_current_user()
    if user:
        sistema = "aritial"
    else:
        sistema = "sistema"
    return render_to_response('index.html', {'sistema':sistema})

def home(request):
    return render_to_response('home.html', {})

def system(request):
    loginUrl = users.create_login_url("/#aritial")
    return render_to_response('services.html', {'log':loginUrl})

def contato(request):
    return render_to_response('contato.html', {})

def aritial(request):
    cliente = Cliente()
    user = users.get_current_user()
    dbUser = db.GqlQuery("SELECT * FROM Cliente WHERE user = :1",user)
    try:
        dbUser[0].user
    except:
        cliente.user = user
        cliente.put()
    logofUrl = users.create_logout_url("/#home")
    user = user.nickname()
    hkey = md5.new()
    hkey.update(str(user))
    hkey = hkey.hexdigest()
    return render_to_response('aritial.html',{'logoff':logofUrl,'key':hkey})

def email(request):
    mail.send_mail(sender='octavio.turra@gmail.com',to="octavio.turra@gmail",subject=request.POST["nome"],body = "Enviado por: " + request.POST["email"] +" Mensagem:" + request.POST["corpo"])
    return HttpResponse("Obrigado pela sua mensagem!")