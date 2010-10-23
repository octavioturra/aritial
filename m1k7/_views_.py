#-*- coding:utf-8 -*-

# Create your views here.

#from django.template import Context, loader
from django.shortcuts import render_to_response, get_list_or_404
from django.http import HttpResponseRedirect
from django import forms
from models import Page

class ContactForm(forms.Form):
    '''
        Campos do formulário
    '''
    title = forms.CharField(max_length=25)
    name = forms.CharField()

def main(request):
  #visitor = Visitor()
  #visitor.ip = request.META["REMOTE_ADDR"]
  #visitor.put()
    #pages = ['Início', 'Perfil', 'Serviços', 'Contato']
    pages = Page.all()
    return render_to_response('main.html', {'pages':pages})

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render_to_response('main.html', {
        'form': form,'paco':'Erro, formulario mal colocado'
    })
  #visitors = Visitor.all()
  #visitors.order("-added_on")

  #for visitor in visitors.fetch(limit=40):
      #result += visitor.ip + u" visited on " + unicode(visitor.added_on) + u""

  #return HttpResponse(result)
