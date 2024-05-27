from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import WorkType
from .forms import WorkTypeForm
from django.db.models import Q

class WorkTypeListView(ListView):
    model = WorkType
    template_name = 'worktypes/worktype_list.html'
    context_object_name = 'worktypes'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return WorkType.objects.filter(
                Q(name__icontains=query)
            ).order_by('-id')
        else:
            return WorkType.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class WorkTypeCreateView(CreateView):
    model = WorkType
    form_class = WorkTypeForm
    template_name = 'worktypes/worktype_form.html'
    success_url = reverse_lazy('worktype_list')

class WorkTypeUpdateView(UpdateView):
    model = WorkType
    form_class = WorkTypeForm
    template_name = 'worktypes/worktype_form.html'
    success_url = reverse_lazy('worktype_list')

class WorkTypeDeleteView(DeleteView):
    model = WorkType
    template_name = 'worktypes/worktype_confirm_delete.html'
    success_url = reverse_lazy('worktype_list')
