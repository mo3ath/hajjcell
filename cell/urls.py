from django.conf.urls import url
from django.views.generic import ListView, DetailView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('activate/', views.get_balance, name='get_balance'),
    url('get_balance/', views.get_balance, name='get_balance'),
    url('cells/',views.showCells,name='showCells'),
    url('newguide/',views.enterGuid,name='enterGuid'),
    url('recharge/',views.recharge,name='recharge'),
    url('guide/',views.guidsInfo,name='guidsInfo'),
    url('newcell/',views.enterCell,name='enterCell'),
    
]