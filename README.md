Faris Bayhaqi
2106653110
PBP A
Tugas 2

Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django
Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

Deskripsi Tugas
Pada tugas ini, kamu akan mengimplementasikan konsep Model-View-Template serta beberapa hal yang sudah kamu pelajari selama tutorial lab. Kamu dapat menyelesaikan tugas ini dengan memanfaatkan source code tugas lab berikut. Adapun pada tugas lab 1 ini kamu diminta untuk:

1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
5. Membuat sebuah README.md yang berisi link menuju aplikasi Heroku yang sudah kamu deploy serta jawaban dari beberapa pertanyaan berikut:
   - Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py,
     models.py, dan berkas html;
     ->![Untitled Diagram drawio (3)](https://user-images.githubusercontent.com/94624202/190207366-f071378a-13ac-45cc-be84-64bb9d29d5b8.png)
       URL       : Mengarahkan permintaan HTTP ke tampilan yang sesuai berdasarkan URL perminataan
       View      : Menerima permintaan HTTP dan mengembalikan respon HTTP. view mengakses data yang diperlukan untuk memenuhi request melalu model, dan mendelegasikan
                   formating sebagai tanggung jawab dari template
       Models    : Struktur data aplikasi, dan menyediakan mekanisme untuk mengelola dan meminta records dalam database
       Templates : Struktur / layout sebuah file dengan placeholder yang digunakan utk mewakili konten yang sebenarnya

   - Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
     -> Virtual enviroment adalah sebuah tempat yang digunakan untuk menjalankan suatu project dengan suatu lingkungan yang terisolasi,sehingga dependency/requirements
        suatu project dapat dilakukan tanpa mengganggu enviroment asli, walaupun tanpa menggunakan virtual enviroment kita tetap bisa membuat aplikasi web berbasis
        Django, dikarenakan requirements yang diperlukan bisa diinstall di luat virtual enviroment.
     
   - Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
     -> Pertama, saya mulai mengerjakan dari models.py karena pada poin 1 saya harus dapat melakukan pengambilan data dari model. Saya mengisi data yang ada pada
        template kedalam models.py. Selanjutnya saya mengerjakan views.py dimana saya harus membuat fungsi untuk melakukan pengambilan data dari model, saya lakukan
        itu dengan meng-import class yang saya buat pada models.py dan membuat fungsi sesuai dengan yang diminta. Selanjutnya saya meng-import fungsi pada views.py
        ke dalam urls.py dan setelah itu saya menentukan path untuk fungsi yang saya buat pada views.py. Selanjutnya saya langsung mengerjakan bagian struktur web /
        bagian template dari web saya, dengan cara membuat katalog.html dan mengisi file tersebut sesuai data yang sudah ada di views.py. Terakhir saya melakukan
        deployment ke Heroku dengan memasukan API  dan nama app heroku saya ke secret repositori github saya, setelah itu saya langsung melakukan deployment pada 
        bagian actions>deploy pada github, dan hasilnya dapat diliah di https://pbp-tugas2-farisbayhaqi.herokuapp.com
   
Perhatikan bahwa kamu harus mengerjakan tugas ini menggunakan repositori berbeda dengan tutorial.

Deadline Pengerjaan
Tugas ini memiliki tenggat waktu pengumpulan pada tanggal 15 September 2022 pada pukul 12.00. Harap mengumpulkan link repositori yang kamu gunakan ke dalam slot submisi yang telah disediakan di SCELE.

Bonus
Kamu akan mendapatkan nilai bonus pada penilaian tugas ini apabila kamu berhasil mengimplementasikan dan mendemonstrasikan testing dasar (contoh: unit testing, functional testing, dan lain-lain). Silakan cari di Google untuk melihat cara membuat testing di Django.
