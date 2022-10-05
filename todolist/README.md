# To-Do-List : [Tugas 4](#tugas-4-pbp) dan [Tugas 5](#tugas-5-pbp) PBP
Link web page : [Klik di sini](https://labdivany.herokuapp.com/todolist/)<br>

## Tugas 5 PBP

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

### Jelaskan tag HTML5 yang kamu ketahui.

### Jelaskan tipe-tipe CSS selector yang kamu ketahui.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

## Tugas 4 PBP

### Apa kegunaan {% csrf_token %} pada elemen <form>? 
{% csrf_token %} berfungsi sebagai tempat 'diletakannya' csrf token.<br>

### Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF adalah Cross Site Request Forgery. CSRF merupakan sebuah ancaman yang menyebabkan penggunan melakukan suatu aksi pada web yang sebenarnya tidak diniatkan. Django memiliki fitur bawaan yang dapat memproteksi dari ancaman tersebut. Nah, jika tidak ada potongan kode tersebut pada elemen form, ancaman CSRF tidak dapat dihindari.<br>

### Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa. Cara membuat form secara manual adalah dengan memasukkan elemen-elemen html form dan memberi label. Lalu layouting dengan mengatur position dan ukurannya.<br>

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Data submisi pengguna pada form dijadikan sebagai input untuk membuat instance dari class pada models karena models ini berperan untuk menghubungkan views dan database. Setelah itu, instance models tersebut disimpan ke database dengan method save(). Lalu, data-data tersebut ditampilkan melalui html dengan menggunakan django template variable pada html.<br>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat class Task pada models.py dengan atribut-atrbiut yang ditentukan
2. Membuat file .html untuk halaman utama (todolist), login, register, dan create-task (halaman menambah task baru)
3. Membuat form pada halaman yang memberikan input seperti login, register, dan create-task
4. Membuat fungsi login dan membuat halaman perlu diakses dengan login terlebih dahulu
5. Membuat fungsi untuk membuat task baru
6. Membuat HttpResponse berupa reverse antar login dan register
7. Membuat filter pada fungsi untuk menampilkan halaman utama berdasarkan usernya
8. Mendeploy ke heroku
