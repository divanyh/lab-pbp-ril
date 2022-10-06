# To-Do-List : [Tugas 4](#tugas-4-pbp) dan [Tugas 5](#tugas-5-pbp) PBP
Link web page : [Klik di sini](https://labdivany.herokuapp.com/todolist/)<br>

## Tugas 5 PBP

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
- Inline CSS:
*Styling* dilakukan langsung di tiap tag html yang ingin di-*styling*. Kelebihannya adalah developer dapat melihat dan mengubah styling tiap-tiap komponen secara langsung pada komponennya, tidak perlu mengingat class/id dan mencarinya di css. Kekurangannya adalah sangat mungkin terjadi redundansi pada code. Misal, ada tipe komponen yang sama tetapi berada di section yang berbeda. Selain itu, tentu tidak dapat diplikasikan antar file html. <br>
- Internal CSS:
*Styling* dilakukan secara kolektif di head html. Kelebihannya adalah code lebih rapi dan meminimumkan redundansi code pada komponen-komponennya. Kekurangannya adalah redundansi tetap mungkin terjadi di antar file html. <br>
- Eksternal CSS:
*Styling* dilakukan di suatu file terpisah (.css). Kelebihannya adalah file html lebih clean dan dapat digunakan antar file html. Kekurangannya adalah setiap pengubahan untuk suatu komponen perlu mengingat class/id dan mencarinya di file tersebut. <br>

### Jelaskan tag HTML5 yang kamu ketahui.
- a: untuk memberikan hyperlink pada komponen
- head: section untuk menyimpan informasi-informasi terkait dokumen termasuk title dan styling
- body: section yang merupakan badan/isi dari dokumen, biasanya di section ini lah komponen-komponen yang akan ditampilkan terletak.
- div: tag yang mendefinisikan suatu bagian/*section* baru
- h*: (* = 1-6) tag untuk membuat heading, semakin besar angka semakin kecil
- html: tag yang mendefinisikan page html itu sendiri
- img: tag untuk menambahkan gambar
- input: tag untuk menambahkan komponen yang berfungsi untuk menerima input dari pengguna
- label: tag untuk memberikan keterangan pada komponen dengan tag input
- meta: tag untuk menyediakan metadata yang terstruktur terkait dokumen
- nav: tag yang mendefinisikan *section* yang berfungsi sebagai navigasi.
- p: tag untuk menampung tulisan (paragraph)
- li: tag untuk mendefinisikan list
- ul: tag untuk mendefinisikan unordered list
- strong: tag untuk mengubah tulisan menjadi bold
- i: tag untuk mengubah tulisan menjadi italic
- u: tag untuk mengubah tulisan menjadi underlined
- title: tag untuk menambahkan title pada dokumen<br>

### Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- '*': CSS selector yang berguna untuk memilih semua elemen
- '': CSS selector yang berguna untuk memilih elemen dengan tag tersebut
- '.': CSS selector yang berguna untuk memilih elemen dengan class tertentu
- '#': CSS selector yang berguna untuk memilih elemen berdasarkan idnya 
Semakin ke bawah semakin spesifik. Jika dilakukan styling berbeda pada sebuah elemen yang memiliki id dan containernya dengan class tertentu untuk sebuah elemen maka yang akan diterapkan kepada elemen tersebut adalah yg dengan CSS selector '#' terhadap idnya.<br>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat section head pada setiap page html dan menambahkan link bootstrap untuk menjadi stylesheet
2. Memberikan class dan style pada setiap komponen dan section secara inline
3. Membuat semua elemen menjadi responsif

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
