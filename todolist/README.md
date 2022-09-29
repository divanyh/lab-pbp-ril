### Apa kegunaan {% csrf_token %} pada elemen <form>? 
{% csrf_token %} berfungsi sebagai tempat 'diletakannya' csrf token.

### Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF adalah Cross Site Request Forgery. CSRF merupakan sebuah ancaman yang menyebabkan penggunan melakukan suatu aksi pada web yang sebenarnya tidak diniatkan. Django memiliki fitur bawaan yang dapat memproteksi dari ancaman tersebut. Nah, jika tidak ada potongan kode tersebut pada elemen form, ancaman CSRF tidak dapat dihindari.

### Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa. Cara membuat form secara manual adalah dengan memasukkan elemen-elemen html form dan memberi label. Lalu layouting dengan mengatur position dan ukurannya.

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
