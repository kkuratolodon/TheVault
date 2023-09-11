from django.shortcuts import render

from .models import Item


# Create your views here.
def show_main(request):
    items = Item.objects.all()
    context = {
        'items' : items,
        'app_name' : 'The Vault',
        'name': 'Muhammad Irfan Firmansyah',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)