1.
- JSON digunakan untuk mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet. Sedangkan XML memiliki data yang lebih terstruktur dan 
  pengguna dapat menggunakannya untuk menambahkan catatan.

- JSON menyimpan elemennya secara efisien akan tetapi tidak rapi untuk dilihat. Sedangkan XML menyimpan elemen-elemen nya dengan cara yang terstruktur,
  mudah dibaca oleh manusia dan mesin, akan tetapi kurang efisien.

- HTML (Hypertext Markup Language) adalah bahasa markup yang digunakan untuk membuat halaman website. Isinya terdiri dari berbagai kode yang dapat menyusun
  struktur suatu website. HTML terdiri dari kombinasi teks dan simbol yang disimpan dalam sebuah file. Dalam membuat file HTML, terdapat standar atau format
  khusus yang harus diikuti. Format tersebut telah tertuang dalam standar kode internasional atau ASCII (American Standard Code for Information Interchange).

2.
- karena user interaction dengan aplikasi itu sendiri membutuhkan data delivery. jika data delivery di bawah standar, maka user experience akan terdampak juga.

3.
- Membuat aplikasi baru dengan cara python manage.py startapp mywatchList
- membuat pathing pada /project_django/urls.py dan /mywatchList/urls.py
  - pada project_django = 'mywatchlist/'
  - pada mywatchList = '','html/','xml/','json/'
- mengisi mywatchList/models.py sesuai field data yang diinginkan
- mengisi mywatchList/views.py dengan meng-import class dari mywatchList/models.py
  - Membuat function show_watchlist dengan parameter request dan return sebagai html
  - Membuat function show_xml dengan parameter request dan return sebagai xml
  - Membuat function show_json dengan parameter request dan return sebagai json
- add, commit, dan push

