from django.shortcuts import render

def home(request):
    return render(request, 'Home.html')

def living(request):
    return render(request, 'Living.html')
    