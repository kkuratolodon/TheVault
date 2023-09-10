# Tugas 2 PBP 
Muhammad Irfan Firmansyah (2206816102) \
PBP-B \
Link Deploy: [Link](https://thevault.adaptable.app/main)

## 1. Checklist Tugas
- [x] **Membuat sebuah proyek Django baru.**
    1. Membuat direktori baru dan menginisialisasi git dengan `git init`
    2. Membuat repositori di github dan menghubungkannya dengan repositori lokal dengan `git remote add origin [link]`
    3. Membuat virtual environment, dengan ```python -m venv env``` dan mengaktifkannya dengan  `env\Scripts\activate.bat`
    4. Menaruh dependencies di `requirements.txt` dan menginstallnya dengan `pip install -r requirements.txt`
    5. Membuat project django baru dengan `django-admin startproject TheVault .`
    6. Menambahkan host yang diizinkan di `settings.py` dengan cara mengisi list `ALLOWED_HOSTS` dengan host yang diizinkan (Untuk diawal isi dengan '*', untuk mengizinkan semua host).
    7. Membuat `.gitignore` yang berisikan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git.
    8. Menjalankan server Django dengan `python manage.py runserver` dan kemudian dibuka di `http://localhost:8000/` untuk mengetes apakah server django sudah berjalan dengan baik.
- [x] **Membuat aplikasi dengan nama main pada proyek tersebut.**
    1. Membuka direktori projek TheVault
    2. Membuka cmd di direktori tersebut dan mengaktifkan virtual environment `env\Scripts\activate.bat`
    3. Membuat aplikasi baru dengan nama 'main', menggunakan `python manage.py startapp main`
    4. Menambahkan `main` ke dalam variabel `INSTALLED_APPS` di `settings.py`
    ```
    INSTALLED_APPS = [
        ...,
        'main',
        ...
    ]
    ```
- [x] **Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**
    1. Membuka `urls.py` di direktori projek TheVault, dan mengimport
    ```
    from django.urls import path, include
    ```
    lalu menambahkan path pada variabel urlpatterns,
    ```
    urlpatterns = [
        ...
        path('main/', include('main.urls')),
        ...
    ]
    ```
- [x] **Membuat model pada aplikasi main.**
    1. Membuka `models.py` dan menambahkan attribute yang diinginkan
    ```
    from django.db import models
    from django.forms import ValidationError
    
    
    class Item(models.Model):
        name = models.CharField(max_length=255)
        amount = models.IntegerField()
        date_added = models.DateField(auto_now_add=True)
        price = models.IntegerField()
        description = models.TextField()
    ```
    2. Memigrasi model dengan cara
    ```
    python manage.py makemigrations
    ```
    kemudian, 
    ```
    python manage.py migrate
    ```
- [x] **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas.**
    1. Membuka `views.py` dan menambahkan pasangan key-value yang dibutuhkan dalam variabel context
    ```
    from django.shortcuts import render
    
    
    # Create your views here.
    def show_main(request):
        context = {
            'app_name' : 'The Vault',
            'name': 'Muhammad Irfan Firmansyah',
            'class': 'PBP B'
        }
    
        return render(request, "main.html", context)
    ```
    2. Membuat direktori templates di dalam direktori app main, dan membuat `main.html` di dalamnya, dengan isi sesuai keinginan
    ```
    <h1>{{ app_name }}</h1>
    
    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ```
- [x] **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
    1. Membuat `urls.py` di dalam direktori app main, kemudian diisi dengan
    ```
    from django.urls import path
    from main.views import show_main
    
    app_name = 'main'
    
    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    `show_main` adalah fungsi di `views.py` yang digunakan sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.
- [x] **Melakukan deployment ke Adaptable**
    1. Membuka https://Adaptable.io dan sign in menggunakan akun github
    2. Klik `App Dashboard` dan klik `+ NEW APP`
    3. Pilih `Connect an Existing Repository` dan pilih repository dari projek ini (TheVault)
    4. Pilih branch yang diinginkan (main)
    5. Pilih `Python App Template`
    6. Pilih PostgreSQL
    7. Pilih versi python yang sesuai di ven (3.11)
    8. Menggunakan start command `python manage.py migrate && gunicorn TheVault.wsgi`
    9. Pilih nama app (TheVault) dan start deploy.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
