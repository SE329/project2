from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^options/', views.options, name='options'),
    url(r'^import/', views.importScreen, name='import'),
    url(r'^plan/', views.plan, name='plan')
]