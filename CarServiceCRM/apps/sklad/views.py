from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Item, SortGroup
from .forms import ItemForm


class OverviewListView(ListView):
    model = Item
    template_name = 'sklad/overview.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        group_id = self.request.GET.get('group')

        if not group_id:
            first_group = SortGroup.objects.first()
            if first_group:
                group_id = first_group.id

        if query:
            return Item.objects.filter(name__icontains=query).order_by('-id')
        elif group_id:
            try:
                group_id = int(group_id)
                return Item.objects.filter(sort_group__id=group_id).order_by('-id')
            except ValueError:
                return Item.objects.none()
        else:
            return Item.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['sort_groups'] = SortGroup.objects.all()
        context['active_group_id'] = self.request.GET.get('group')
        if not context['active_group_id'] and not context['query']:
            first_group = SortGroup.objects.first()
            if first_group:
                context['active_group_id'] = first_group.id
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
