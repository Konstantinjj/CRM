from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm
from django.db.models import Q

def item_list(request):
    query = request.GET.get('q')
    if query:
        items = Item.objects.filter(Q(name__icontains=query)).order_by('-id')
    else:
        items = Item.objects.all().order_by('-id')
    return render(request, 'warehouse/item_list.html', {'items': items, 'query': query})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'warehouse/item_form.html', {'form': form})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'warehouse/item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'warehouse/item_confirm_delete.html', {'item': item})
