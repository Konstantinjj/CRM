from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Item, SortGroup

class OverviewListView(ListView):
    model = Item
    template_name = 'sklad/overview.html'
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Item.objects.filter(name__icontains=query).order_by('-id')
        else:
            return Item.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['sort_groups'] = SortGroup.objects.all()
        context['active_group_id'] = self.request.GET.get('group')
        return context
