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

    now_text={
        "hour":now.hour,
        "minute":now.minute,
        "second":now.second,
    }


    return render(request,'original/index.html',now_text)
