# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import  UserCreationForm
from django.conf import settings
from django.urls import reverse_lazy





User = get_user_model()

class IndexView(TemplateView):


        template_name = 'index.html'

index = IndexView.as_view()



def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_email()
        success = True
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)





