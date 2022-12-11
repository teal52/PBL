from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('entry/',views.entry,name='entry'),
    path('gpioon/',views.on,name='on'),
    path('gpiooff/',views.off,name='off'),
]