import os
import time #buat ngasih efek delay gitu diaa
#mohon ampun abang abang ini tabel saya banyak yang belum sempat saya baikin lagi buat outputnya T^T

# Database pengguna nya pakai nested list
# trus ini bacanya [username, password, role]
pengguna = [
    ["gea", "pacar seokjin", "admin"],
    ["user", "user123", "user"]
]

# Database produk juga pakai nested list
# ini bacanya: [id, nama, kategori, harga, stok]
produk = [
    [1, "Whiskas 1kg", "Makanan", 50000, 20],
    [2, "Royal Canin 2kg", "Makanan", 150000, 15],
    [3, "Pasir Gumpal 5kg", "Kebersihan", 45000, 30],
    [4, "Sisir Kucing", "Grooming", 25000, 50],
    [5, "Mainan Bola", "Mainan", 15000, 40]
]

# Keranjang belanja
# Format: {username: [[id_produk, nama, harga, jumlah], ...]}
keranjang = {}

# Variabel untuk ngecek user yang login
user_login = ""
role_login = ""
status_login = False

# PROGRAM UTAMA
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
        
        # verifikasi duluu disini
        ketemu = False #kenapa false? karna ini ceritanya belum dapat user yang cocok
        for i in pengguna:
            if i[0] == username and i[1] == password:
                user_login = username
                role_login = i[2]
                status_login = True
                ketemu = True
                break
        
        if ketemu == True:
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
                            for i in produk:
                                print(f"|{i[0]:<5}| {i[1]:<25}| {i[2]:<15}| Rp{i[3]:<13} |{i[4]:<10}|")
                        
                        print("=" * 80)
                        time.sleep(10)
                    
                    # TAMBAH PRODUK
                    elif pilihan_admin == "2":
                        os.system('cls || clear')
                        print("=" * 50)
                        print("|               TAMBAH PRODUK BARU               |")
                        print("=" * 50)
                        
                        # Generate ID otomatis
                        if len(produk) == 0:
                            id_baru = 1
                        else:
                            id_baru = produk[-1][0] + 1
                        
                        nama = input("\nNama Produk: ")
                        kategori = input("Kategori (Makanan/Kebersihan/Grooming/Mainan): ")
                        
                        # Error handling
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
                                produk.append([id_baru, nama, kategori, harga, stok])
                                print(f"\nProduk '{nama}' berhasil ditambahkan!")
                                time.sleep(2)
                    
                    #FITR UPDATE PRODUK
                    elif pilihan_admin == "3":
                        os.system('cls || clear')
                        print("=" * 50)
                        print("|                UPDATE PRODUK                   |")
                        print("=" * 50)
                        
                        print(f"\n|{'ID':<5}| {'Nama Produk':<41}|")
                        print("-" * 50)
                        for i in produk:
                            print(f"|{i[0]:<5}| {i[1]:<41}|")
                            print("=" * 50)
                        
                        id_str = input("\nMasukkan ID produk yang ingin diupdate: ")
                        
                        if id_str.isdigit() == False:
                            print("\nID harus berupa angka!")
                            time.sleep(2)
                        else:
                            id_update = int(id_str)
                            ketemu = False
                            
                            for i in produk:
                                if i[0] == id_update:
                                    ketemu = True
                                    print(f"\nProduk ditemukan: {i[1]}")
                                    print("\nPilih yang ingin diupdate:")
                                    print("1. Nama")
                                    print("2. Kategori")
                                    print("3. Harga")
                                    print("4. Stok")
                                    pilih = input("Pilihan: ")
                                    
                                    if pilih == "1":
                                        nama_baru = input("Nama baru: ")
                                        i[1] = nama_baru
                                        print("\nNama produk berhasil diupdate!")
                                    elif pilih == "2":
                                        kategori_baru = input("Kategori baru: ")
                                        i[2] = kategori_baru
                                        print("\nKategori produk berhasil diupdate!")
                                    elif pilih == "3":
                                        harga_str = input("Harga baru: ")
                                        if harga_str.isdigit() == False:
                                            print("\nHarga harus berupa angka!")
                                        else:
                                            i[3] = int(harga_str)
                                            print("\nHarga produk berhasil diupdate!")
                                    elif pilih == "4":
                                        stok_str = input("Stok baru: ")
                                        if stok_str.isdigit() == False:
                                            print("\nStok harus berupa angka!")
                                        else:
                                            i[4] = int(stok_str)
                                            print("\nStok produk berhasil diupdate!")
                                    else:
                                        print("\nPilihan tidak valid!")
                                    time.sleep(2)
                                    break
                            
                            if ketemu == False:
                                print("\nProduk dengan ID tersebut tidak ditemukan!")
                                time.sleep(2)
                    
                    # FITUR HAPUS PRODUK
                    elif pilihan_admin == "4":
                        os.system('cls || clear')
                        print("=" * 50)
                        print("|                  HAPUS PRODUK                    |")
                        print("=" * 50)
                        
                        print(f"\n|{'ID':<5}| {'Nama Produk':413}|")
                        print("-" * 50)
                        for i in produk:
                            print(f"|{i[0]:<5}| {i[1]:<37}|")
                        
                        id_str = input("\nMasukkan ID produk yang ingin dihapus: ")
                        
                        if id_str.isdigit() == False:
                            print("\nID harus berupa angka!")
                            time.sleep(2)
                        else:
                            id_hapus = int(id_str)
                            ketemu = False
                            
                            for i in produk:
                                if i[0] == id_hapus:
                                    ketemu = True
                                    konfirmasi = input(f"\nYakin ingin menghapus '{i[1]}'? (y/n): ")
                                    if konfirmasi.lower() == "y":
                                        produk.remove(i)
                                        print("\nProduk berhasil dihapus!")
                                    else:
                                        print("\nPenghapusan dibatalkan.")
                                    time.sleep(2)
                                    break
                            
                            if ketemu == False:
                                print("\nProduk dengan ID tersebut tidak ditemukan!")
                                time.sleep(2)
                    
                    #FITUR CARI PRODUK
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
                        for i in produk:
                            if keyword.lower() in i[1].lower():
                                print(f"{i[0]:<5} {i[1]:<25} {i[2]:<15} Rp{i[3]:<13} {i[4]:<10}")
                                ketemu = True
                        
                        if ketemu == False:
                            print("Produk tidak ditemukan.")
                        
                        print("=" * 80)
                        time.sleep(3)
                    
                    # FITUR LOGOUT
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
                    
                    #FITUR LIHAT PRODUK
                    if pilihan_user == "1":
                        os.system('cls || clear')
                        print("=" * 80)
                        print("|                        DAFTAR PRODUK WINGKY                        |")
                        print("=" * 80)
                        print(f"{'ID':<5} {'Nama Produk':<25} {'Kategori':<15} {'Harga':<15} {'Stok':<10}")
                        print("-" * 80)
                        
                        if len(produk) == 0:
                            print("Tidak ada produk tersedia.")
                        else:
                            for i in produk:
                                print(f"{i[0]:<5} {i[1]:<25} {i[2]:<15} Rp{i[3]:<13} {i[4]:<10}")
                        
                        print("=" * 80)
                        time.sleep(3)
                    
                    #FITUR CARI PRODUK
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
                        for i in produk:
                            if keyword.lower() in i[1].lower():
                                print(f"{i[0]:<5} {i[1]:<25} {i[2]:<15} Rp{i[3]:<13} {i[4]:<10}")
                                ketemu = True
                        
                        if ketemu == False:
                            print("Produk tidak ditemukan.")
                        
                        print("=" * 80)
                        time.sleep(3)
                    
                    #FITUR BUAT NAMBAH KE KERANJANG
                    elif pilihan_user == "3":
                        os.system('cls || clear')
                        print("=" * 50)
                        print("|            TAMBAH KE KERANJANG             |")
                        print("=" * 50)
                        
                        # Tampilkan produk
                        print("\n" + "=" * 80)
                        print(f"{'ID':<5} {'Nama Produk':<25} {'Kategori':<15} {'Harga':<15} {'Stok':<10}")
                        print("-" * 80)
                        for i in produk:
                            print(f"{i[0]:<5} {i[1]:<25} {i[2]:<15} Rp{i[3]:<13} {i[4]:<10}")
                        print("=" * 80)
                        
                        id_str = input("\nMasukkan ID produk yang ingin dibeli: ")
                        
                        if id_str.isdigit() == False:
                            print("\nID harus berupa angka!")
                            time.sleep(2)
                        else:
                            id_beli = int(id_str)
                            ketemu = False
                            
                            for i in produk:
                                if i[0] == id_beli:
                                    ketemu = True
                                    jumlah_str = input(f"Jumlah {i[1]} yang ingin dibeli: ")
                                    
                                    if jumlah_str.isdigit() == False:
                                        print("\nJumlah harus berupa angka!")
                                        time.sleep(2)
                                    else:
                                        jumlah = int(jumlah_str)
                                        
                                        if jumlah > i[4]:
                                            print(f"\nStok tidak cukup! Stok tersedia: {i[4]}")
                                            time.sleep(2)
                                        elif jumlah <= 0:
                                            print("\nJumlah harus lebih dari 0!")
                                            time.sleep(2)
                                        else:
                                            # Inisialisasi keranjang
                                            if user_login not in keranjang:
                                                keranjang[user_login] = []
                                            
                                            # Cek apakah produk yang dimau sudah ada di keranjang
                                            ada = False
                                            for item in keranjang[user_login]:
                                                if item[0] == id_beli:
                                                    item[3] = item[3] + jumlah
                                                    ada = True
                                                    break
                                            
                                            if ada == False:
                                                keranjang[user_login].append([id_beli, i[1], i[3], jumlah])
                                            
                                            print(f"\n{jumlah} {i[1]} berhasil ditambahkan ke keranjang!")
                                            time.sleep(2)
                                    break
                            
                            if ketemu == False:
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
                            print(f"{'No':<5} {'Nama Produk':<25} {'Harga':<15} {'Jumlah':<10} {'Subtotal':<15}")
                            print("-" * 80)
                            
                            total = 0
                            nomor = 1
                            for item in keranjang[user_login]:
                                subtotal = item[2] * item[3]
                                total = total + subtotal
                                print(f"{nomor:<5} {item[1]:<25} Rp{item[2]:<13} {item[3]:<10} Rp{subtotal:<13}")
                                nomor = nomor + 1
                            
                            print("-" * 80)
                            print(f"{'TOTAL':<56} Rp{total:<13}")
                            print("=" * 80)
                        
                        time.sleep(3)
                    
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
                            print(f"\n{'No':<5} {'Nama Produk':<25} {'Jumlah':<10}")
                            print("-" * 45)
                            
                            nomor = 1
                            for item in keranjang[user_login]:
                                print(f"{nomor:<5} {item[1]:<25} {item[3]:<10}")
                                nomor = nomor + 1
                            
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
                                    item_hapus = keranjang[user_login][no_hapus - 1]
                                    konfirmasi = input(f"\nYakin ingin menghapus '{item_hapus[1]}' dari keranjang? (y/n): ")
                                    
                                    if konfirmasi.lower() == "y":
                                        keranjang[user_login].pop(no_hapus - 1)
                                        print("\nItem berhasil dihapus dari keranjang!")
                                    else:
                                        print("\nPenghapusan dibatalkan.")
                                    time.sleep(2)
                    
                    # CHECKOUT
                    elif pilihan_user == "6":
                        os.system('cls || clear')
                        print("=" * 50)
                        print("|                  CHECKOUT                     |")
                        print("=" * 50)
                        
                        if user_login not in keranjang or len(keranjang[user_login]) == 0:
                            print("\nKeranjang belanja kosong. Tidak ada yang bisa dicheckout.")
                            time.sleep(2)
                        else:
                            print("\n" + "=" * 80)
                            print(f"{'No':<5} {'Nama Produk':<25} {'Harga':<15} {'Jumlah':<10} {'Subtotal':<15}")
                            print("-" * 80)
                            
                            total = 0
                            nomor = 1
                            for item in keranjang[user_login]:
                                subtotal = item[2] * item[3]
                                total = total + subtotal
                                print(f"{nomor:<5} {item[1]:<25} Rp{item[2]:<13} {item[3]:<10} Rp{subtotal:<13}")
                                nomor = nomor + 1
                            
                            print("-" * 80)
                            print(f"{'TOTAL PEMBAYARAN':<56} Rp{total:<13}")
                            print("=" * 80)
                            
                            konfirmasi = input("\nLanjutkan pembayaran? (y/n): ")
                            
                            if konfirmasi.lower() == "y":
                                # Kurangi stok produk
                                for item in keranjang[user_login]:
                                    for i in produk:
                                        if i[0] == item[0]:
                                            i[4] = i[4] - item[3]
                                            break
                                
                                # Kosongkan keranjang
                                keranjang[user_login] = []
                                
                                print("\n" + "=" * 50)
                                print("     PEMBAYARAN BERHASIL!")
                                print("     Terima kasih telah berbelanja di Wingky!")
                                print("=" * 50)
                                time.sleep(3)
                            else:
                                print("\nPembayaran dibatalkan.")
                                time.sleep(2)
                    
                    # LOGOUT
                    elif pilihan_user == "7":
                        print("\nLogout berhasil!")
                        time.sleep(1)
                        status_login = False
                    
                    else:
                        print("\nPilihan tidak valid!")
                        time.sleep(2)
        else:
            print("\nUsername atau password salah!") #jadi kalau login nya gagal, muncul pesan erornyaa
            time.sleep(2)
    
    # ===== MENU REGISTER =====
    elif pilihan_utama == "2":
        os.system('cls || clear')
        print("=" * 50)
        print("   SELAMAT DATANG DI TOKO PERALATAN KUCING WINGKY")
        print("=" * 50)
        print("\n--- REGISTER AKUN BARU ---")
        
        username_baru = input("Username: ")
        password_baru = input("Password: ")
        
        pengguna.append([username_baru, password_baru, "user"]) #jadi kita nambahin user baru ke list pengguna dengan role "user" jadi bisa kita pastiin bukan admin
        print(f"\nRegistrasi berhasil! Akun '{username_baru}' telah dibuat.")
        print("Silakan login untuk melanjutkan.")
        time.sleep(2)
    
    # ===== BAGIAN KELUAR =====
    elif pilihan_utama == "3":
        os.system('cls || clear')
        print("=" * 60)
        print("|       Terima kasih telah mengunjungi Toko Wingky!        |")
        print("=" * 60)
        break #Kita keluar dari loop while True nya 
    
    else:
        print("\nPilihan kamu tidak valid nih!") #jadi kalau milih pilihan diluar 1-3 eror dia makanya outputnya bilang gak valid
        time.sleep(2)