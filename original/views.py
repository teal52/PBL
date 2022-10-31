from dataclasses import dataclass
from pipes import Template
from pkgutil import ImpImporter
from re import template
from tkinter import font
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

import datetime
import sys

from . import timer


# Create your views here.

def index(request):
    print(timer.get_timer())
    return render(request,'original/base.html')

def entry():
    return render(request,'original/base.html')

