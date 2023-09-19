from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from main.forms import ItemForm

from .models import Item


# Create your views here.
def show_main(request):
    items = Item.objects.all()
    banyak_item = 0

    # Membuat harga item dipisahkan dengan titik tiap 3 digit
    for item in items:
        item.rating = f"{item.rating:.2f}"
        # menghitung banyak item
        banyak_item += 1

    context = {
        'items' : items,
        'app_name' : 'The Vault',
        'name': 'Muhammad Irfan Firmansyah',
        'class': 'PBP-B',
        'banyak_item': banyak_item
    }

    return render(request, "main.html", context)

# Method membuat item baru
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def delete_item(request, id):
    item = Item.objects.filter(pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_html(request):
    items = Item.objects.all().values()
    return HttpResponse(items)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")