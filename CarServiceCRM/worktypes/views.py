from django.shortcuts import render, get_object_or_404, redirect
from .models import WorkType
from .forms import WorkTypeForm
from django.db.models import Q

def worktype_list(request):
    query = request.GET.get('q')
    if query:
        worktypes = WorkType.objects.filter(Q(name__icontains=query)).order_by('-id')
    else:
        worktypes = WorkType.objects.all().order_by('-id')
    return render(request, 'worktypes/worktype_list.html', {'worktypes': worktypes, 'query': query})

def worktype_create(request):
    if request.method == 'POST':
        form = WorkTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worktype_list')
    else:
        form = WorkTypeForm()
    return render(request, 'worktypes/worktype_form.html', {'form': form})

def worktype_edit(request, pk):
    worktype = get_object_or_404(WorkType, pk=pk)
    if request.method == 'POST':
        form = WorkTypeForm(request.POST, instance=worktype)
        if form.is_valid():
            form.save()
            return redirect('worktype_list')
    else:
        form = WorkTypeForm(instance=worktype)
    return render(request, 'worktypes/worktype_form.html', {'form': form})

def worktype_delete(request, pk):
    worktype = get_object_or_404(WorkType, pk=pk)
    if request.method == 'POST':
        worktype.delete()
        return redirect('worktype_list')
    return render(request, 'worktypes/worktype_confirm_delete.html', {'worktype': worktype})
