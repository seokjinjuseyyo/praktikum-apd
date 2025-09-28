print("=" * 65)
print("|          SELAMAT DATANG DI TOKO MAKANAN KUCING WINGKY         |")
print("=" * 65)

status_member = input("Apakah Anda member? (ya/tidak): ")

if status_member == "ya":
    print("\n-------- SILAHKAN ANDA MELAKUKAN LOGIN TERLEBIH DAHULU --------")
    
    username_input = input("Silahkan masukkan username anda: ")
    password_input = input("Silahkan masukkan password anda: ")
    
    username_benar = "gea"  
    password_benar = "007"   
    
    login_berhasil = True if username_input == username_benar and password_input == password_benar else False
    
    if login_berhasil:
        print(f"\nLogin berhasil! Selamat datang {username_benar}, selamat berbelanja!")
        
        print("\n" + "=" * 65)
        print("|          MENU MAKANAN KUCING YANG TERSEDIA HARI INI           |")
        print("=" * 65)
        print("| No |            Nama Produk             |        Harga        |")
        print("|----|------------------------------------|---------------------|")
        print("| 1  | Royal Canin Persian Adult          |     Rp  85.000      |")
        print("| 2  | Whiskas Dry Food Tuna              |     Rp  45.000      |")
        print("| 3  | Pro Plan Kitten Chicken            |     Rp 120.000      |")
        print("| 4  | Me-O Adult Cat Seafood             |     Rp  35.000      |")
        print("| 5  | Hills Science Diet Indoor          |     Rp 150.000      |")
        print("=" * 65)
        
        pilihan = int(input("\nSilahkan pilih etalase produk yang diinginkan (1/2/3/4/5): "))
        quantity = int(input("Masukkan jumlah produk yang ingin anda beli: "))
        
        if pilihan == 1:
            nama_produk = "Royal Canin Persian Adult"
            harga_satuan = 85000
        elif pilihan == 2:
            nama_produk = "Whiskas Dry Food Tuna"
            harga_satuan = 45000
        elif pilihan == 3:
            nama_produk = "Pro Plan Kitten Chicken"
            harga_satuan = 120000
        elif pilihan == 4:
            nama_produk = "Me-O Adult Cat Seafood"
            harga_satuan = 35000
        elif pilihan == 5:
            nama_produk = "Hills Science Diet Indoor"
            harga_satuan = 150000
        else:
            print("Pilihan tidak valid!")
            nama_produk = "Produk Tidak Dikenal"
            harga_satuan = 0
        
        harga_sebelum_diskon = harga_satuan * quantity
        diskon_persen = 15
        total_diskon = harga_sebelum_diskon * diskon_persen / 100
        harga_setelah_diskon = harga_sebelum_diskon - total_diskon
        
        print("\n" + "=" * 65)
        print("|                         STRUK PEMBELIAN                       |")
        print("=" * 65)
        print(f"| Produk       : {nama_produk:<30}                 |")
        print(f"| Jumlah       : {quantity:<2} pack                                        |")
        print(f"| Harga Satuan : Rp {harga_satuan:<20,}                        |")
        print("|-" + "-" * 61 + "-|")
        print(f"| Harga Sebelum Diskon : Rp {harga_sebelum_diskon:<20,}                |")
        print(f"| Diskon Member (15%)  : Rp {total_diskon:<20,}                |")
        print(f"| TOTAL BAYAR          : Rp {harga_setelah_diskon:<20,}                |")
        print("=" * 65)
        print("       Terimakasih karena telah berbelanja di toko WINGKY          ")
        print("                Semoga hari anda menyenangkan                      ")
        
    else:
        print("\nWah login anda gagal! Username atau password anda salah3")
        print("Silahkan coba lagi atau sign in sebagai member baru")

else:
    print("\n" + "=" * 65)
    print("|          MENU MAKANAN KUCING YANG TERSEDIA HARI INI           |")
    print("=" * 65)
    print("| No |            Nama Produk             |        Harga        |")
    print("|----|------------------------------------|---------------------|")
    print("| 1  | Royal Canin Persian Adult          |     Rp  85.000      |")
    print("| 2  | Whiskas Dry Food Tuna              |     Rp  45.000      |")
    print("| 3  | Pro Plan Kitten Chicken            |     Rp 120.000      |")
    print("| 4  | Me-O Adult Cat Seafood             |     Rp  35.000      |")
    print("| 5  | Hills Science Diet Indoor          |     Rp 157.500      |")
    print("=" * 65)
    
    pilihan = int(input("\nSilahkan pilih etalase produk yang diinginkan (1/2/3/4/5): "))
    quantity = int(input("Masukkan jumlah produk yang ingin anda beli: "))
    
    if pilihan == 1:
        nama_produk = "Royal Canin Persian Adult"
        harga_satuan = 85000
    elif pilihan == 2:
        nama_produk = "Whiskas Dry Food Tuna"
        harga_satuan = 45000
    elif pilihan == 3:
        nama_produk = "Pro Plan Kitten Chicken"
        harga_satuan = 120000
    elif pilihan == 4:
        nama_produk = "Me-O Adult Cat Seafood"
        harga_satuan = 35000
    elif pilihan == 5:
        nama_produk = "Hills Science Diet Indoor"
        harga_satuan = 157500
    else:
        print("Pilihan tidak valid!")
        nama_produk = "Produk Tidak Dikenal"
        harga_satuan = 0
    
    total_harga = harga_satuan * quantity
    
    print("\n" + "=" * 65)
    print("|                        STRUK PEMBELIAN                        |")
    print("=" * 65)
    print(f"| Produk       : {nama_produk:<30}                 |")
    print(f"| Jumlah       : {quantity:<2} pack                                        |")
    print(f"| Harga Satuan : Rp {harga_satuan:<30}              |")
    print("|-" + "-" * 61 + "-|")
    print(f"| TOTAL BAYAR : Rp {total_harga:<30}               |")
    print("=" * 65)
    print("       Terima kasih karena telah berbelanja di toko WINGKY       ")
    print("                  Semoga hari anda menyenangkan                  ")
    print("       Daftar member sekarang untuk mendapatkan diskon 15%!      ")