from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.index, name='index'),
    path('loginpost/', views.loginpost, name='loginpost'),
    #path('sign/', views.sign, name='sign')
]
