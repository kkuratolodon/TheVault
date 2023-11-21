import datetime
import json
import os

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.forms import ValidationError
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseNotFound, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from main.forms import ItemForm
from main.models import Item
from TheVault import settings


@login_required(login_url='/login')
def show_main(request):
    if 'last_login' not in request.COOKIES:
        return login_user(request)

    items = Item.objects.filter(user=request.user).order_by('name')
    banyak_item = 0

    # Loop setiap item
    for item in items:
        # membuat rating dibuletin 2 angka di blkg koma
        item.rating = f"{item.rating:.2f}"
        # menghitung banyak item
        banyak_item += 1
    
    context = {
        'items' : items,
        'app_name' : 'The Vault',
        'name': 'Muhammad Irfan Firmansyah',
        'class': 'PBP-B',
        'username': request.user.username,
        'banyak_item': banyak_item,
        'last_login': request.COOKIES['last_login'][:-7],
    }

    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# Method membuat item baru
def create_item(request):
    form = ItemForm(request.POST or None, request.FILES)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form, 'username': request.user.username, 'last_login': request.COOKIES['last_login'][:-7],}
    return render(request, "create_item.html", context)

def del_item(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def inc_item(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        item.amount += 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def dec_item(request, id):
    if request.method == "POST":
        item= Item.objects.get(pk=id)
        if item.amount > 0:
            item.amount -= 1
            item.save()
        if item.amount == 0:
            item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def show_html(request):
    items = Item.objects.filter(user=request.user).values()
    return HttpResponse(items)

@login_required(login_url='/login')
def show_xml(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

@login_required(login_url='/login')
def show_json(request):
    data = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_product_json(request):
    items = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items))

@csrf_exempt
def add_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        artist = request.POST.get("artist")
        amount = request.POST.get("amount")
        rating = request.POST.get("rating")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        user = request.user

        if image is None:
            image = os.path.join(settings.MEDIA_ROOT, 'default_album.png')
        
        new_product = Item(name=name, artist=artist, amount=amount, rating=rating, description=description, image=image, user=user)
        try:
            new_product.full_clean()
            new_product.save()
            return HttpResponse(b"CREATED", status=201)
        except ValidationError as e:
            return HttpResponseBadRequest(json.dumps(e.message_dict))

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            image = data["image"],
            rating = int(data["rating"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)