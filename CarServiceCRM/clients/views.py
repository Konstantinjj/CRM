from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm

def client_list(request):
    clients = Client.objects.all()
    paginator = Paginator(clients, 2)  # Показывать 10 клиентов на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'clients/client_list.html', {'page_obj': page_obj})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'clients/client_form.html', {'form': form})

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/client_form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'clients/client_confirm_delete.html', {'client': client})

def client_cars(request, pk):
    client = get_object_or_404(Client, pk=pk)
    cars = client.cars.all()
    return render(request, 'clients/client_cars.html', {'client': client, 'cars': cars})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'clients/client_detail.html', {'client': client})
