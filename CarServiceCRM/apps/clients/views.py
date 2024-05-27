from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Client
from .forms import ClientForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ClientListView(ListView):
    model = Client
    template_name = 'clients/client_list.html'
    context_object_name = 'clients'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Client.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(middle_name__icontains=query) |
                Q(phone_number__icontains=query)
            ).order_by('-id')
        else:
            return Client.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

    def paginate_queryset(self, queryset, page_size):
        paginator = Paginator(queryset, page_size)
        page = self.request.GET.get('page')
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        return (paginator, page_obj, page_obj.object_list, page_obj.has_other_pages())

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients/client_form.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'clients/client_confirm_delete.html'
    success_url = reverse_lazy('client_list')

class ClientCarsView(ListView):
    model = Client
    template_name = 'clients/client_cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        client = get_object_or_404(Client, pk=self.kwargs['pk'])
        return client.cars.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = get_object_or_404(Client, pk=self.kwargs['pk'])
        return context

class ClientDetailView(ListView):
    model = Client
    template_name = 'clients/client_detail.html'
    context_object_name = 'client'

    def get_object(self):
        return get_object_or_404(Client, pk=self.kwargs['pk'])
