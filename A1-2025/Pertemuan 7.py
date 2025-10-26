# def perkenalan():
#     print ('mata kuliah')
#     print('kalkuus')
# x = 5*5
# def perkalian():
#     x = 5 * 3
#     print(x)

# perkalian()

# def perkenalan (nama):
#     print(nama)

# perkenalan('gea')

# def luaspersegipanjang(panjang,lebar):
#     luas = panjang * lebar
# print (f'luas dari persegi panjang adalah {luas}')

# luaspersegipanjang('5,3')

# def luaspersegi(sisi):
#     luas = sisi*sisi
#     return luas
# print ('luas dari persegi adalah' (luas persegi (8)))

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print ("Volume Persegi = ", volume)
# luas_persegi(4)
# volume_persegi(8)

# def faktorial(n):
#     # Basis (Base Case): Kondisi berhenti
#     if n == 1 or n == 0:
#         return 1
#     # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# # Memanggil fungsi
# hasil = faktorial(5)
# print(f"Hasil dari 5! adalah: {hasil}")

# fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")
#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")

# # Fungsi untuk menampilkan semua data
# film = []
# def show_data():
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#     for indeks in range(len(film)):
#         print(indeks, "|", film[indeks])

# # Fungsi untuk menambah data
# def insert_data():
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")

# # Fungsi untuk mengedit data
# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")

#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")

# # Fungsi untuk menghapus data
# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         film.remove(film[indeks])
#         print("Film berhasil dihapus!")

# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")

#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     else:
#         print('Tidak ada di menu')


# while True:
#     show_menu()

# harga = (input('masukan harga'))
# print(harga)

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else:
#     print(angka)

# try:
#     usn = input('Username yang diinginkan : ')
#     if len(usn) < 5:
#         raise ValueError('Nama Minimal Memiliki 5 karakter')
# except ValueError as e:
#         print(e)
# else:
#     print(usn)

# Studi Kasus 2: Error Handling untuk Input Password
# Kriteria: Minimal 8 karakter dan wajib ada angka


try:
    password = input("\ninput password: ")
    pavalid = len(password) >= 8
    aangka = False
    for karakter in password:
        if karakter.isdigit():
            aangka = True
            break
    if not pavalid and not aangka:
        raise ValueError("Password tidak memenuhi 2 kriteria:\n- Panjang password kurang dari 8 karakter\n- Tidak mengandung angka")
    elif not pavalid:
        raise ValueError("Password terlalu pendek! Minimal 8 karakter")
    elif not aangka:
        raise ValueError("Password harus mengandung minimal 1 angka")
except ValueError as e:
    print("ERROR!")
    print(f"salah {e}")
    
else:
    print("SUKSES!")
    print("Password valid! Semua kriteria terpenuhi.")
    
finally:
    print("\nProgram selesai dijalankan")