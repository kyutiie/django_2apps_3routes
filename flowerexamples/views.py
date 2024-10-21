
from django.shortcuts import render

def flowerallpink(request):
    return render(request, 'flowerexamples/flowerallpink.html')

def flowerrose(request):
    return render(request, 'flowerexamples/flowerrose.html')

def flowertulips(request):
    return render(request, 'flowerexamples/flowertulips.html')
