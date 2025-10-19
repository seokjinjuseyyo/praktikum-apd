import os
import time

# Database penggunanya diganti jadi pakai dictionary sebelumnya kan pakai nested list
# cara bacanya {username: {"password": password, "role": role}}
pengguna = {
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
produk = {
    1: {"nama": "Whiskas 1kg", "kategori": "Makanan", "harga": 50000, "stok": 20},
    2: {"nama": "Royal Canin 2kg", "kategori": "Makanan", "harga": 150000, "stok": 15},
    3: {"nama": "Pasir Gumpal 5kg", "kategori": "Kebersihan", "harga": 45000, "stok": 30},
    4: {"nama": "Sisir Kucing", "kategori": "Grooming", "harga": 25000, "stok": 50},
    5: {"nama": "Mainan Bola", "kategori": "Mainan", "harga": 15000, "stok": 40}
}


# cara bacanya: {username: {id_produk: {"nama": nama, "harga": harga, "jumlah": jumlah}}}
keranjang = {}

# Variabel untuk ngecek user yang login
user_login = ""
role_login = ""
status_login = False

# ini program utamanya nda ada yang diubah cuma diubah bagian list kemarin jadi dictionary aja
while True:
    os.system('cls || clear')
    print("=" * 60)
    print("|      SELAMAT DATANG DI TOKO PERALATAN KUCING WINGKY      |")
    print("=" * 60)
    print("\n1. Login")
    print("2. Register")
    print("3. Keluar")
    
    pilihan_utama = input("\nPilih menu (1-3): ")
    
    # ===== MENU LOGIN =====
    if pilihan_utama == "1":
        os.system('cls || clear')
        print("=" * 60)
        print("|      SELAMAT DATANG DI TOKO PERALATAN KUCING WINGKY      |")
        print("=" * 60)
        print("\n--- LOGIN ---")
        username = input("Username: ")
        password = input("Password: ")
        
        # Verifikasi login dulu disini
        if username in pengguna and pengguna[username]["password"] == password:
            user_login = username
            role_login = pengguna[username]["role"]
            status_login = True
            print(f"\nLogin berhasil! Selamat datang, {user_login}")
            time.sleep(1)
            
            # ===== MENU ADMIN =====
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
                    
                    # LIHAT PRODUK
                    if pilihan_admin == "1":
                        os.system('cls || clear')
                        print("=" * 80)
                        print("|                             DAFTAR PRODUK WINGKY                             |")
                        print("=" * 80)
                        print(f"|{'ID':<5}| {'Nama Produk':<25}| {'Kategori':<15}| {'Harga':<15} |{'Stok':<10}|")
                        print("-" * 80)
                        
                        if len(produk) == 0:
                            print("Tidak ada produk tersedia.")
                        else:
                            for id_produk, data in produk.items():
                                print(f"|{id_produk:<5}| {data['nama']:<25}| {data['kategori']:<15}| Rp{data['harga']:<13} |{data['stok']:<10}|")
                        
                        print("=" * 80)
                        time.sleep(10)
                    
                    # TAMBAH PRODUK
                    elif pilihan_admin == "2":
                        os.system('cls || clear')
                        print("=" * 50)
                        print("|               TAMBAH PRODUK BARU               |")
                        print("=" * 50)
                        

                        if len(produk) == 0:
                            id_baru = 1
                        else:
                            id_baru = max(produk.keys()) + 1
                        
                        nama = input("\nNama Produk: ")
                        kategori = input("Kategori (Makanan/Kebersihan/Grooming/Mainan): ")
                        
                        
                        harga_str = input("Harga: ")
                        if harga_str.isdigit() == False:
                            print("\nHarga harus berupa angka!")
                            time.sleep(2)
                        else:
                            harga = int(harga_str)
                            
                            stok_str = input("Stok: ")
                            if stok_str.isdigit() == False:
                                print("\nStok harus berupa angka!")
                                time.sleep(2)
                            else:
                                stok = int(stok_str)
                                produk[id_baru] = {
                                    "nama": nama,
                                    "kategori": kategori,
                                    "harga": harga,
                                    "stok": stok
                                }
                                print(f"\nProduk '{nama}' berhasil ditambahkan!")
                                time.sleep(2)
                    
                    # UPDATE PRODUK
                    elif pilihan_admin == "3":
                        os.system('cls || clear')
                        print("=" * 50)
                        print("|                UPDATE PRODUK                   |")
                        print("=" * 50)
                        
                        print(f"\n|{'ID':<5}| {'Nama Produk':<41}    |")
                        print("-" * 50)
                        for id_produk, data in produk.items():
                            print(f"|{id_produk:<5}| {data['nama']:<41}    |")
                            print("=" * 50)
                        
                        id_str = input("\nMasukkan ID produk yang ingin diupdate: ")
                        
                        if id_str.isdigit() == False:
                            print("\nID harus berupa angka!")
                            time.sleep(2)
                        else:
                            id_update = int(id_str)
                            
                            if id_update in produk:
                                print(f"\nProduk ditemukan: {produk[id_update]['nama']}")
                                print("\nPilih yang ingin diupdate:")
                                print("1. Nama")
                                print("2. Kategori")
                                print("3. Harga")
                                print("4. Stok")
                                pilih = input("Pilihan: ")
                                
                                if pilih == "1":
                                    nama_baru = input("Nama baru: ")
                                    produk[id_update]["nama"] = nama_baru
                                    print("\nNama produk berhasil diupdate!")
                                elif pilih == "2":
                                    kategori_baru = input("Kategori baru: ")
                                    produk[id_update]["kategori"] = kategori_baru
                                    print("\nKategori produk berhasil diupdate!")
                                elif pilih == "3":
                                    harga_str = input("Harga baru: ")
                                    if harga_str.isdigit() == False:
                                        print("\nHarga harus berupa angka!")
                                    else:
                                        produk[id_update]["harga"] = int(harga_str)
                                        print("\nHarga produk berhasil diupdate!")
                                elif pilih == "4":
                                    stok_str = input("Stok baru: ")
                                    if stok_str.isdigit() == False:
                                        print("\nStok harus berupa angka!")
                                    else:
                                        produk[id_update]["stok"] = int(stok_str)
                                        print("\nStok produk berhasil diupdate!")
                                else:
                                    print("\nPilihan tidak valid!")
                                time.sleep(2)
                            else:
                                print("\nProduk dengan ID tersebut tidak ditemukan!")
                                time.sleep(2)
                    
                    # HAPUS PRODUK
                    elif pilihan_admin == "4":
                        os.system('cls || clear')
                        print("=" * 50)
                        print("|                  HAPUS PRODUK                    |")
                        print("=" * 50)
                        
                        print(f"\n|{'ID':<5}| {'Nama Produk':<37}|")
                        print("-" * 50)
                        for id_produk, data in produk.items():
                            print(f"|{id_produk:<5}| {data['nama']:<37}|")
                        
                        id_str = input("\nMasukkan ID produk yang ingin dihapus: ")
                        
                        if id_str.isdigit() == False:
                            print("\nID harus berupa angka!")
                            time.sleep(2)
                        else:
                            id_hapus = int(id_str)
                            
                            if id_hapus in produk:
                                konfirmasi = input(f"\nYakin ingin menghapus '{produk[id_hapus]['nama']}'? (y/n): ")
                                if konfirmasi.lower() == "y":
                                    del produk[id_hapus]
                                    print("\nProduk berhasil dihapus!")
                                else:
                                    print("\nPenghapusan dibatalkan.")
                                time.sleep(2)
                            else:
                                print("\nProduk dengan ID tersebut tidak ditemukan!")
                                time.sleep(2)
                    
                    # CARI PRODUK
                    elif pilihan_admin == "5":
                        os.system('cls || clear')
                        print("=" * 50)
                        print("|                 CARI PRODUK                 |")
                        print("=" * 50)
                        keyword = input("\nMasukkan nama produk: ")
                        
                        print("\n" + "=" * 80)
                        print("|                        HASIL PENCARIAN                       |")
                        print("=" * 80)
                        print(f"{'ID':<5} {'Nama Produk':<25} {'Kategori':<15} {'Harga':<15} {'Stok':<10}")
                        print("-" * 80)
                        
                        ketemu = False
                        for id_produk, data in produk.items():
                            if keyword.lower() in data['nama'].lower():
                                print(f"{id_produk:<5} {data['nama']:<25} {data['kategori']:<15} Rp{data['harga']:<13} {data['stok']:<10}")
                                ketemu = True
                        
                        if ketemu == False:
                            print("Produk tidak ditemukan.")
                        
                        print("=" * 80)
                        time.sleep(3)
                    
                    # LOGOUT
                    elif pilihan_admin == "6":
                        print("\nLogout berhasil!")
                        time.sleep(1)
                        status_login = False
                    
                    else:
                        print("\nPilihan tidak valid!")
                        time.sleep(2)
            
            # ===== MENU USER =====
            else:
                while status_login == True:
                    os.system('cls || clear')
                    print("=" * 50)
                    print(f"|           MENU PELANGGAN - Halo, {user_login}!         |")
                    print("=" * 50)
                    print("\n1. Lihat Semua Produk")
                    print("2. Cari Produk")
                    print("3. Tambah ke Keranjang")
                    print("4. Lihat Keranjang")
                    print("5. Hapus dari Keranjang")
                    print("6. Checkout")
                    print("7. Logout")
                    
                    pilihan_user = input("\nPilih menu (1-7): ")
                    
                    # LIHAT PRODUK
                    if pilihan_user == "1":
                        os.system('cls || clear')
                        print("=" * 80)
                        print("|                             DAFTAR PRODUK WINGKY                             |")
                        print("=" * 80)
                        print(f"{'ID':<5} {'Nama Produk':<25} {'Kategori':<15} {'Harga':<15} {'Stok':<10}")
                        print("-" * 80)
                        
                        if len(produk) == 0:
                            print("Tidak ada produk tersedia.")
                        else:
                            for id_produk, data in produk.items():
                                print(f"{id_produk:<5} {data['nama']:<25} {data['kategori']:<15} Rp{data['harga']:<13} {data['stok']:<10}")
                        
                        print("=" * 80)
                        time.sleep(7)
                    
                    # CARI PRODUK
                    elif pilihan_user == "2":
                        os.system('cls || clear')
                        print("=" * 50)
                        print("|                  CARI PRODUK                   |")
                        print("=" * 50)
                        keyword = input("\nMasukkan nama produk: ")
                        
                        print("\n" + "=" * 80)
                        print("|                        HASIL PENCARIAN                        |")
                        print("=" * 80)
                        print(f"{'ID':<5} {'Nama Produk':<25} {'Kategori':<15} {'Harga':<15} {'Stok':<10}")
                        print("-" * 80)
                        
                        ketemu = False
                        for id_produk, data in produk.items():
                            if keyword.lower() in data['nama'].lower():
                                print(f"{id_produk:<5} {data['nama']:<25} {data['kategori']:<15} Rp{data['harga']:<13} {data['stok']:<10}")
                                ketemu = True
                        
                        if ketemu == False:
                            print("Produk tidak ditemukan.")
                        
                        print("=" * 80)
                        time.sleep(3)
                    
                    # TAMBAH KE KERANJANG
                    elif pilihan_user == "3":
                        os.system('cls || clear')
                        print("=" * 80)
                        print("|                             TAMBAH KE KERANJANG                              |")
                        print("\n" + "=" * 80)
                        print(f"| {'ID':<2}| {'Nama Produk':<26}| {'Kategori':<15}| {'Harga':<15}| {'Stok':<10}|")
                        print("-" * 80)
                        for id_produk, data in produk.items():
                            print(f"| {id_produk:<2}| {data['nama']:<26}| {data['kategori']:<15}| Rp{data['harga']:<13}| {data['stok']:<10}|")
                        print("=" * 80)
                        
                        id_str = input("\nMasukkan ID produk yang ingin dibeli: ")
                        
                        if id_str.isdigit() == False:
                            print("\nID harus berupa angka!")
                            time.sleep(2)
                        else:
                            id_beli = int(id_str)
                            
                            if id_beli in produk:
                                jumlah_str = input(f"Jumlah {produk[id_beli]['nama']} yang ingin dibeli: ")
                                
                                if jumlah_str.isdigit() == False:
                                    print("\nJumlah harus berupa angka!")
                                    time.sleep(2)
                                else:
                                    jumlah = int(jumlah_str)
                                    
                                    if jumlah > produk[id_beli]['stok']:
                                        print(f"\nStok tidak cukup! Stok tersedia: {produk[id_beli]['stok']}")
                                        time.sleep(2)
                                    elif jumlah <= 0:
                                        print("\nJumlah harus lebih dari 0!")
                                        time.sleep(2)
                                    else:
                                        # Inisialisasi keranjang
                                        if user_login not in keranjang:
                                            keranjang[user_login] = {}
                                        
                                        # Cek apakah produk sudah ada di keranjang
                                        if id_beli in keranjang[user_login]:
                                            keranjang[user_login][id_beli]["jumlah"] += jumlah
                                        else:
                                            keranjang[user_login][id_beli] = {
                                                "nama": produk[id_beli]["nama"],
                                                "harga": produk[id_beli]["harga"],
                                                "jumlah": jumlah
                                            }
                                        
                                        print(f"\n{jumlah} {produk[id_beli]['nama']} berhasil ditambahkan ke keranjang!")
                                        time.sleep(2)
                            else:
                                print("\nProduk dengan ID tersebut tidak ditemukan!")
                                time.sleep(2)
                    
                    # LIHAT KERANJANG
                    elif pilihan_user == "4":
                        os.system('cls || clear')
                        print("=" * 80)
                        print("|                              KERANJANG BELANJA                               |")
                        print("=" * 80)
                        
                        if user_login not in keranjang or len(keranjang[user_login]) == 0:
                            print("\nKeranjang belanja kosong.")
                            print("=" * 80)
                        else:
                            print(f"| {'No':<5}| {'Nama Produk':<25}| {'Harga':<15}| {'Jumlah':<10}| {'Subtotal':<14}|")
                            print("-" * 80)
                            
                            total = 0
                            nomor = 1
                            for id_produk, item in keranjang[user_login].items():
                                subtotal = item["harga"] * item["jumlah"]
                                total += subtotal
                                print(f"| {nomor:<5}| {item['nama']:<25}| Rp{item['harga']:<13}| {item['jumlah']:<10}| Rp{subtotal:<14}|")
                                nomor += 1
                            
                            print("-" * 80)
                            print(f"| {'TOTAL':<56} Rp{total:<13}    |")
                            print("=" * 80)
                        
                        time.sleep(7)
                    
                    # HAPUS DARI KERANJANG
                    elif pilihan_user == "5":
                        os.system('cls || clear')
                        print("=" * 50)
                        print("|             HAPUS DARI KERANJANG               |")
                        print("=" * 50)
                        
                        if user_login not in keranjang or len(keranjang[user_login]) == 0:
                            print("\nKeranjang belanja kosong.")
                            time.sleep(2)
                        else:
                            print(f"\n  {'No':<5} {'Nama Produk':<25} {'Jumlah':<10}")
                            print("-" * 50)
                            
                            nomor = 1
                            list_id = list(keranjang[user_login].keys())
                            for id_produk in list_id:
                                item = keranjang[user_login][id_produk]
                                print(f"  {nomor:<5} {item['nama']:<25} {item['jumlah']:<10}")
                                nomor += 1
                            
                            no_str = input("\nMasukkan nomor item yang ingin dihapus: ")
                            
                            if no_str.isdigit() == False:
                                print("\nNomor harus berupa angka!")
                                time.sleep(2)
                            else:
                                no_hapus = int(no_str)
                                
                                if no_hapus < 1 or no_hapus > len(keranjang[user_login]):
                                    print("\nNomor tidak valid!")
                                    time.sleep(2)
                                else:
                                    id_hapus = list_id[no_hapus - 1]
                                    nama_item = keranjang[user_login][id_hapus]["nama"]
                                    konfirmasi = input(f"\nYakin ingin menghapus '{nama_item}' dari keranjang? (y/n): ")
                                    
                                    if konfirmasi.lower() == "y":
                                        del keranjang[user_login][id_hapus]
                                        print("\nItem berhasil dihapus dari keranjang!")
                                    else:
                                        print("\nPenghapusan dibatalkan.")
                                    time.sleep(2)
                    
                    # CHECKOUT
                    elif pilihan_user == "6":
                        os.system('cls || clear')
                        print("=" * 80)
                        print("|                                CHECKOUT                                   |")
                        print("=" * 80)
                        
                        if user_login not in keranjang or len(keranjang[user_login]) == 0:
                            print("\nKeranjang belanja kosong. Tidak ada yang bisa dicheckout.")
                            time.sleep(2)
                        else:
                            print("\n" + "=" * 80)
                            print(f"{'No':<5} {'Nama Produk':<25} {'Harga':<15} {'Jumlah':<10} {'Subtotal':<15}")
                            print("-" * 80)
                            
                            total = 0
                            nomor = 1
                            for id_produk, item in keranjang[user_login].items():
                                subtotal = item["harga"] * item["jumlah"]
                                total += subtotal
                                print(f"{nomor:<5} {item['nama']:<25} Rp{item['harga']:<13} {item['jumlah']:<10} Rp{subtotal:<13}")
                                nomor += 1
                            
                            print("-" * 80)
                            print(f"{'TOTAL PEMBAYARAN':<56} Rp{total:<15}")
                            print("=" * 80)
                            
                            konfirmasi = input("\nLanjutkan pembayaran? (y/n): ")
                            
                            if konfirmasi.lower() == "y":
                                # Kurangi stok produk
                                for id_produk, item in keranjang[user_login].items():
                                    produk[id_produk]["stok"] -= item["jumlah"]
                                
                                # Kosongkan keranjang
                                keranjang[user_login] = {}
                                
                                print("\n" + "=" * 50)
                                print("               PEMBAYARAN BERHASIL!")
                                print("     Terima kasih telah berbelanja di Wingky!")
                                print("=" * 50)
                                time.sleep(8)
                            else:
                                print("\nPembayaran dibatalkan.")
                                time.sleep(4)
                    
                    # LOGOUT
                    elif pilihan_user == "7":
                        print("\nLogout berhasil!")
                        time.sleep(3)
                        status_login = False
                    
                    else:
                        print("\nPilihan tidak valid!")
                        time.sleep(3)
        else:
            print("\nUsername atau password salah!")
            time.sleep(3)
    
    # ===== MENU REGISTER =====
    elif pilihan_utama == "2":
        os.system('cls || clear')
        print("=" * 50)
        print("   SELAMAT DATANG DI TOKO PERALATAN KUCING WINGKY")
        print("=" * 50)
        print("\n--- REGISTER AKUN BARU ---")
        
        username_baru = input("Username: ")
        password_baru = input("Password: ")
        
        pengguna[username_baru] = {
            "password": password_baru,
            "role": "user"
        }
        print(f"\nRegistrasi berhasil! Akun '{username_baru}' telah dibuat.")
        print("Silakan login untuk melanjutkan.")
        time.sleep(4)
    
    # ===== KELUAR =====
    elif pilihan_utama == "3":
        os.system('cls || clear')
        print("=" * 60)
        print("|       Terima kasih telah mengunjungi Toko Wingky!        |")
        print("=" * 60)
        break
    
    else:
        print("\nPilihan kamu tidak valid nih!")
        time.sleep(3)