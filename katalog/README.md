![Bagan Django Divany](/assets/image/BaganDjangoDivany.jpg)

Virtual Environment digunakan agar pengguna Python bisa menggunakan berbagai packages berbeda untuk berbagai project. Dengan adanya virtual environment, kita bisa membuat sebuah lingkup 'virtual' dan menginstall package yang diperlukan untuk project tertentu tanpa risiko merusak package-package lain di project yang lainnya. Dari hal tersebut, seharusnya tanpa virtual environment kita tetap bisa membuat web app berbasis Django. Akan tetapi, project-project lain yang kita miliki akan lebih baik kalau homogen karena jika sudah memerlukan package yg berbeda bisa saja merusak package yang sudah ada. Solusinya kembali lagi dengan menggunakan virtual environment untuk project yang berbeda tersebut :upside_down_face: :+1:

Implementasi yang saya lakukan adalah:
1. Saya membuat repositori baru untuk tugas 2 dan clone ke local
2. Saya mengaktifkan virtual environment dan menginstall package-package yang digunakan di lab pbp
3. Saya melakukan migrasi
4. Saya mengecek apakah class pada models.py sudah mencakup variabel-variabel yang ada di data (di file berformat .json)
5. Setelah memastikan hal tersebut, saya membuat fungsi untuk mengambil data dari models.py dan memberi context nama-nama variable untuk ditampilkan dengan sintaks django di html serta merendernya
6. Saya membuat routing untuk memetakan fungsi pada file urls.py agar ketika ada client request akan dipanggil fungsi tersebut. Routing yang saya buat adalah membuat sebuah URLPattern
7. Data yang didapat oleh fungsi di views.py kemudian ditampilkan di file .html dengan sintaks django sesuai dengan context yang dibuat.
8. Melakukan commit dan push ke github
9. Membuat aplikasi baru di Heroku dan menambahkan nama & API key pada secrets di repository github. 
10. Karena 'main' nya ada di project_django, memastikan ada routing ke page katalog pada urls.py di project django, dan ada installed apps untuk katalog di settings.py project_django