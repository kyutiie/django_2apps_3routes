
from django.shortcuts import render

def home(request):
    return render(request, 'flowerblog/home.html')

def about(request):
    return render(request, 'flowerblog/about.html')

def contact(request):
    return render(request, 'flowerblog/contact.html')
