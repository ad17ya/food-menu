from django.shortcuts import render
from django.http import HttpResponse
from food.models import Item
from django.template import loader

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