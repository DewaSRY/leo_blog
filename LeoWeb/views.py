from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import ContentModel,EmailModel,EmailModel
from .forms import EmailForms
# Create your views here.

class allArticle(ListView):
    template_name='allArticle/allArticle.html'
    model=ContentModel
    context_object_name='contents'
    
    
class SingelArticle(DetailView):
    template_name='allArticle/singleArticle.html'
    model=ContentModel
    context_object_name='content'
    
class getEmail(CreateView):
    template_name ='allArticle/get_email.html'
    model =EmailModel
    form_class =EmailForms
    # context_object_name='EmailForms'
    success_url ="success"

class success(TemplateView):
    template_name='allArticle/success.html'
