# To-Do-List : [Tugas 6](#tugas-6-pbp) PBP
Link web page : [Klik di sini](https://labdivany.herokuapp.com/todolist/)<br>

## Tugas 6 PBP

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Asynchronous programming adalah pendekatan programming yang lebih fleksibel dibandingkan synchronous programming. Hal ini disebabkan oleh asynchronous programming tidak terikat oleh hirarki urutan perintah. Oleh karenanya, asynchronous programming dapat menerima banyak perintah dalam satu waktu secara simultan dan independen (tiap-tiap perintahnya). Berikut adalah beberapa kelebihan dan kekurangannya:
    - Kelebihan:
        1. Memberikan user experience yang lebih baik karena membuat program lebih responsive dan mengurangi waktu menunggu untuk program load ulang
        2. Programmer bisa membuat kustomisasi pesan error
        3. Programmer bisa menyederhanakan program yang seharusnya synchronous dengan metode *promise-based callback*
    - Kekurangan:
        1. Untuk menyusun fungsi-fungsi asynchronous, programmer harus mempunyai pengetahuan yang mendalam mengenai pemanggilan dan rekursif karena fungsi asynchronous umumnya lebih kompleks
        2. Latency pada program mungkin lebih tinggi karena banyaknya asynchronous request dapat membuat server overload yang menyebabkan program melambat
        3. Tidak terlalu banyak bahasa pemrograman yang compatible dengan skema asynchronous <br>
- Synchronous programming merupakan pendekatan programming yang menggunakan operasi blocking I/O yang artinya setiap operasi harus dijalankan sebelum yang setelahnya dieksekusi (harus berurutan). Berikut adalah beberapa kelebihan dan kekurangannya:
    - Kelebihan:
        1. Simple, menulis program synchronous lebih mudah dibandingkan program asynchronous
        2. Lebih mudah dicari oleh *search engine* karena lebih mudah baginya untuk menemukan web yang menggunakan arsitektur synchronous
    - Kekurangan:
        1. Waktu loadnya lebih lambat
        2. Membutuhkan lebih banyak resource karena membutuhkan lebih banyak threads <br>

### Jelaskan maksud dari paradigma Event-Driven Programming dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah pendekatan programming yang tujuan penulisan code nya adalah untuk merespon event. Event ini umumnya merupakan suatu aksi dari eksternal program. Event dapat dipicu maupun tidak oleh user. Misal, event yang dipicu oleh user adalah ketika user klik suatu tombol maka akan muncul gambar. Sedangkan event yang tidak dipicu user biasanya terdapat pada sistem otomatis seperti layar ponsel yang menaikkan kecerahannya ketika pengguna sedang berada di luar ruang. <br>

Salah satu penerapannya pada tugas ini adalah ketika user klik tombol bergambar tempat sampah, task terhapus. <br>

### Jelaskan penerapan asynchronous programming pada AJAX.
AJAX membuat web app (dan browser) melakukan perkerjaan mengirim dan menampilkan data dari server di balik layar. Dengan AJAX, untuk melakukan parsing tidak perlu merefresh halaman dan 'mengganggu' tampilan dan behaviour dari halaman setiap data dimanipulasi. AJAX memisahkan bagian penampilan dan pertukaran data sehingga halaman web/aplikasi dapat mengubah database secara dinamis tanpa perlu mereload seluruh halaman.<br>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat fungsi baru pada views.py untuk menampilkan data dalam format json
2. Membuat url baru untuk fungsi tersebut
3. Membuat fungsi pada JS untuk parsing dari url
4. Menampilkan hasil parsing dengan menggunakan innerHTML
5. Membuat Modal untuk menampilkan form untuk menambahkan task baru
6. Membuat fungsi pada views.py untuk mengambil data dari form pada modal dan menjadikannya sebuah objek task baru 
7. Membuat fungsi pada JS untuk mengambil data baru tersebut dan seakan-akan menambahkannya ke dalam list task
