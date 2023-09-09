from django.shortcuts import render


# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'The Vault',
        'name': 'Muhammad Irfan Firmansyah',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)