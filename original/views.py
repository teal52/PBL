from pipes import Template
from re import template
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):

    key_text={
        "name_text": "4E",
    }

    return render(request,'original/index.html',key_text)
