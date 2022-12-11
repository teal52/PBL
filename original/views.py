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

from . import weather
from . import gpio


# Create your views here.

def index(request):
    weather_data = weather.get_json()

    return render(request,'original/base.html',weather_data)

def entry(request):
    
    return render(request,'original/setup.html')


def on(request):
    switch_state = True
    print(switch_state)
    gpio.switch(switch_state)
    return render(request, 'original/gpio.html',{'state': 'on'})

def off(request):
    switch_state = False
    print(switch_state)
    gpio.switch(switch_state)
    return render(request, 'original/gpio.html',{'state': 'off'})

