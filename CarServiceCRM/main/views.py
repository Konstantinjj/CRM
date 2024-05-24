from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def clients(request):
    return render(request, 'main/clients.html')

def cars(request):
    return render(request, 'main/cars.html')