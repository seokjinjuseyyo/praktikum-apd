import os
import time
from prettytable import PrettyTable
import pwinput

# cara bacanya {username: {"password": password, "role": role}}
pengguna = { #ini variabel global 1
    "gea": {
        "password": "pacar seokjin",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    }
}

# cara bacanya: {id: {"nama": nama, "kategori": kategori, "harga": harga, "stok": stok}}
produk = { #variabel global 2
    1: {"nama": "Whiskas 1kg", "kategori": "Makanan", "harga": 50000, "stok": 20},
    2: {"nama": "Royal Canin 2kg", "kategori": "Makanan", "harga": 150000, "stok": 15},
    3: {"nama": "Pasir Gumpal 5kg", "kategori": "Kebersihan", "harga": 45000, "stok": 30},
    4: {"nama": "Sisir Kucing", "kategori": "Grooming", "harga": 25000, "stok": 50},
    5: {"nama": "Mainan Bola", "kategori": "Mainan", "harga": 15000, "stok": 40}
}

keranjang = {} #variabel global 3

# 3 Variabel dibawah ini dipakai untuk ngecek user yang login 
user_login = "" #variabel global 4
role_login = "" #variabel global 5
status_login = False #variabel global 6

# Fungsi 1 yang pakai parameter
def validasi_input_angka(prompt, pesan_error="Input harus berupa angka!"):
    while True:
        try:
            input_str = input(prompt) #ini variabel lokal 
            hasil = int(input_str) #ini variabel lokal 
            return hasil
        except ValueError:
            print(f"\n{pesan_error}")
            time.sleep(4)
            return None


# Fungsi ke 2 yang pakai parameter juga
def hitung_total_keranjang_rekursif(list_items, index=0):
    if index >= len(list_items): #base case
        return 0
    
    
    item_sekarang = list_items[index]
    subtotal = item_sekarang["harga"] * item_sekarang["jumlah"]
    return subtotal + hitung_total_keranjang_rekursif(list_items, index + 1) #fungsi rekursif

# Fungsi 1 yang gaada parameternya
def tampilkan_header_utama():
    os.system('cls || clear')
    print("=" * 60)
    print("|      SELAMAT DATANG DI TOKO PERALATAN KUCING WINGKY      |")
    print("=" * 60)

# Fungsi ke 2 yang gaada parameternya
def generate_id_produk_baru():
    if len(produk) == 0:
        id_baru = 1
    else:
        id_baru = max(produk.keys()) + 1
    return id_baru

def tampilkan_daftar_produk(): #prosedur 1
    print("\n" + "=" * 59)
    print("|                   DAFTAR PRODUK WINGKY                  |")
    print("=" * 59)
    
    if len(produk) == 0:
        print("Tidak ada produk tersedia.")
    else:
        table = PrettyTable()
        table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
        table.align["ID"] = "c"
        table.align["Nama Produk"] = "l"
        table.align["Kategori"] = "l"
        table.align["Harga"] = "r"
        table.align["Stok"] = "c"
        
        for id_produk, data in produk.items(): #ini variabel lokal yang ada dalam loop
            table.add_row([
                id_produk,
                data['nama'],
                data['kategori'],
                f"Rp {data['harga']:,}",
                data['stok']
            ])
        
        print(table)
    
    print("=" * 59)

def tampilkan_isi_keranjang(): #prosedur ke 2
    print("=" * 59)
    print("|                   KERANJANG BELANJA                     |")
    print("=" * 59)
    
    if user_login not in keranjang or len(keranjang[user_login]) == 0:
        print("\nKeranjang belanja kosong.")
        print("=" * 59)
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama Produk", "Harga", "Jumlah", "Subtotal"]
        table.align["No"] = "c"
        table.align["Nama Produk"] = "l"
        table.align["Harga"] = "r"
        table.align["Jumlah"] = "c"
        table.align["Subtotal"] = "r"
        
        nomor = 1 #ini variabel lokal 
        list_items = [] #ini variabel lokal 
        
        for id_produk, item in keranjang[user_login].items(): #ini ada pakai variabel lokal 
            subtotal = item["harga"] * item["jumlah"] #ini ada pakai variabel lokal 
            list_items.append(item)
            table.add_row([
                nomor,
                item['nama'],
                f"Rp {item['harga']:,}",
                item['jumlah'],
                f"Rp {subtotal:,}"
            ])
            nomor += 1
        
        print(table)
        
        #fungsi rekursif untuk hitung total
        total = hitung_total_keranjang_rekursif(list_items) #ini ada pakai variabel lokal 
        
        print(f"{'TOTAL':>10} Rp {total:,}")
        print("=" * 59)

while True: #program utamanya
    tampilkan_header_utama() #ini pakai fungsi 1
    print("\n1. Login")
    print("2. Register")
    print("3. Keluar")
    
    pilihan_utama = input("\nPilih menu (1-3): ")
    
    # Menu login
    if pilihan_utama == "1":
        tampilkan_header_utama() # ini pakai fungsi 1
        print("\n-------------------- LOGIN SECTION -------------------------")

        try: # Error handling untuk bagian login
            username = input("Username: ") #ini variabel lokal 
            if not username:
                raise ValueError("Username tidak boleh kosong")
            
            password = pwinput.pwinput(prompt="Password: ", mask="*") #ini variabel lokal - menggunakan pwinput
            if not password:
                raise ValueError("Password tidak boleh kosong")
            
            # Verifikasi login dulu disini
            if username in pengguna and pengguna[username]["password"] == password:
                user_login = username
                role_login = pengguna[username]["role"]
                status_login = True
                print(f"\nLogin berhasil! Selamat datang, {user_login}")
                time.sleep(4)
                
                # Menu adminnya
                if role_login == "admin":
                    while status_login == True:
                        os.system('cls || clear')
                        print("=" * 50)
                        print(f"|            MENU ADMIN - Halo, {user_login}!             |")
                        print("=" * 50)
                        print("\n1. Lihat Semua Produk")
                        print("2. Tambah Produk")
                        print("3. Update Produk")
                        print("4. Hapus Produk")
                        print("5. Cari Produk")
                        print("6. Logout")
                        
                        pilihan_admin = input("\nPilih menu (1-6): ")
                        
                        # fitur lihat produk
                        if pilihan_admin == "1":
                            os.system('cls || clear')
                            tampilkan_daftar_produk() # ini pakai prosedur 1
                            time.sleep(10)
                        
                        # fitur tambah produk
                        elif pilihan_admin == "2":
                            os.system('cls || clear')
                            print("=" * 50)
                            print("|               TAMBAH PRODUK BARU               |")
                            print("=" * 50)
                            
                            try: # Error handling untuk bagian tambah produk
                                id_baru = generate_id_produk_baru() # ini pakai fungsi 2
                                
                                nama = input("\nNama Produk: ")
                                if not nama:
                                    raise ValueError("Nama produk tidak boleh kosong")
                                
                                kategori = input("Kategori (Makanan/Kebersihan/Grooming/Mainan): ")
                                if not kategori:
                                    raise ValueError("Kategori tidak boleh kosong")
                                
                                # fungsi buat validasi harus brupa angka
                                harga = validasi_input_angka("Harga: ", "Harga harus berupa angka!")
                                if harga is None or harga <= 0:
                                    raise ValueError("Harga harus lebih dari 0")
                                
                                stok = validasi_input_angka("Stok: ", "Stok harus berupa angka!")
                                if stok is None or stok < 0:
                                    raise ValueError("Stok tidak boleh negatif")
                                
                                produk[id_baru] = { #ini variabel lokal 
                                    "nama": nama, #ini variabel lokal 
                                    "kategori": kategori, #ini variabel lokal 
                                    "harga": harga, #ini variabel lokal 
                                    "stok": stok #ini variabel lokal 
                                }
                                print(f"\nProduk '{nama}' berhasil ditambahkan!")
                                time.sleep(4)
                                
                            except ValueError as e:
                                print(f"\nError: {e}")
                                time.sleep(4)
                        
                        # fitur update produknya
                        elif pilihan_admin == "3":
                            os.system('cls || clear')
                            print("=" * 50)
                            print("|                UPDATE PRODUK                   |")
                            print("=" * 50)
                            
                            # Menggunakan PrettyTable untuk menampilkan list produk
                            table = PrettyTable()
                            table.field_names = ["ID", "Nama Produk"]
                            table.align["ID"] = "c"
                            table.align["Nama Produk"] = "l"
                            
                            for id_produk, data in produk.items():
                                table.add_row([id_produk, data['nama']])
                            
                            print(table)
                            
                            try: # Error handling untuk bagian fitur update
                                id_update = validasi_input_angka("\nMasukkan ID produk yang ingin diupdate: ", "ID harus berupa angka!")#ini variabel lokal 
                                #line diatas ini pakai fungsi 1 dengan parameter
                                if id_update is None:
                                    raise ValueError("Input dibatalkan")
                                
                                if id_update not in produk:
                                    raise KeyError("Produk dengan ID tersebut tidak ditemukan!")
                                
                                print(f"\nProduk ditemukan: {produk[id_update]['nama']}")
                                print("\nPilih yang ingin diupdate:")
                                print("1. Nama")
                                print("2. Kategori")
                                print("3. Harga")
                                print("4. Stok")
                                pilih = input("Pilihan: ") #ini variabel lokal 
                                
                                if pilih == "1":
                                    nama_baru = input("Nama baru: ") #ini variabel lokal 
                                    if not nama_baru:
                                        raise ValueError("Nama tidak boleh kosong")
                                    produk[id_update]["nama"] = nama_baru
                                    print("\nNama produk berhasil diupdate!")
                                elif pilih == "2":
                                    kategori_baru = input("Kategori baru: ") #ini variabel lokal 
                                    if not kategori_baru:
                                        raise ValueError("Kategori tidak boleh kosong")
                                    produk[id_update]["kategori"] = kategori_baru
                                    print("\nKategori produk berhasil diupdate!")
                                elif pilih == "3":
                                    harga_baru = validasi_input_angka("Harga baru: ", "Harga harus berupa angka!") 
                                    #line diatas merupakan variabel lokal dan menggunakan fungsi 1 dengan parameter
                                    if harga_baru is None or harga_baru <= 0:
                                        raise ValueError("Harga harus lebih dari 0")
                                    produk[id_update]["harga"] = harga_baru
                                    print("\nHarga produk berhasil diupdate!")
                                elif pilih == "4":
                                    stok_baru = validasi_input_angka("Stok baru: ", "Stok harus berupa angka!")
                                    #line diatasmerupakan variabel lokal dan menggunakan fungsi 1 dengan parameter
                                    if stok_baru is None or stok_baru < 0:
                                        raise ValueError("Stok tidak boleh negatif")
                                    produk[id_update]["stok"] = stok_baru
                                    print("\nStok produk berhasil diupdate!")
                                    time.sleep(4)
                                else:
                                    print("\nPilihan tidak valid!")
                                time.sleep(4)
                                
                            except (ValueError, KeyError) as e:
                                print(f"\nError: {e}")
                                time.sleep(4)
                        
                        # fitur hapus produk
                        elif pilihan_admin == "4":
                            os.system('cls || clear')
                            print("=" * 50)
                            print("|                 HAPUS PRODUK                   |")
                            print("=" * 50)
                            
                            # Menggunakan PrettyTable untuk menampilkan list produk
                            table = PrettyTable()
                            table.field_names = ["ID", "Nama Produk"]
                            table.align["ID"] = "c"
                            table.align["Nama Produk"] = "l"
                            
                            for id_produk, data in produk.items():
                                table.add_row([id_produk, data['nama']])
                            
                            print(table)
                            
                            try: # Error handling untuk fitur hapus produk
                                id_hapus = validasi_input_angka("\nMasukkan ID produk yang ingin dihapus: ", "ID harus berupa angka!")
                                #line diatas ini menggunakan fungsi 1 dengan parameter
                                if id_hapus is None:
                                    raise ValueError("Input dibatalkan")
                                
                                if id_hapus not in produk:
                                    raise KeyError("Produk dengan ID tersebut tidak ditemukan!")
                                
                                konfirmasi = input(f"\nYakin ingin menghapus '{produk[id_hapus]['nama']}'? (y/n): ")
                                if konfirmasi.lower() == "y":
                                    del produk[id_hapus]
                                    print("\nProduk berhasil dihapus!")
                                else:
                                    print("\nPenghapusan dibatalkan.")
                                time.sleep(4)
                                
                            except (ValueError, KeyError) as e:
                                print(f"\nError: {e}")
                                time.sleep(4)
                        
                        # fitur buat mempermudah cari produk 
                        elif pilihan_admin == "5":
                            os.system('cls || clear')
                            print("=" * 59)
                            print("|                      CARI PRODUK                        |")
                            print("=" * 59)
                            keyword = input("\nMasukkan nama produk: ")
                            
                            print("\n" + "=" * 59)
                            print("|                     HASIL PENCARIAN                     |")
                            print("=" * 59)
                            
                            # Menggunakan PrettyTable untuk menampilkan hasil pencarian
                            table = PrettyTable()
                            table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
                            table.align["ID"] = "c"
                            table.align["Nama Produk"] = "l"
                            table.align["Kategori"] = "l"
                            table.align["Harga"] = "r"
                            table.align["Stok"] = "c"
                            
                            ketemu = False
                            for id_produk, data in produk.items():
                                if keyword.lower() in data['nama'].lower():
                                    table.add_row([
                                        id_produk,
                                        data['nama'],
                                        data['kategori'],
                                        f"Rp {data['harga']:,}",
                                        data['stok']
                                    ])
                                    ketemu = True
                            
                            if ketemu:
                                print(table)
                            else:
                                print("\nProduk tidak ditemukan.")
                            
                            print("=" * 59)
                            time.sleep(4)
                        
                        # fitur buat log out
                        elif pilihan_admin == "6":
                            print("\nLogout berhasil!")
                            time.sleep(4)
                            status_login = False
                        
                        else:
                            print("\nPilihan tidak valid!")
                            time.sleep(4)
                
                # menu pengguna
                else:
                    while status_login == True:
                        os.system('cls || clear')
                        print("=" * 50)
                        print(f"|           MENU PELANGGAN - Halo, {user_login}!          |")
                        print("=" * 50)
                        print("\n1. Lihat Semua Produk")
                        print("2. Cari Produk")
                        print("3. Tambah ke Keranjang")
                        print("4. Lihat Keranjang")
                        print("5. Hapus dari Keranjang")
                        print("6. Checkout")
                        print("7. Logout")
                        
                        pilihan_user = input("\nPilih menu (1-7): ")
                        
                        # fitur buat lihat produk
                        if pilihan_user == "1":
                            os.system('cls || clear')
                            tampilkan_daftar_produk() #ini pakai prosedur 1
                            time.sleep(7)

                        # fitur buat mempermudah cari produk
                        elif pilihan_user == "2":
                            os.system('cls || clear')
                            print("=" * 50)
                            print("|                  CARI PRODUK                   |")
                            print("=" * 50)
                            keyword = input("\nMasukkan nama produk: ")
                            
                            print("\n" + "=" * 59)
                            print("|                     HASIL PENCARIAN                     |")
                            print("=" * 59)
                            
                            # Menggunakan PrettyTable untuk menampilkan hasil pencarian
                            table = PrettyTable()
                            table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
                            table.align["ID"] = "c"
                            table.align["Nama Produk"] = "l"
                            table.align["Kategori"] = "l"
                            table.align["Harga"] = "r"
                            table.align["Stok"] = "c"
                            
                            ketemu = False
                            for id_produk, data in produk.items():
                                if keyword.lower() in data['nama'].lower():
                                    table.add_row([
                                        id_produk,
                                        data['nama'],
                                        data['kategori'],
                                        f"Rp {data['harga']:,}",
                                        data['stok']
                                    ])
                                    ketemu = True
                            
                            if ketemu:
                                print(table)
                            else:
                                print("\nProduk tidak ditemukan.")
                            
                            print("=" * 59)
                            time.sleep(5)

                        # fitur tambahkan produk ke keranjang
                        elif pilihan_user == "3":
                            os.system('cls || clear')
                            print("=" * 59)
                            print("|                  TAMBAH KE KERANJANG                    |")
                            print("=" * 59)
                            
                            # Menggunakan PrettyTable untuk menampilkan list produk
                            table = PrettyTable()
                            table.field_names = ["ID", "Nama Produk", "Kategori", "Harga", "Stok"]
                            table.align["ID"] = "c"
                            table.align["Nama Produk"] = "l"
                            table.align["Kategori"] = "l"
                            table.align["Harga"] = "r"
                            table.align["Stok"] = "c"
                            
                            for id_produk, data in produk.items():
                                table.add_row([
                                    id_produk,
                                    data['nama'],
                                    data['kategori'],
                                    f"Rp {data['harga']:,}",
                                    data['stok']
                                ])
                            
                            print(table)
                            
                            try:
                                id_beli = validasi_input_angka("\nMasukkan ID produk yang ingin dibeli: ", "ID harus berupa angka!")
                                if id_beli is None:
                                    raise ValueError("Input dibatalkan")
                                
                                if id_beli not in produk:
                                    raise KeyError("Produk dengan ID tersebut tidak ditemukan!")
                                
                                jumlah_beli = validasi_input_angka("Jumlah: ", "Jumlah harus berupa angka!")
                                if jumlah_beli is None or jumlah_beli <= 0:
                                    raise ValueError("Jumlah harus lebih dari 0")
                                
                                if jumlah_beli > produk[id_beli]["stok"]:
                                    raise ValueError(f"Stok tidak cukup! Stok tersedia: {produk[id_beli]['stok']}")
                                
                                # Inisialisasi keranjang user jika belum ada
                                if user_login not in keranjang:
                                    keranjang[user_login] = {}
                                
                                # Tambah ke keranjang
                                if id_beli in keranjang[user_login]:
                                    keranjang[user_login][id_beli]["jumlah"] += jumlah_beli
                                else:
                                    keranjang[user_login][id_beli] = {
                                        "nama": produk[id_beli]["nama"],
                                        "harga": produk[id_beli]["harga"],
                                        "jumlah": jumlah_beli
                                    }
                                
                                print(f"\n{produk[id_beli]['nama']} (x{jumlah_beli}) berhasil ditambahkan ke keranjang!")
                                time.sleep(4)
                                print("=" * 59)
                                
                            except (ValueError, KeyError) as e:
                                print(f"\nError: {e}")
                                print("=" * 59)
                                time.sleep(4)

                        # fitur lihat keranjang
                        elif pilihan_user == "4":
                            os.system('cls || clear')
                            tampilkan_isi_keranjang() #ini pakai prosedur 2
                            time.sleep(7)

                        # fitur hapus dari keranjang
                        elif pilihan_user == "5":
                            os.system('cls || clear')
                            print("=" * 38)
                            print("|         HAPUS DARI KERANJANG       |")
                            print("=" * 38)
                            
                            if user_login not in keranjang or len(keranjang[user_login]) == 0:
                                print("\nKeranjang belanja kosong.")
                                time.sleep(4)
                            else:
                                # Menggunakan PrettyTable untuk menampilkan isi keranjang
                                table = PrettyTable()
                                table.field_names = ["No", "ID", "Nama Produk", "Jumlah"]
                                table.align["No"] = "c"
                                table.align["ID"] = "c"
                                table.align["Nama Produk"] = "l"
                                table.align["Jumlah"] = "c"
                                
                                nomor = 1
                                id_list = []
                                for id_produk, item in keranjang[user_login].items():
                                    table.add_row([
                                        nomor,
                                        id_produk,
                                        item['nama'],
                                        item['jumlah']
                                    ])
                                    id_list.append(id_produk)
                                    nomor += 1
                                
                                print(table)
                                
                                try:
                                    id_hapus = validasi_input_angka("\nMasukkan ID produk yang ingin dihapus: ", "ID harus berupa angka!")
                                    if id_hapus is None:
                                        raise ValueError("Input dibatalkan")
                                    
                                    if id_hapus not in keranjang[user_login]:
                                        raise KeyError("Produk tidak ada di keranjang!")
                                    
                                    konfirmasi = input(f"\nYakin ingin menghapus '{keranjang[user_login][id_hapus]['nama']}' dari keranjang? (y/n): ")
                                    if konfirmasi.lower() == "y":
                                        del keranjang[user_login][id_hapus]
                                        print("\nProduk berhasil dihapus dari keranjang!")
                                    else:
                                        print("\nPenghapusan dibatalkan.")
                                    time.sleep(4)
                                    
                                except (ValueError, KeyError) as e:
                                    print(f"\nError: {e}")
                                    time.sleep(4)

                        # fitur checkout
                        elif pilihan_user == "6":
                            os.system('cls || clear')
                            print("=" * 59)
                            print("|                       CHECKOUT                          |")
                            print("=" * 59)
                            
                            if user_login not in keranjang or len(keranjang[user_login]) == 0:
                                print("\nKeranjang belanja kosong. Tidak ada yang bisa dicheckout.")
                                time.sleep(4)
                            else:
                                tampilkan_isi_keranjang()
                                
                                konfirmasi = input("\nLanjutkan checkout? (y/n): ")
                                if konfirmasi.lower() == "y":
                                    # Kurangi stok
                                    for id_produk, item in keranjang[user_login].items():
                                        produk[id_produk]["stok"] -= item["jumlah"]
                                    
                                    # Kosongkan keranjang
                                    keranjang[user_login] = {}
                                    
                                    print("\n" + "=" * 59)
                                    print("|       Checkout berhasil! Terima kasih telah berbelanja!      |")
                                    print("=" * 59)
                                    time.sleep(5)
                                else:
                                    print("\nCheckout dibatalkan.")
                                    time.sleep(4)

                        # fitur logout
                        elif pilihan_user == "7":
                            print("\nLogout berhasil!")
                            time.sleep(4)
                            status_login = False
                        
                        else:
                            print("\nPilihan tidak valid!")
                            time.sleep(4)
            else:
                print("\nUsername atau password salah!")
                time.sleep(4)
                
        except ValueError as e:
            print(f"\nError: {e}")
            time.sleep(4)
    
    # Menu Register
    elif pilihan_utama == "2":
        tampilkan_header_utama()
        print("\n-------------------- REGISTER SECTION ----------------------")
        
        try:
            username_baru = input("Username baru: ")
            if not username_baru:
                raise ValueError("Username tidak boleh kosong")
            
            if username_baru in pengguna:
                raise ValueError("Username sudah terdaftar!")
            
            password_baru = pwinput.pwinput(prompt="Silahkan input password baru: ", mask="*") # Menggunakan passwordnya
            if not password_baru:
                raise ValueError("Password tidak boleh kosong")
            
            pengguna[username_baru] = {
                "password": password_baru,
                "role": "user"
            }
            
            print(f"\nRegistrasi berhasil! Silakan login dengan username '{username_baru}'")
            time.sleep(4)
            
        except ValueError as e:
            print(f"\nError: {e}")
            time.sleep(4)
    
    # Menu Keluar
    elif pilihan_utama == "3":
        print("\nTerima kasih telah mengunjungi Toko Peralatan Kucing Wingky!")
        break
    
    else:
        print("\nPilihan tidak valid!")
        time.sleep(4)

