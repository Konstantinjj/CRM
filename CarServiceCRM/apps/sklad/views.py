from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Item, SortGroup
from .forms import ItemForm

class OverviewListView(ListView):
    model = Item
    template_name = 'sklad/overview.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('q')
        group_id = self.request.GET.get('group')

        if group_id and query:
            queryset = Item.objects.filter(sort_group__id=group_id, name__icontains=query).order_by('-id')
        elif group_id:
            queryset = Item.objects.filter(sort_group__id=group_id).order_by('-id')
        elif query:
            queryset = Item.objects.filter(name__icontains=query).order_by('-id')
        else:
            queryset = Item.objects.all().order_by('-id')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['sort_groups'] = SortGroup.objects.all()
        context['active_group_id'] = self.request.GET.get('group')
        return context

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'sklad/item_form.html'
    success_url = reverse_lazy('overview')

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'sklad/item_form.html'
    success_url = reverse_lazy('overview')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'sklad/item_confirm_delete.html'
    success_url = reverse_lazy('overview')
