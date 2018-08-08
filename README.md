# Jahim
Jahim ( Aplikasi Pemin**ja**man Antar **Him**punan )

Repositori ini berisi back-end dari aplikasi Jahim

<h1>Fitur :</h1>
<hr>
/recent : Akan mereturn data json dictionary yang berisi 5 barang terakhir yang dimasukkan ke dalam database. Dictionary berisi :<br>
    - Nama Barang
    - Jumlah yang tersedia
    - Harga pinjam
    - Nama himpunan yang menyediakan
<br><br>
/search : Menerima post data dictionary {'tipe' : tipe, 'cari' : cari}, lalu jika tipe adalah :<br>
    1. Username<br>
        Maka /search akan mereturn status code apakah nama himpunan yang dicari ada, jika ketemu akan mereturn juga id dari himpunan tersebut di database
    2. Barang<br>
        Maka /search akan mereturn status code apakah barang tersebut ada di database, jika ada maka akan direturn data json yang berisi nama barang, jumlah, harga, id database himpunan yang menyediakan
<br><br>
/login : Menerima post data dictionary {'username':username,'password':password}, lalu memvalidasi apakah username ada di database dan passwordnya benar, lalu mereturn status code sesuai hasil validasi
<br><br>
/register : Menerima post data dictionary {'username':username,'displayname':displayname,'password':password} lalu memvalidasi apakah username sudah ada di database/displayname sudah ada di database, jika keduanya belum ada maka akan ditambahkan ke database lalu di return status code sukses, jika gagal maka akan direturn status code gagal

# TODO :
<br>
  1. Implementasi /user/<id> untuk mencari data user dengan id bersangkutan
  2. Implementasi /barang/<id> untuk mencari barang dengan id bersangkutan
  3. Implementasi /registerBarang untuk mendaftarkan barang suatu himpunan
