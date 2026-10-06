# Minpro-2-DDP-SistemInformasiRumahSakitHewan

Nama : Jihanun Syam Nafi'ah <br>
Kelas : A <br>
NIM : 2609116017


# Penjelasan Program
Sistem Informasi Administrasi Rumah Sakit Hewan adalah program yang digunakan untuk membantu mengelola data pasien hewan. Program ini dikembangkan dari Mini Project 1 dengan menambahkan sistem login menggunakan username dan password serta hak akses berdasarkan role pengguna.
Program memiliki dua role, yaitu Admin dan Staff. <br>

Admin mempunyai hak akses CRUD yang meliputi :
1. menambah data pasien hewan, 
2. melihat data pasien hewan, 
3. mengubah data pasien hewan,
4. menghapus data pasien. <br>

Sedangkan, staff memiliki akses untuk :
1. menambah data pasien hewan,
2. melihat data pasien hewan. <br>

Data pasien meliputi nama hewan, jenis hewan, nama pemilik, dan penyakit. Program memakai Dictionary dan Function, validasi input menggunakan conditional statement, dan juga beberapa library seperti os, time, PrettyTable, dan pwinput. Program ini juga menerapkan error handling untuk menangani kesalahan input agar program tidak langsung berhenti ketika pengguna memasukkan input yang tidak tepat.

# Flowchart dan Penjelasan Alur
<img width="1574" height="1806" alt="MinPro2 drawio" src="https://github.com/user-attachments/assets/32956d5e-10e2-4a69-b337-a0b716afd770" /> 


1. Flowchart mulai dari simbol mulai, kemudian menuju proses memasukkan username dan password. Setelah input, alur masuk ke simbol decision “username & password benar?”. Jika Tidak, alur akan ke proses menampilkan pesan “Username atau password salah”, lalu garis balik ke bagian input username dan password untuk mencoba login kembali. Jika jawabannya Ya, alur akan meneruskan ke pengecekan role pengguna.
2. Melakukan pengecekan role, setelah login berhasil, alur menuju decision “role = admin?”. Pada bagian ini flowchart bercabang menjadi dua. Apabila jawabannya Ya, maka akan ke menu admin. Jika jawabannya Tidak, akan ke menu staff.
3. Dari menu admin, alur kemudian diteruskan ke input pilihan 1–5. Setelah pengguna memasukkan pilihan, alur melewati beberapa simbol decision, yaitu “pilihan 1?”, “pilihan 2?”, “pilihan 3?”, “pilihan 4?”, dan “pilihan 5?”. Apabila salah satu keputusan bernilalai Ya, alur masuk ke proses yang sesuai. Jika semuanya bernilai Tidak sampai pilihan 5, maka akan menampilkan pesan “Pilihan tidak tersedia” dan akan kembali ke input pilihan melalui konektor.
4. Dan menu staff, alur lanjut ke konektor B kemudian ke input pilihan 1–3. Alurnya menggunakan keputusan “pilihan 1?”, “pilihan 2?”, dan “pilihan 3?”. Jika pengguna memilih pilihan 1, alur akan menuju proses tambah data. Apabila memilih pilihan 2, alur menuju proses lihat data. Dan jika memilih pilihan 3, alur menuju proses keluar. Jika tidak memilih ketiganya, akan menampilkan pesan “Pilihan tidak tersedia” dan alur kembali ke input pilihan.
5. Apabila pilihan tambah data dipilih, alur lanjut dengan memasukkan data pasien, yaitu nama, jenis hewan, nama pemilik, dan penyakit. Setelah seluruh data dimasukkan, sistem menampilkan pesan bahwa data berhasil ditambahkan. 
6. dan ketika pilihan lihat data dipilih, alur menuju proses menampilkan tabel data pasien. Kemudian terdapat decision “Data kosong?”. Jika Ya, menampilkan pesan “Belum ada data”. Jika Tidak, akan menampilkan data pasien. Setelah proses selesai, alur kembali ke menu
7. Pada pilihan ubah data, meminta nomor pasien yang ingin diubah. Kemudian ada desicion “Nomor tersedia?”. Jika jawabannya Tidak, akan menampilkan pesan “Nomor tidak tersedia” dan alur kembali ke proses untukmemasukkan nomor pasien. Jika jawabannya Ya, admin memasukkan data baru pasien, lalu sistem menampilkan pesan bahwa data berhasil diubah. Setelah itu, alur kembali ke menu admin.
8. Di pilihan hapus data, alur meminta nomor pasien yang ingin dihapus. dan kemudian memeriksa apakah nomor tersebut tersedia. Jika jawabannya Tidak, sistem menampilkan pesan “Nomor tidak tersedia” dan kembali ke memasukkan nomor pasien. Jika jawabannya Ya, data pasien dihapus dan sistem menampilkan pesan bahwa data berhasil dihapus. Setelah itu, alur kembali ke menu admin.
9. Terakhir pada saat pengguna memilih Keluar, alur meninggalkan menu yang sedang digunakan dan menuju proses Keluar. Setelah itu, alur dilanjutkan mke Selesai, sehingga program berakhir.


# Dokumentasi Program & Output
<img width="310" height="78" alt="Screenshot 2026-10-06 203640" src="https://github.com/user-attachments/assets/46daae5e-f055-4740-8830-1702fa941a5e" />

Pada tahap pertama, pengguna diminta untuk memasukkan username dan password agar bisa mengakses sistem. Kemudiamn program akan memeriksa data login apakah sudah benar dan menentukan role pengguna berdasarkan akun yang mau digunakan. Disini saya akan login sebagai Admin.


<img width="308" height="98" alt="Screenshot 2026-10-06 204007" src="https://github.com/user-attachments/assets/4943e5c0-1cf7-4128-9365-ebd447d9e353" />

Setelah username dan password yang dimasukkan sesuai, ini adalah hasil output sistem yang menampilkan pesan bahwa login berhasil serta menampilkan role pengguna. Pengguna kemudian diarahkan ke menu sesuai dengan role yang dimiliki. Disini akan diarahkan ke menu admin karena di awal saya memilih role admin


Lalu ini tampilan menu admin yang dimana terdapat lima pilihan, yaitu 
  1. menambah data pasien,
  2. melihat data pasien,
  3. mengubah data pasien,
  4. menghapus data pasien, dan
  5. keluar.

Admin memiliki akses CRUD lengkap di data pasien hewan, berbeda dengan Staff


<img width="308" height="116" alt="Screenshot 2026-10-06 204533" src="https://github.com/user-attachments/assets/203862b1-fed9-40dc-8dcc-6b1239caa94e" />

Ini adalah output ketika kita memilih pilihan 1 yaitu menambah data pasien, disini akan diminta untuk memasukkan nama hewan, jenis hewan, nama pemilik dan penyakit. Jika sesuai maka program akan menampilkan Data berhasil ditambahkan


<img width="302" height="140" alt="Screenshot 2026-10-06 204844" src="https://github.com/user-attachments/assets/776da625-004e-42d6-977b-b56bf7f46b54" />

Pada menu Lihat Data kali ini, menampilkan data pasien hewan yang telah disimpan dalam bentuk tabel. Tampilan tabel dibuat dengan library PrettyTable sehingga data lebih terstruktur, rapi, enak diliat dan mudah dibaca.


<img width="284" height="222" alt="Screenshot 2026-10-06 205116" src="https://github.com/user-attachments/assets/5b239b87-6390-4b1f-a90b-5a2cd39a9cd5" />

Di pilihan ke 3 yaitu mengubah data pasien hewan, disini sistem meminta admin untuk memilih nomor pasien mana yang ingin diubah. pada output ini admin memilih pasien nomor 1. Jika tersedia maka program langsung akan meminta admin untuk memasukkan nama hewan baru, jenis hewan baru, nama pemilik baru, dan penyakit baru. Jika sudah program akan menampilkan bahwa DATA PASIEN BERHASIL DIUBAH.


<img width="350" height="173" alt="Screenshot 2026-10-06 205609" src="https://github.com/user-attachments/assets/9a8d1311-11fb-4230-81e3-a8538ff10bd8" />

Selanjutnya pilihan ke 4 yaitu hapus data, dipakai oleh admin untuk menghapus data pasien. Di sini porgram meminta admin untuk memilih nomor data yang ingin dihapus lalu admin memilih nomor 4 sebgai pasien yang ingin dihapus, kemudian sistem menghapus data tersebut dari daftar pasien dan  menampilkan pesan bahwa Data berhasil dihapus.


<img width="301" height="73" alt="Screenshot 2026-10-06 205900" src="https://github.com/user-attachments/assets/9203ec32-789d-49da-878b-a17e3c84a25e" />

Disini program memakai validasi input menggunakan conditional statement untuk mengecek data yang dimasukkan apakah sesuai dengan program. Di output ini admin memasukkan data kosong, maka yang terjai adalah sistem akan menampilkan pesan Nama hewan tidak boleh kosong.


<img width="314" height="153" alt="Screenshot 2026-10-06 210158" src="https://github.com/user-attachments/assets/998e15a6-e9da-499c-aca3-133ebcce308e" />


Lalu ini program menggunakan error handling untuk menangani kesalahan input yang seharusnya berupa angka tapi malah huruf. Dengan adanya error handling, input yang salah tidak menyebabkan program langsung berhenti, tetapi sistem menampilkan pesan kesalahan kepada admin yaitu Input harus berupa angka.


<img width="296" height="123" alt="Screenshot 2026-10-06 210426" src="https://github.com/user-attachments/assets/ce6cd0f7-fcd1-4922-9f3e-d59f0897018c" />

Dan ini output ketika admin memilih menu 5 yaitu keluar. DSan program menampilkan KELUAR DARI MENU ADMIN lalu kembali ke halaman login.



<img width="281" height="91" alt="Screenshot 2026-10-06 210903" src="https://github.com/user-attachments/assets/31ece6da-4495-4c8d-a308-03f126b28a36" />

Disini pengguna mencoba login lagi apabila username dan password tepat maka akan menampilkan BERHASIL LOGIN. Kali ini pengguna akan login sebagai staff yang dimana hanya mempunyai 3 akses saja yaitu :
   1. menambah data pasien hewan
   2. melihat data pasien hewan
   3. Keluar


<img width="302" height="86" alt="Screenshot 2026-10-06 211714" src="https://github.com/user-attachments/assets/3cd3150c-6014-4aab-ac8f-c80f03208a79" />

Ini tampilan menu pilihan jika lgoin sebagai staff yg dimana hanya mempunyai 3 akses, berbeda dengan admin.
