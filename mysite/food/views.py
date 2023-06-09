from django.shortcuts import render, redirect
from django.http import HttpResponse
from food.models import Item
from django.template import loader
from food.forms import ItemForm

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list' : item_list,
    }
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse('<h1>This is an item<h1>')

def detail(request, item_id):
    item_detail = Item.objects.get(pk=item_id)
    context = {
        'item' : item_detail,
    }

    return render(request, 'food/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form})

def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete-confirm.html', {'item': item})