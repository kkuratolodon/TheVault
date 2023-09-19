# Tugas 3 PBP 
Muhammad Irfan Firmansyah (2206816102) \
PBP-B \
![We Live We Love We Lie](https://cdn.discordapp.com/attachments/1049115719306051644/1151515266593857607/realistic-cat.gif) <br>

## 1. Apa perbedaan antara form POST dan form GET dalam Django?
- Form POST: Mengirimkan data secara langsung ke file lain tanpa menampilkan data tersebut pada URL. Biasanya, metode ini digunakan untuk mengirimkan data yang penting atau rahasia, seperti password. Dalam Django, form login dikembalikan menggunakan metode POST, di mana browser mengumpulkan data formulir, mengencodenya untuk transmisi, mengirimkannya ke server, dan kemudian menerima kembali responsnya.

- Form GET: Mengirimkan data dengan cara menampilkan data atau nilai pada URL. Data yang dikirimkan akan ditampung oleh action. Dalam konteks Django, metode GET mengumpulkan data yang dikirimkan menjadi sebuah string dan menggunakan ini untuk membuat URL.

## 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

- XML adalah bahasa markup yang menyediakan aturan untuk menentukan data apa pun. XML menggunakan tanda untuk membedakan antara atribut data dan data aktual. XML mendukung pertukaran informasi antara sistem komputer, seperti situs web, basis data, dan aplikasi pihak ketiga. XML juga memiliki kemampuan menampilkan data karena merupakan bahasa markup.

- JSON adalah format pertukaran data terbuka yang dapat dibaca baik oleh manusia maupun mesin. JSON bersifat independen dari setiap bahasa pemrograman dan merupakan output API umum dalam berbagai aplikasi. JSON lebih cepat untuk membaca dan menulis karena dapat diuraikan lebih mudah daripada XML. JSON juga lebih ringkas dan memiliki ukuran file yang lebih kecil, yang memungkinkan transmisi data yang lebih cepat.

- HTML adalah bahasa markup yang digunakan untuk menentukan struktur dan presentasi konten di web. HTML memiliki tanda standar yang harus digunakan semua orang. Anda tidak dapat membuat tanda Anda sendiri saat menulis HTML. HTML menitikberatkan pada bagaimana format tampilan dari data.

## 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- JSON memiliki ukuran file yang lebih kecil daripada XML, sehingga menghemat bandwidth dan waktu transmisi.
  
- JSON memiliki struktur kode yang lebih sederhana dan mudah dipahami oleh manusia, sehingga memudahkan development dan debugging.
  
- JSON memiliki kemampuan untuk menyimpan data dalam bentuk array dan nested objek, sehingga dapat menangani data yang kompleks dan dinamis.
  
- JSON dapat digunakan dengan berbagai bahasa pemrograman modern, seperti PHP, Python, Ruby, C++, Perl, dll.
  
- JSON dapat digunakan sebagai format data untuk komunikasi antara server dan aplikasi web atau sebagai format penyimpanan data sederhana.

## 4. Checklist Tugas
- [x] **Membuat input form untuk menambahkan objek model pada app sebelumnya.**
    1. Membuat file baru di dalam directori main bernama `forms.py`, seperti berikut:
        ```py
        from django.forms import ModelForm

        from main.models import Item

        class ItemForm(ModelForm):
            class Meta:
                model = Item
                fields = ["name", "artist", "amount", "rating", "description"]
        ```
    2. Membuka file `views.py`, kemudian menambahkan import
        ```
        from django.http import HttpResponseRedirect
        from main.forms import ItemForm
        from django.urls import reverse
        ```
        Kemudian membuat fungsi `create_item` dalam `views.py`
        ```py
        def create_item(request):
            form = ItemForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                form.save()
                return HttpResponseRedirect(reverse('main:show_main'))

            context = {'form': form}
            return render(request, "create_item.html", context)
        ```
        Kemudian menambahkan pasangan key-value items dalam dictionary `context`
        ``` py
        ...
        items = Item.objects.all() # 1
        context = {
            'items' : items, # 2
            'app_name' : 'The Vault',
            'name': 'Muhammad Irfan Firmansyah',
            'class': 'PBP-B'
        }
        ...

        ```
    3. Membuka `urls.py` pada direktori `main` dan import fungsi `create_item` tadi
        ```
        from main.views import show_main, create_product
        ```
        kemudian menambahkan *path url* ke dalam `urlpatterns` pada `urls.py`
        ```py
        path('create-product', create_product, name='create_product'),
        ```
    4. Membuat file HTML baru bernama `create_item.html` pada direktori `main/templates`
        ```html
        {% extends 'base.html' %} 

        {% block content %}
        <h1>Add New Product</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td>
                        <input type="submit" value="Add New Album"/>
                    </td>
                </tr>
            </table>
        </form>

        {% endblock %}
        ```
    5. Mengubah tampilan main.html, dengan menambahkan table dan button di bawah untuk menambahkan item
        ```html
        ...
        <table>
            <tr>
                <th style="border: 1px solid black; text-align: center;">&nbsp; Name &nbsp;</th>
                <th style="border: 1px solid black; text-align: center;">&nbsp; Artist &nbsp;</th>
                <th style="border: 1px solid black; text-align: center;">&nbsp; Rating &nbsp;</th>
                <th style="border: 1px solid black; text-align: center;">&nbsp; Description &nbsp;</th>
                <th style="border: 1px solid black; text-align: center;">&nbsp; Amount &nbsp;</th>
            </tr>
        
            {% for item in items %}
                <tr>
                    <td style="border: 1px solid black; text-align: center;"> &nbsp; {{item.name}} &nbsp; </td>
                    <td style="border: 1px solid black; text-align: center;"> &nbsp; {{item.artist}} &nbsp; </td>
                    <td style="border: 1px solid black; text-align: center;"> &nbsp; {{item.rating}}/10 &nbsp; </td>
                    <td style="border: 1px solid black; text-align: center;"> &nbsp; {{item.description}} &nbsp; </td>
                    <td style="border: 1px solid black; text-align: center;"> &nbsp; {{item.amount}} &nbsp; </td>
                    <td style="border: 1px solid black; text-align: center;">
                        <a href="{% url 'main:delete_item' item.id %}">
                            <button style="color: red; border: none; font-weight: bold;">
                                X
                            </button>
                        </a>
                    </td>
                </tr>
            {% endfor %}
        </table>
        ...
        <a href="{% url 'main:create_item' %}">
            <button style="font-weight: bold;">
                Add New Album
            </button>
        </a>
        ...

        ```
- [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID
    1. Membuka `views.py`, kemudian menambahkan import
    ```py
    from django.http import HttpResponse
    from django.core import serializers
    ```
    2. membuat 5 fungsi views yang diperlukan ke dalam `views.py`
    ```py
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
    ```
- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2
    1. Membuka `urls.py` pada direktori main, dan import 5 fungsi views yang sudah dibuat tadi.
    ```py
    from main.views import show_html, show_json, show_json_by_id, show_xml, show_xml_by_id
    ```
    2. Menambahkan menambahkan 5 *path url*nya ke dalam `urlpatterns` untuk mengakses 5 fungsi tadi.
    ```py
    ...
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    ...
    ```
## 5. Screenshot Postman
- **HTML**
![HTML](https://cdn.discordapp.com/attachments/1049115719306051644/1153651104266080258/image.png)
- **XML**
![XML](https://cdn.discordapp.com/attachments/1049115719306051644/1153651276308029440/image.png)
- **JSON**
![JSON](https://cdn.discordapp.com/attachments/1049115719306051644/1153651374794489896/image.png)
- **XML/ID**
![XML/ID](https://cdn.discordapp.com/attachments/1049115719306051644/1153651449939644517/image.png)
- **HTML**
![JSON/ID](https://cdn.discordapp.com/attachments/1049115719306051644/1153651513797902336/image.png)
# Tugas 2 PBP
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
    1. Melakukan add, commit, push dari repository lokal ke github
    2. Membuka https://Adaptable.io dan sign in menggunakan akun github
    3. Klik `App Dashboard` dan klik `+ NEW APP`
    4. Pilih `Connect an Existing Repository` dan pilih repository dari projek ini (TheVault)
    5. Pilih branch yang diinginkan (main)
    6. Pilih `Python App Template`
    7. Pilih PostgreSQL
    8. Pilih versi python yang sesuai di ven (3.11)
    9. Menggunakan start command `python manage.py migrate && gunicorn TheVault.wsgi`
    10. Pilih nama app (The-Vault) dan start deploy.

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan Django](https://media.discordapp.net/attachments/1054028087551078452/1151072455620829244/image.png?width=1310&height=372)
1. User : User adalah orang yang mengakses aplikasi web, misalnya dengan membuka situs web tersebut di browser.
2. URL Configuration (urls.py): Ketika user meminta halaman atau melakukan tindakan tertentu di situs web, permintaan mereka akan pertama-tama mencocokkan URL yang diminta dengan pola URL yang telah ditentukan di dalam berkas urls.py. Ini adalah cara Django tahu apa yang harus dilakukan dengan permintaan tersebut.
3. Views (Tampilan): Setelah URL cocok dengan pola yang ada di urls.py, permintaan akan diarahkan ke "tampilan" yang sesuai. Views adalah bagian dari aplikasi yang mengatur logika tampilan. Tampilan ini bisa mengambil data dari model (jika diperlukan) dan melakukan berbagai tugas lainnya.
4. Models (Model-data): Model adalah cara menggambarkan dan berinteraksi dengan data dalam aplikasi. Models mencakup struktur database dan cara mengambil atau menyimpan data. Tampilan (views) dapat berkomunikasi dengan model untuk mengelola data.
5. Database: Database adalah tempat di mana data dari aplikasi disimpan secara permanen. Tampilan (views) dapat mengakses dan memanipulasi data di dalam database menggunakan model-data yang telah didefinisikan.
6. Template: Setelah tampilan selesai memproses data atau logika bisnis, mereka akan menggunakan template HTML. Template ini berisi kode HTML yang akan digunakan untuk menghasilkan halaman web yang dilihat oleh pengguna. Data yang diperoleh dari tampilan akan dimasukkan ke dalam template ini.
7. Views (Kembali): Setelah template diisi dengan data, tampilan akan mengembalikan halaman HTML yang telah selesai dibuat kepada pengguna. Pengguna akan melihat halaman ini di peramban mereka sebagai respons atas permintaan awal.

Dengan kata lain, alur ini menjelaskan bagaimana permintaan dari pengguna dikendalikan oleh aplikasi web Django, melalui URL, tampilan, model, dan database, hingga akhirnya menghasilkan halaman web yang diberikan kepada pengguna sebagai respons.

## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
- Mengapa kita menggunakan virtual environment?
Virtual environment (venv) digunakan untuk mengisolasi proyek Python, memungkinkan manajemen dependensi yang terkendali, memfasilitasi pemeliharaan proyek, dan memastikan keseragaman lingkungan pengembangan tim. Dengan venv, kita dapat menghindari konflik dependensi antar-proyek, memisahkan lingkungan proyek dari Python global, dan menjaga proyek kita tetap bersih dan teratur. 
- Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Meskipun aplikasi Django dapat dibuat tanpa menggunakan virtual environment, sangat dianjurkan untuk memanfaatkannya dalam proses pengembangan aplikasi web berbasis Django. Hal ini akan memberikan manfaat dalam hal manajemen dependensi yang lebih efisien, pembatasan pengaruh proyek terhadap perubahan di instalasi Python global, serta menjaga keselamatan dan kerapihan proyek. Penggunaan virtual environment adalah praktik yang baik dalam pengembangan Python dan akan mendukung kelancaran serta ketertiban dalam pengembangan proyek Anda.
## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
1. MVC (Model-View-Controller):

- Model: Bertanggung jawab untuk mengelola data dan aturan bisnis.
- View: Bertanggung jawab untuk menampilkan data kepada pengguna.
- Controller: Bertanggung jawab untuk mengendalikan aliran aplikasi dan berfungsi sebagai penghubung antara Model dan View.
Perbedaan utama dengan Django adalah bahwa Django mengikuti pola MVT (Model-View-Template), yang menggunakan Template (T) untuk mengontrol tampilan, sedangkan dalam MVC, View berperan dalam mengontrol tampilan.

2. MVT (Model-View-Template):

- Model: Sama seperti dalam MVC, mengelola data dan aturan bisnis.
- View: Bertanggung jawab untuk menampilkan data kepada pengguna, mengontrol aliran aplikasi, dan berkomunikasi dengan Model.
- Template: Bertanggung jawab untuk merender tampilan dan mendefinisikan bagaimana data akan ditampilkan.
MVT adalah pola yang diterapkan secara khusus dalam Django, yang menggantikan "Controller" dengan "View" dan menambahkan komponen "Template" yang khusus untuk merender tampilan.

3. MVVM (Model-View-ViewModel):

- Model: Bertanggung jawab untuk mengelola data dan aturan bisnis, sama seperti dalam pola lainnya.
- View: Menampilkan data dan berinteraksi dengan pengguna, tetapi memiliki hubungan yang lebih erat dengan ViewModel.
- ViewModel: Bertanggung jawab untuk mengatur tampilan, berfungsi sebagai perantara antara Model dan View, dan mengelola logika tampilan.
MVVM adalah pola yang sering digunakan dalam pengembangan aplikasi berbasis framework JavaScript seperti Angular atau Vue.js. Ini memisahkan peran pengelolaan tampilan dari View, dengan ViewModel bertanggung jawab atas tugas ini.

Perbedaan utama di antara ketiga pola desain ini terletak pada cara mereka mengatur tanggung jawab dalam sebuah aplikasi. MVC lebih berfokus pada mengatur alur aplikasi, MVT menekankan pada presentasi data dengan menggunakan template, sedangkan MVVM memperkenalkan ViewModel untuk mempermudah pengikatan data dua arah. Keputusan yang tepat dalam memilih salah satu dari ketiganya bergantung pada jenis aplikasi yang tengah Anda kembangkan serta preferensi pribadi dalam pengembangan perangkat lunak.
