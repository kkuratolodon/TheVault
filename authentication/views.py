from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from main.models import *

logged_user = None

@csrf_exempt
def register(request):
    
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')

    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "status": False,
            "message": "Username sudah terdaftar."
        }, status=400)

    if password1 != password2:
        return JsonResponse({
            "status": False,
            "message": "Password dan Konfirmasi Password anda berbeda!."
        }, status=400)
    
    user = User.objects.create_user(username=username, password=password1)
    user.save()

    return JsonResponse({
        "username": user.username,
        "status": True,
        "message": "Registrasi berhasil!"
    }, status=201)

@csrf_exempt
def login(request):
    global logged_user
    username = request.POST['username']
    password = request.POST['password']
    print(username, password)
    user = authenticate(username=username, password=password)
    logged_user = user
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Username atau Password anda salah."
        }, status=401)
    
@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        logged_user = None
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    
def show_json(request):
    data = Item.objects.filter(user = logged_user)
    return HttpResponse(serializers.serialize('json', data))