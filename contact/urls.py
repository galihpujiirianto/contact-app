from django.urls import path
app_name = 'contact'

from . import views

urlpatterns = [
    path('', views.index, name='index')
]