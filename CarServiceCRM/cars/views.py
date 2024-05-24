from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm
from clients.models import Client

def car_list(request):
    cars = Car.objects.select_related('client').all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form})

def car_create_for_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.client = client
            car.save()
            return redirect('client_cars', pk=client.pk)
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form, 'client': client})

def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_form.html', {'form': form})

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'cars/car_confirm_delete.html', {'car': car})
