# Tugas 5 PBP 
Muhammad Irfan Firmansyah (2206816102) <br>
PBP-B <br>

## 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
1. **Selektor Tag** <br>
   Selektor ini memilih elemen berdasarkan nama tag. Misalnya, `p { color: blue; }` akan memilih semua elemen `<p>` dan mengatur warna teksnya menjadi biru. Selektor tag sangat berguna jika ingin menerapkan style yang sama ke semua elemen dengan tag tertentu.

2. **Selektor Class** <br>
   Selektor ini memilih elemen berdasarkan nama class yang diberikan. Misalnya, `.pink { color: white; background: pink; padding: 5px; }` akan memilih semua elemen dengan class "pink" dan menerapkan style tersebut. Selektor class sangat berguna untuk menerapkan style yang sama ke sekelompok elemen yang memiliki class yang sama.

3. **Selektor ID** <br>
   Selektor ini hampir sama dengan class, tetapi ID bersifat unik dan hanya boleh digunakan oleh satu elemen saja. Misalnya, `#header { background: teal; color: white; height: 100px; padding: 50px; }` akan memilih elemen dengan ID "header" dan menerapkan style tersebut. Selektor ID sangat berguna untuk menerapkan style khusus ke satu elemen tertentu.

4. **Selektor Atribut**
   Selektor ini memilih elemen berdasarkan atribut. Misalnya, `input[type=text] { background: none; color: cyan; padding: 10px; border: 1px solid cyan; }` akan memilih semua elemen `<input>` yang memiliki atribut type='text' dan menerapkan gaya tersebut. Selektor atribut sangat berguna jika Anda ingin menerapkan style khusus ke elemen dengan atribut tertentu.

5. **Selektor Universal**
   Selektor ini digunakan untuk menyeleksi semua elemen pada jangkauan (scope) tertentu. Misalnya, `* { border: 1px solid grey; }` akan memberikan garis solid dengan ukuran 1px dan berwarna grey ke semua elemen. Selektor universal biasanya digunakan untuk mereset CSS.

## 2. Jelaskan HTML5 Tag yang kamu ketahui.
1. **`<html>`**: Tag ini mewakili akar (elemen tingkat atas) dari dokumen HTML, jadi juga disebut sebagai elemen root.
2. **`<head>`**: Tag ini berisi informasi yang dapat dibaca oleh mesin (metadata) tentang dokumen, seperti judul, skrip, dan lembar gaya.
3. **`<body>`**: Tag ini mewakili konten dari dokumen HTML.
4. **`<title>`**: Tag ini mendefinisikan judul dokumen yang ditampilkan di bilah judul browser atau tab halaman.
5. **`<h1>` sampai `<h6>`**: Tag ini digunakan untuk mendefinisikan heading.
6. **`<p>`**: Tag ini digunakan untuk mendefinisikan paragraf.
7. **`<a>`**: Tag ini digunakan untuk membuat hyperlink.
8. **`<img>`**: Tag ini digunakan untuk menyisipkan gambar.
9. **`<br>`**: Tag ini digunakan untuk memasukkan jeda baris.
10. **`<table>`, `<tr>`, `<td>`**: Tag ini digunakan untuk membuat tabel.

## 3. Jelaskan perbedaan antara margin dan padding.
1. **Margin**
   Margin adalah ruang di luar batas elemen. Margin tidak memiliki warna, dan sepenuhnya transparan. Margin digunakan untuk membuat ruang di antara elemen di halaman web. Misalnya, jika Anda ingin memiliki ruang 20px di antara dua elemen, Anda dapat menggunakan margin.

2. **Padding**
   Padding adalah ruang di antara konten elemen dan batas elemen tersebut. Padding bisa berwarna jika elemen tersebut memiliki background color. Padding digunakan untuk membuat ruang di dalam elemen. Misalnya, jika Anda ingin konten di dalam elemen memiliki ruang 20px dari batas elemen, Anda dapat menggunakan padding.

## 4.  Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
1. **Bootstrap**
   - Bootstrap adalah framework CSS yang paling banyak digunakan dan populer. 
   - Bootstrap menyediakan komponen yang telah dirancang sebelumnya, seperti navigasi, dropdown, progress bar, dll.
   - Bootstrap juga menyediakan sistem grid yang kuat dan responsif.
   - Bootstrap lebih cocok untuk proyek yang membutuhkan pengembangan cepat atau untuk mereka yang baru belajar tentang pengembangan web.

2. **Tailwind CSS**
   - Tailwind adalah framework CSS utility-first yang memberikan lebih banyak kontrol kepada pengembang.
   - Dengan Tailwind, Anda mendapatkan kelas utilitas dasar untuk membangun desain yang benar-benar kustom.
   - Tailwind tidak menyediakan komponen yang telah dirancang sebelumnya dan mengharuskan Anda untuk merancang dari awal.
   - Tailwind lebih cocok untuk proyek yang membutuhkan desain kustom atau untuk pengembang yang lebih berpengalaman.

## 5. Checklist tugas
- [x] Menambahkan Bootstrap ke aplikasi
Menambahkan tag meta... di `base.html`
```
<head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
</head>
```
CSS
```
<head>
    {% block meta %}
        ...
    {% endblock meta %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</head>
```
JS
```
<head>
    ...
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
</head>
```
Tambahan
```
<head>
    ...
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
</head>
```
- [x] designing
1. Membuat direktori static di main dan di dalamnya ditaruh file css dan file image yang dibutuhkan
2. Menghubungkan html dengan css tadi
3. Mengubah warna background, tampilan item, dll

# Tugas 4 PBP 
## 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah form yang digunakan untuk membuat pengguna baru yang dapat menggunakan aplikasi web. Formulir ini memiliki tiga bidang: username, password, dan konfirmasi password.
- Kelebihan dari Django UserCreationForm adalah:

  - Django UserCreationForm merupakan bagian dari sistem otentikasi pengguna bawaan Django, yang melakukan sebagian besar persyaratan proyek yang paling umum, menangani berbagai tugas, dan validasi kata sandi dan izin.
  - UserCreationForm memiliki fungsi save() yang memungkinkan kita untuk menyimpan instance Pengguna ke dalam database.

- Namun, Django UserCreationForm juga memiliki beberapa kekurangan:

  - Django secara umum dianggap sebagai perangkat lunak monolitik. Ini memungkinkan komunitas untuk mengembangkan ratusan modul dan aplikasi yang dapat digunakan kembali tetapi juga telah membatasi kecepatan pengembangan Django.
  - Django perlu mempertahankan kompatibilitas mundur, sehingga berevolusi dengan lambat.

## 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- Autentikasi adalah proses verifikasi identitas pengguna. Dalam konteks Django, autentikasi memverifikasi bahwa pengguna adalah siapa yang mereka klaim. Misalnya, ketika pengguna mencoba masuk, sistem akan memeriksa apakah kombinasi nama pengguna dan kata sandi yang diberikan cocok dengan apa yang ada di database.

- Otorisasi, di sisi lain, menentukan apa yang dapat dilakukan oleh pengguna yang telah terautentikasi. Ini berarti setelah pengguna berhasil masuk, sistem akan memeriksa apa yang diizinkan pengguna lakukan, seperti akses ke halaman tertentu atau melakukan tindakan tertentu.

Kedua konsep ini penting karena mereka membantu menjaga keamanan aplikasi Django. Autentikasi membantu mencegah akses yang tidak sah dengan memastikan hanya pengguna yang memiliki kredensial yang valid yang dapat masuk. Sementara itu, otorisasi membantu mencegah penyalahgunaan sistem dengan membatasi apa yang dapat dilakukan oleh setiap pengguna, bahkan setelah mereka masuk.

## 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookie adalah sejumlah kecil informasi yang dikirim oleh server web ke browser, dan kemudian dikirim kembali oleh browser pada permintaan halaman di masa mendatang. Cookie dapat digunakan untuk autentikasi, pelacakan user, dan mempertahankan preferensi user. 

Django, sebuah framework pengembangan web berbasis Python, juga menggunakan cookies untuk mengelola data sesi pengguna. Berikut adalah cara Django menggunakan cookies dalam konteks manajemen sesi pengguna:

- Membuat Cookie Sesi: Saat seorang pengguna masuk atau melakukan tindakan tertentu pada aplikasi web yang memerlukan data sesi, Django akan membuat cookie sesi. Cookie ini biasanya berisi ID sesi yang unik.

- Penyimpanan Data Sesi: Django memungkinkan Anda untuk menyimpan data sesi pengguna dalam cookie ini. Data sesi dapat berisi informasi seperti preferensi pengguna, keranjang belanja, atau status login. Data ini disimpan di sisi server, tetapi hanya ID sesi yang dikirimkan ke pengguna melalui cookie.

- Mengakses Data Sesi: Django menyediakan API untuk mengakses data sesi pengguna. Anda dapat mengambil data sesi berdasarkan ID sesi yang ditemukan dalam cookie pengguna.

- Keamanan: Django memastikan keamanan data sesi dengan mengenkripsi cookie dan menggunakan berbagai langkah keamanan, seperti menandai cookie dengan HttpOnly dan Secure untuk mencegah akses dari JavaScript dan melalui koneksi HTTP yang tidak aman.

- Kadaluwarsa: Anda dapat mengatur berapa lama cookie sesi akan bertahan sebelum kedaluwarsa. Setelah cookie sesi kedaluwarsa, data sesi tersebut akan dihapus.

## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web dapat menjadi aman, tetapi ada risiko potensial yang harus diwaspadai. Beberapa risiko dan pertimbangan terkait dengan penggunaan cookies dalam konteks keamanan adalah sebagai berikut:

- Keamanan Data: Cookies dapat digunakan untuk menyimpan data sensitif, seperti token otentikasi atau informasi pengguna. Jika tidak diimplementasikan dengan benar, cookie ini dapat menjadi target peretasan dan pencurian data. Oleh karena itu, sangat penting untuk mengenkripsi data sensitif dalam cookie.

- Cross-Site Scripting (XSS): Serangan XSS terjadi ketika penyerang menyisipkan skrip jahat ke dalam halaman web yang kemudian dijalankan di peramban pengguna. Jika cookies mengandung data sensitif dan tidak dijalankan dalam mode HttpOnly, penyerang dapat mencoba mencuri informasi ini melalui serangan XSS.

- Cross-Site Request Forgery (CSRF): Serangan CSRF terjadi ketika penyerang memaksa pengguna yang sudah diautentikasi untuk melakukan tindakan tertentu tanpa sepengetahuan mereka. Cookies yang digunakan dalam autentikasi dapat digunakan dalam serangan ini, oleh karena itu perlu melindungi aplikasi Anda dari serangan CSRF dengan menggunakan token anti-CSRF.

- Kebocoran Informasi: Cookies biasanya dikirimkan ke server bersama dengan setiap permintaan HTTP, termasuk permintaan ke sumber daya statis. Ini dapat menyebabkan kebocoran informasi jika cookie yang seharusnya hanya digunakan pada halaman tertentu terekspos pada sumber daya publik.

- Kadaluwarsa: Jika Anda tidak mengatur kadaluwarsa yang benar untuk cookies sesi, data sesi Anda dapat tetap ada dalam sistem pengguna bahkan setelah mereka seharusnya keluar. Ini dapat memungkinkan akses yang tidak sah ke sesi pengguna.

- Manajemen Cookie yang Tidak Aman: Manajemen cookie yang buruk, seperti penggunaan cookie non-HttpOnly untuk data sensitif, dapat meningkatkan risiko pencurian informasi.

## 5. Checklist Tugas
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
  1. Register <br>
    import beberapa fungsi yg dibutuhkan dan buat fungsi register di `views.py`
      ```py
      ...
      from django.shortcuts import redirect
      from django.contrib.auth.forms import UserCreationForm
      from django.contrib import messages
      ...
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
      ...
      ```
      membuat `register.html` di `main/templates`
      ```
      {% extends 'base.html' %}
      
      {% block meta %}
          <title>Register</title>
      {% endblock meta %}
      
      {% block content %}  
      
      <div class = "login">
          
          <h1>Register</h1>  
      
              <form method="POST" >  
                  {% csrf_token %}  
                  <table>  
                      {{ form.as_table }}  
                      <tr>  
                          <td></td>
                          <td><input type="submit" name="submit" value="Daftar"/></td>  
                      </tr>  
                  </table>  
              </form>
      
          {% if messages %}  
              <ul>   
                  {% for message in messages %}  
                      <li>{{ message }}</li>  
                      {% endfor %}  
              </ul>   
          {% endif %}
      
      </div>  
      
      {% endblock content %}
      ```    
      menambahkan path url tadi di `urls.py`
      ```
      path('register/', register, name='register'),
      ```
    2. Login <br>
       import fungsi yang diperlukan dan membuat fungsi login_user di `views.py`
       ```
       ...
       from django.contrib.auth import authenticate, login
       ...
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
       ...
       ```
        membuat `login.html` di `main/templates`.
        ```
        {% extends 'base.html' %}
        {% block meta %}
            <title>Login</title>
        {% endblock meta %}
        {% block content %}
        <div class = "login">
            <h1>Login</h1>
            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <tr>
                        <td>Username: </td>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>            
                    <tr>
                        <td>Password: </td>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login"></td>
                    </tr>
                </table>
            </form>
            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}     
            Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
        </div>
        {% endblock content %}
        ```
       Menambahkan path login tadi di `urls.py` di direktori main
    3. Logout <br>
    menambahkan import dan fungsi logout di `views.py` 
    ```
    ...
    from django.contrib.auth import logout
    ...
    def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
    ...
    ```   
    menambahkan button logout di `main.html` <br>
    kemudian, menambahkan path logout di `urls.py` di direkotri main
  
- [x] Menghubungkan model Item dengan User
    1. menambahkan import dan attribute user di models
    ```
    ...
    from django.contrib.auth.models import User
    ...
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ...
    ```
    2. menambahkan line di fungsi `create_item` di `views.py`
  ```
  ...
  def create_product(request):
     form = ProductForm(request.POST or None)
     if form.is_valid() and request.method == "POST":
         product = form.save(commit=False)
         product.user = request.user
         product.save()
         return HttpResponseRedirect(reverse('main:show_main'))
  ...
      
  ```
    3. migrate modelsnya
- [x] Menambahkan 2 user baru dan masing-masing punya 3 item
![user1](https://cdn.discordapp.com/attachments/1049115719306051644/1155821369163010120/image.png)
![user02](https://cdn.discordapp.com/attachments/1049115719306051644/1155821532992503808/image.png)
# Tugas 3 PBP

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
