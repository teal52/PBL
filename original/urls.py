from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('entry/',views.entry,name='entry'),
    path('on/',views.switch_on,name='on'),
    path('off/',views.switch_off,name='off'),
]