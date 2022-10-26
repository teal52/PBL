from dataclasses import dataclass
from pipes import Template
from re import template
from tkinter import font
from django.shortcuts import render
from django.http import HttpResponse

import datetime
import sys

# Create your views here.

def index(request):

    key_text={
        "name_text": "4E",
    }

    now = datetime.datetime.now()

    hour = f'{now.hour:02}'
    minute = f'{now.minute:02}'
    second = f'{now.second:02}'

    now_text={
        "hour":hour,
        "minute":minute,
        "second":second,
    }


    return render(request,'original/base.html',now_text)
