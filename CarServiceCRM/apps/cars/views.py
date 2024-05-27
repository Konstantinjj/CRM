from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Car
from .forms import CarForm
from apps.clients.models import Client
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Car.objects.filter(
                Q(gos_num__icontains=query) |
                Q(client__first_name__icontains=query) |
                Q(client__last_name__icontains=query)
            ).order_by('-id')
        else:
            return Car.objects.all().order_by('-id')

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

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('car_list')

    def get_initial(self):
        initial = super().get_initial()
        client_id = self.kwargs.get('client_id')
        if client_id:
            client = get_object_or_404(Client, pk=client_id)
            initial['client'] = client
        return initial

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car_confirm_delete.html'
    success_url = reverse_lazy('car_list')
