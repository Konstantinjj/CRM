from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm

def client_list(request):
    clients = Client.objects.all().prefetch_related('cars')
    return render(request, 'clients/client_list.html', {'clients': clients})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'clients/client_form.html', {'form': form})
