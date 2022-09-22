## Tugas 3 PBP : Watchlist
Link web page : [Klik di sini](https://labdivany.herokuapp.com/mywatchlist/)<br>

### Perbedaan JSON, XML, dan HTML
- XML (eXtensible Markup Language) merupakan *Custom Markup Language* yang dapat dispesifikasi oleh industri yang menggunakannya dengan penggunaan semantik yang cukup *strict*. 
- JSON (JavaScript Object Notation) merupakan format pertukaran data dan hanya menyediakan spesifikasi Json pada dasarnya terikat dengan JavaScript, tetapi ternyata JSON sangat cocok untuk pertukaran data antar *Language*.
- HTML (HyperText Markup Language) merupakan Markup Language untuk dokumen dan didesain untuk ditampilkan di *web browser*.
![Table Perbandingan JSON, XML, dan HTML](/assets/image/TablePerbandinganXMLJSONHTML.jpg)
<br>
Referensi:
1. [A Deep Look at JSON vs. XML, Part 1: The History of Each Standard](https://www.toptal.com/web/json-vs-xml-part-1)
2. [A Deep Look At JSON vs. XML, Part 2: The Strengths and Weaknesses of Both](https://www.toptal.com/web/json-vs-xml-part-2)
3. [Slide 4: Data Delivery](https://scele.cs.ui.ac.id/pluginfile.php/161284/mod_resource/content/1/04%20-%20Data%20Delivery.pdf)

### Kenapa data delivery dibutuhkan?
Data delivery dibutuhkan untuk menampilkan request dari pengguna. Selain itu, data delivery juga diperlukan karena ada file yang tidak disimpan di server, tetapi dihasilkan atau baru dibentuk oleh kode program.

### Bagaimana saya mengimplementasikan Tugas 3
1. Membuat class di models.py untuk representasi database initial_watchlist_data.json
2. Membuat fungsi di views.py untuk menampilkan data dengan format yang diminta
3. Menambahkan path pada urls.py agar dapat diakses dengan path yang ditentukan
4. Mendeploy ke heroku

### Mengakses ketiga url di Postman
1. localhost:8000/mywatchlist/html
![Screenshoot Postman HTML](/assets/image/PostmanHTMLDivany.png)
2. localhost:8000/mywatchlist/json
![Screenshoot Postman JSON](/assets/image/PostmanJSONDivany.png)
3. localhost:8000/mywatchlist/json
![Screenshoot Postman XML](/assets/image/PostmanXMLDivany.png)