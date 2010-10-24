#!/usr/bin/env python
#-*- coding:utf-8 -*-


import os

from google.appengine.ext import webapp

from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from google.appengine.ext import db

#conecta ao storage
#login de ana ou octo
#se houver mensagem retorna mensagem
#snao retorna "vazio"
#se houver hash inclui mensagem
#se incluir, atualiza valor

class DbMensageria(db.Model):
    author = db.StringProperty(multiline=False)
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class LoginPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'login.html')
        template_values = {}
        self.response.out.write(template.render(path, template_values))


class MainPage(webapp.RequestHandler):
    usuario=""
    def get(self):
        self.usuario = self.request.get("user")
        if  len(self.usuario)<3:
            self.redirect("/login")
        else:
            self.response.out.write("<meta charset='utf-8'/>")
            greeting = "Bem vindo(a)!!!"
            template_values = {
                'greetings': greeting,
                'usuario': self.usuario
            }

            path = os.path.join(os.path.dirname(__file__), 'index.html')
            self.response.out.write(template.render(path, template_values))

class Mensageria(webapp.RequestHandler):
    def get(self):
        dtb = DbMensageria()
        author = self.request.get("user")
        dtb.author = author
        dtb.content = self.request.get('inputText')
        dtb.put()
        self.redirect("/?user="+author)

class Receberia(webapp.RequestHandler):
    def get(self):
        self.response.out.write('<meta http-equiv="refresh" content="20" />')
        dtb = db.GqlQuery("SELECT * FROM DbMensageria\
         ORDER BY date DESC LIMIT 10")
        self.response.headers["Content-tpye"]="text/html"
        for greeting in dtb:
            author = greeting.author
            if greeting.author:
                self.response.out.write('<div style="border:1px solid #c00;\
                                        padding:5px;width:600px;margin:5px">\
                                        <b style="text-transform:capitalize">\
                                        %s</b> dizer:' %
                                        author)
                self.response.out.write('<blockquote>%s</blockquote></div>' %
                                      greeting.content )
            else:
                self.response.out.write('<div>Um anonimo diz:')
                self.response.out.write('<blockquote>%s</blockquote></div>' %
                                      greeting.content)

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                     ('/index',MainPage),
                                     ("/mensageria",Mensageria),
                                     ("/receberia",Receberia),
                                     ("/login",LoginPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
