from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def login_page(request):
    return render(request, 'login.html', {})

def register_page(request):
    return render(request ,'signup.html', {})

