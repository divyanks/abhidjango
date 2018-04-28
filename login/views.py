from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.template import loader
from .form import loginForm
from .models import user

#from .forms import CommentForm

def index(request):
    #comments = Comment.objects.order_by('-date_added')
    form = loginForm()
    return render(request,"login/index.html" , {'form':form})

def loginpost(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user1, loggedIn = user.isLoggedIn(email, password)
            print(user1,loggedIn)
            if loggedIn:
                object_list = Datatable.objects.all() #or any kind of queryset
                json = serializers.serialize('json', object_list)
                return render(request,"login/home.html",user1)
            else:
                return render(request,"login/index.html" )
