from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Item
from .forms import ItemForm
from django.db.models import Q

class ItemListView(ListView):
    model = Item
    template_name = 'warehouse/item_list.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Item.objects.filter(
                Q(name__icontains=query)
            ).order_by('-id')
        else:
            return Item.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'warehouse/item_form.html'
    success_url = reverse_lazy('item_list')

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'warehouse/item_form.html'
    success_url = reverse_lazy('item_list')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'warehouse/item_confirm_delete.html'
    success_url = reverse_lazy('item_list')
