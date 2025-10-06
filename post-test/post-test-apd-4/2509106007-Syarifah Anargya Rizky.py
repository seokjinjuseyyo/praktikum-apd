import os

username_benar = "gea"
password_benar = "007"

lanjut_program = True

while lanjut_program:
    os.system('cls || clear')
    
    print("=" * 65)
    print("|          SELAMAT DATANG DI TOKO MAKANAN KUCING WINGKY         |")
    print("=" * 65)
    print()
    
    status_member = input("Apakah Anda merupakan member toko wingky? (y/n): ")
    
    if status_member == "Y":
        status_member = "y"
    elif status_member == "N":
        status_member = "n"
    
    is_member = False
    nama_user = ""
    
    if status_member == "y":
        print()
        print("-------- SILAHKAN ANDA MELAKUKAN LOGIN TERLEBIH DAHULU --------")
        print()
        
        kesempatan = 3
        
        while kesempatan > 0:
            username_input = input("Silahkan masukkan username anda: ")
            password_input = input("Silahkan masukkan password anda: ")
            
            username_bersih = ""
            password_bersih = ""
            
            for huruf in username_input:
                if huruf != " ":
                    username_bersih = username_bersih + huruf
            for huruf in password_input:
                if huruf != " ":
                    password_bersih = password_bersih + huruf
            if username_bersih == "" or password_bersih == "":
                print()
                print("Username dan password anda tidak boleh kosong!")
                kesempatan = kesempatan - 1
                if kesempatan > 0:
                    print(f"Sisa percobaan: {kesempatan}")
                    print()
            else:
                if username_bersih == username_benar and password_bersih == password_benar:
                    is_member = True
                    nama_user = username_benar
                    print()
                    print(f"Login berhasil! Selamat datang kembali {nama_user}, selamat berbelanja!")
                    print()
                    kesempatan = 0
                else:
                    kesempatan = kesempatan - 1
                    if kesempatan > 0:
                        print()
                        print(" Wah Login anda gagal nih! sepertinya Username atau password anda salah.")
                        print(f"Sisa percobaan: {kesempatan}")
                        print()
                    else:
                        print()
                        print("Anda telah gagal login 3 kali!")
                        print("Anda akan dilanjutkan sebagai non-member.")
                        print()
    else:
        print()
        print("Anda akan berbelanja sebagai non-member")
        print()
    
    keranjang = ""
    total_belanja = 0
    lanjut_belanja = True
    produk_baru = ""
    while lanjut_belanja:
        os.system('cls || clear')
        
        if produk_baru != "":
            print()
            print(produk_baru)
            print(f"Total belanja sementara: Rp{total_belanja:,}")
            print()
        
        print("=" * 65)
        print("|          MENU MAKANAN KUCING YANG TERSEDIA HARI INI           |")
        print("=" * 65)
        print("| No |            Nama Produk             |        Harga        |")
        print("|----|------------------------------------|---------------------|")
        print("| 1  | Royal Canin Persian Adult          |     Rp  85.000      |")
        print("| 2  | Whiskas Dry Food Tuna              |     Rp  48.000      |")
        print("| 3  | Pro Plan Kitten Chicken            |     Rp 123.000      |")
        print("| 4  | Me-O Adult Cat Seafood             |     Rp  35.000      |")
        print("| 5  | Hills Science Diet Indoor          |     Rp 157.500      |")
        print("| 6  | CHECKOUT                           |                     |")
        print("=" * 65)
        print()
        
        pilihan = input("Silahkan pilih menu (1/2/3/4/5/6): ")

        if pilihan == "6":
            if keranjang == "":
                print()
                print("Waduh keranjang belanja Anda masih kosong nih!")
                print("Silahkan pilih produk terlebih dahulu!")
                produk_baru = ""
            else:
                lanjut_belanja = False
                
        elif pilihan == "1":
            nama_produk = "Royal Canin Persian Adult"
            harga_perpcs = 85000
            
            quantity = int(input("Masukkan jumlah produk yang ingin anda beli: "))
            
            subtotal = harga_perpcs * quantity
            total_belanja = total_belanja + subtotal
            
            keranjang = keranjang + f"| {nama_produk:<29} | {quantity:<4} pack | Rp {subtotal:<14,} |\n"
            
            produk_baru = f"{nama_produk} ({quantity} pack) berhasil ditambahkan pada keranjang anda!"
            
        elif pilihan == "2":
            nama_produk = "Whiskas Dry Food Tuna"
            harga_perpcs = 48000
            
            quantity = int(input("Masukkan jumlah produk yang ingin anda beli: "))
            
            subtotal = harga_perpcs * quantity
            total_belanja = total_belanja + subtotal
            
            keranjang = keranjang + f"| {nama_produk:<29} | {quantity:<4} pack | Rp {subtotal:<14,} |\n"
            
            produk_baru = f"{nama_produk} ({quantity} pack) berhasil ditambahkan pada keranjang anda!"
            
        elif pilihan == "3":
            nama_produk = "Pro Plan Kitten Chicken"
            harga_perpcs = 123000
            
            quantity = int(input("Masukkan jumlah produk yang ingin anda beli: "))
            
            subtotal = harga_perpcs * quantity
            total_belanja = total_belanja + subtotal
            
            keranjang = keranjang + f"| {nama_produk:<29} | {quantity:<4} pack | Rp {subtotal:<14,} |\n"
            
            produk_baru = f"{nama_produk} ({quantity} pack) berhasil ditambahkan pada keranjang anda!"
            
        elif pilihan == "4":
            nama_produk = "Me-O Adult Cat Seafood"
            harga_perpcs = 35000
            
            quantity = int(input("Masukkan jumlah produk yang ingin anda beli: "))
            
            subtotal = harga_perpcs * quantity
            total_belanja = total_belanja + subtotal
            
            keranjang = keranjang + f"| {nama_produk:<29} | {quantity:<4} pack | Rp {subtotal:<14,} |\n"
            
            produk_baru = f"{nama_produk} ({quantity} pack) berhasil ditambahkan pada keranjang anda!"
            
        elif pilihan == "5":
            nama_produk = "Hills Science Diet Indoor"
            harga_perpcs = 157500
            
            quantity = int(input("Masukkan jumlah produk yang ingin anda beli: "))
            
            subtotal = harga_perpcs * quantity
            total_belanja = total_belanja + subtotal
            
            keranjang = keranjang + f"| {nama_produk:<29} | {quantity:<4} pack | Rp {subtotal:<14,} |\n"
            
            produk_baru = f"{nama_produk} ({quantity} pack) berhasil ditambahkan pada keranjang anda!"
            
        else:
            print()
            print("Pilihan anda tidak valid nih! Silahkan pilih menu yang tersedia yaa.")
            produk_baru = ""
    
    os.system('cls || clear')
    
    print()
    print("=" * 65)
    print("|               STRUK PEMBELIAN DI TOKO WINGKY                  |")
    print("=" * 65)
    print("|             Produk            |   Jumlah  |       Harga       |")
    print("|-------------------------------|-----------|-------------------|")
    print(keranjang, end="")
    print("|" + "-" * 63 + "|")
    
    if is_member == True:
        diskon_persen = 15
        total_diskon = total_belanja * diskon_persen / 100
        total_bayar = total_belanja - total_diskon
        
        print(f"| Harga Sebelum Diskon : Rp {total_belanja:<20,}                |")
        print(f"| Diskon Member (15%)  : Rp {total_diskon:<20,}                |")
        print(f"| TOTAL BAYAR          : Rp {total_bayar:<20,}                |")
    else:
        print(f"| TOTAL BAYAR          : Rp {total_belanja:<22,}              |")
    
    print("=" * 65)
    print("       Terimakasih karena telah berbelanja di toko WINGKY       ")
    print("                Semoga hari anda menyenangkan                   ")
    
    if is_member == False:
        print("       Daftar member sekarang untuk mendapatkan diskon 15%!     ")
    
    print("=" * 65)
    print()
    
    transaksi_baru = input("Apakah Anda ingin memulai transaksi baru? (y/n): ")
    
    if transaksi_baru == "Y":
        transaksi_baru = "y"
    elif transaksi_baru == "N":
        transaksi_baru = "n"
    if transaksi_baru == "y":
        lanjut_program = True
    else:
        os.system('cls || clear')
        print()
        print("=" * 65)
        print("|              TERIMA KASIH TELAH BERBELANJA!                   |")
        print("|                  SAMPAI JUMPA KEMBALI!                        |")
        print("=" * 65)
        print()
        lanjut_program = False