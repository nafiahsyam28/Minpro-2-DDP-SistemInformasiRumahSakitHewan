import os
import time
from prettytable import PrettyTable
import pwinput


print("\n" + "="*45)
print("SISTEM INFORMASI ADMINISTRASI RUMAH SAKIT HEWAN")
print("="*45)

# data login
akun = {
        "admin": {
            "password": "etminketce",
            "role": "admin"
        },

        "staff": {
            "password": "staffkuat",
            "role": "staff"
        }
}


# daftar pasien hewan
daftar_pasien_hewan = [
            {
                "nama": "Naka",
                "jenis_hewan": "Kucing",
                "nama_pemilik": "Jihan",
                "penyakit": "Scabies",
            },
            {
                "nama": "Mambo",
                "jenis_hewan": "Anjing",
                "nama_pemilik": "Peter",
                "penyakit": "Heat Stroke",
            },
            {
                "nama": "Unul",
                "jenis_hewan": "Kucing",
                "nama_pemilik": "Nakhwa",
                "penyakit": "Cacingan",
            },
            {
                "nama": "Mr White",
                "jenis_hewan": "Kelinci",
                "nama_pemilik": "Adel",
                "penyakit": "Keracunan",
            },
            {
                "nama": "Elita",
                "jenis_hewan": "Hamster",
                "nama_pemilik": "Debora Lintang",
                "penyakit": "Pneumonia",
            },
    ]

# function jeda
def jeda():
    input("\nTekan Enter untuk kembali ke menu...")

# function login
def login():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        
        print("\n" + "="*30)
        print("   LOGIN SISTEM ADMINISTRASI")
        print("="*30)

        username = input("username : ")
        password = pwinput.pwinput("password : ")

        if username in akun:
            if akun[username]["password"] == password:
                role = akun[username]["role"]
                print("\nBERHASIL LOGIN")
                print("Role:", role)
                time.sleep(1)
                return role
        
            else:
                print("\nGAGAL LOGIN. Username atau password salah.")

        else:
            print("\nUSERNAME tidak terdaftar.")
            
        ulang = input("\nIngin mencoba lagi? (y/n): ")

        if ulang.lower() == "n":
            return None


# function tambah data 
def tambah_data():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" + "="*45)
    print("TAMBAH DATA PASIEN HEWAN")
    print("="*45)

    nama = input("Masukkan nama hewan : ")
    if nama == "":
        print("Nama hewan tidak boleh kosong.")
        jeda()
        return

    jenis = input("Masukkan jenis hewan : ")
    if jenis == "":
        print("Jenis hewan tidak boleh kosong.")
        jeda()
        return

    pemilik = input("Masukkan nama pemilik : ")
    if pemilik == "":
        print("Nama pemilik tidak boleh kosong.")
        jeda()
        return

    penyakit = input("Masukkan penyakit hewan : ")
    if penyakit == "":
        print("Penyakit hewan tidak boleh kosong")
        jeda()
        return

    pasien_baru = {
            "nama": nama,
            "jenis_hewan": jenis,
            "nama_pemilik": pemilik,
            "penyakit": penyakit
    }
    daftar_pasien_hewan.append(pasien_baru)
    print("\nDATA PASIEN HEWAN BERHASIL DITAMBAHKAN")

    jeda()

# function lihat data
def lihat_data():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" + "="*45)
    print("DATA PASIEN HEWAN")
    print("="*45)

    if len(daftar_pasien_hewan) == 0:
        print("BELUM ADA DATA PASIEN")

    else:
        tabel = PrettyTable()
        tabel.field_names = [
            "No",
            "Nama",
            "Jenis_hewan",
            "Nama_pemilik",
            "Penyakit",
        ]

        for i, pasien in enumerate(daftar_pasien_hewan, start=1):
            tabel.add_row([
            i,
            pasien["nama"],
            pasien["jenis_hewan"],
            pasien["nama_pemilik"],
            pasien["penyakit"]
        ])

        print(tabel)

    jeda()

# function ubah data
def ubah_data():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" + "="*45)
    print("UBAH DATA PASIEN HEWAN")

    if len(daftar_pasien_hewan) == 0:
        print("BELUM ADA DATA YANG BISA DIUBAH")
        jeda()
        return
    tabel = PrettyTable()
    tabel.field_names = [
        "No",
        "Nama",
        "Jenis_hewan",
        "Nama_pemilik",
        "Penyakit"
    ]

    for i, pasien in enumerate(daftar_pasien_hewan, start=1):
        tabel.add_row([
            i,
            pasien["nama"],
            pasien["jenis_hewan"],
            pasien["nama_pemilik"],
            pasien["penyakit"]
        ])

    print(tabel)

    try:
        nomor = int(input("\nPILIH NOMOR PASIEN YANG INGIN DIUBAH: "))
        if 1 <= nomor <= len(daftar_pasien_hewan):
            index = nomor - 1
            print("\nMasukkan data baru.")
            Nama_baru = input("Nama hewan baru: ")
            Jenis_baru = input("Jenis hewan baru: ")
            Pemilik_baru = input("Nama pemilik baru: ")
            Penyakit_baru = input("Penyakit baru: ")
            
            if Nama_baru == "":
                print("Nama hewan tidak boleh kosong.")

            elif Jenis_baru == "":
                print("Jenis hewan tidak boleh kosong.")

            elif Pemilik_baru == "":
                print("Nama pemilik tidak boleh kosong.")

            elif Penyakit_baru == "":
                print("Penyakit tidak boleh kosong.")

            else:
                daftar_pasien_hewan[index] = {
                    "nama": Nama_baru,
                    "jenis_hewan": Jenis_baru,
                    "nama_pemilik": Pemilik_baru,
                    "penyakit": Penyakit_baru
                }

                print("\nDATA PASIEN BERHASIL DIUBAH")

        else:
            print("\nNomor pasien tidak ditemukan.")

    except ValueError:
        print("\nInput harus berupa angka.")

    jeda()

# function hapus data
def hapus_data():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n" + "="*45)
    print("HAPUS DATA PASIEN HEWAN")
    print("="*45)

    if len(daftar_pasien_hewan) == 0:
        print("BELUM ADA DATA YANG BISA DIHAPUS.")
        jeda()
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "No",
        "Nama",
        "Jenis_hewan",
        "Nama_pemilik",
        "Penyakit"
    ]

    for i, pasien in enumerate(daftar_pasien_hewan, start=1):
        tabel.add_row([
            i,
            pasien["nama"],
            pasien["jenis_hewan"],
            pasien["nama_pemilik"],
            pasien["penyakit"]
        ])

    print(tabel)

    try:
        nomor = int(input("\nPILIH NOMOR PASIEN YANG INGIN DIHAPUS: "))
        if 1 <= nomor <= len(daftar_pasien_hewan):
            pasien_dihapus = daftar_pasien_hewan.pop(nomor - 1)
            print(
                "\nDATA PASIEN",
                pasien_dihapus["nama"],
                "BERHASIL DIHAPUS."
            )
        else:
            print("\nNomor pasien tidak terdaftar.")

    except ValueError:
        print("\nInput harus berbentuk angka")

    jeda()

# function menu admin
def menu_admin():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "="*45)
        print("DAFTAR PILIHAN INFORMASI REGISTRASI")
        print("="*45)
        print("1. Menambah data pasien hewan")
        print("2. Melihat data pasien hewan")
        print("3. Mengubah data pasien hewan")
        print("4. Menghapus data pasien hewan")
        print("5. Keluar")
        print("="*45)

        pilihan = input("Pilihlah menu (1-5): ")

        if pilihan == "1":
            tambah_data()

        elif pilihan == "2":
            lihat_data()

        elif pilihan == "3":
            ubah_data()

        elif pilihan == "4":
            hapus_data()
        
        elif pilihan == "5":
            print("\nKELUAR DARI MENU ADMIN")
            time.sleep(1)
            break

        else:
            print("\nPILIHAN TIDAK TERSEDIA.")
            jeda()

# function menu staff
def menu_staff():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "="*45)
        print("DAFTAR MENU STAFF SISTEM INFORMASI REGISTRASI")
        print("="*45)
        print("1. Menambah data pasien hewan")
        print("2. Melihat data pasien hewan")
        print("3. Keluar")
        print("="*45)

        pilihan = input ("Pilihlah menu (1-3): ")

        if pilihan == "1":
            tambah_data()

        elif pilihan == "2":
            lihat_data()

        elif pilihan == "3":
            print("\nSELESAI. KELUAR DARI MENU STAFF")
            time.sleep(1)
            break

        else:
            print("\nPILIHAN TIDAK TERSEDIA.")
            jeda()


# program utama
while True:
    role = login()
    if role == "admin":
        menu_admin()

    elif role == "staff":
        menu_staff()

    else:
        print("\nPROGRAM SELESAI. TERIMA KASIH")
        break