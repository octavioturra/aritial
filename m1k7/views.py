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

'''
    Aritial

    Simples sistema de conversação aleatória baseado em frases dos usuários
    e conteúdo aprendido através de livros txt

    PLAN

        Sistema inteligente de procura que retornará seu perfil e alguns dados
        que você procurar, identificando suas necessidades através de dados
        semânticos e proporcionar um estudo de todo o perfil psicológico do
        usuário.

'''


def main(request):
    '''
        Main

        Página principal com o controle do Ajax
    '''
    user = users.get_current_user()
    if user:
        sistema = "aritial"
    else:
        sistema = "sistema"
    return render_to_response('index.html', {'sistema':sistema})

def home(request):
    '''
        Home

        Página de entrada do site

        PLAN
            Criar um microblog do Aritial, com conteúdo dinâmico que trará
            algumas frases interessantes do Knowledge
    '''
    return render_to_response('home.html', {})

def system(request):
    '''
        System

        Página de entrada ou Login

        PLAN
            Identificar usuários que tenham o seu mesmo perfil e listá-los aqui
    '''
    loginUrl = users.create_login_url("/#aritial")
    return render_to_response('services.html', {'log':loginUrl})

def contato(request):
    '''
        Contato

        Página de contato com os criadores

        PLAN
            Adicionar aqui o contato de todas as pessoas e ferramentas
            utilizadas no desenvolvimento
    '''
    return render_to_response('contato.html', {})

def aritial(request):
    '''
        Aritial

        Página inicial do sistema e contâiner do AJAX de controle

        PLAN
            Integrar com serviços de imagem, upload com Drag'n Drop e fazer
            com que mais pessoas interajam nesta página
    '''
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
    '''
        Email

        Simples ferramenta de send mail

        PLAN
            Transformar num contâiner de chamados com contato e interação
            que coordena o perfil do usuário
    '''
    mail.send_mail(sender='octavio.turra@gmail.com',to="octavio.turra@gmail",subject=request.POST["nome"],body = "Enviado por: " + request.POST["email"] +" Mensagem:" + request.POST["corpo"])
    return HttpResponse("Obrigado pela sua mensagem!")
