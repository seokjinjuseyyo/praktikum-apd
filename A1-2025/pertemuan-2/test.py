print("Ada 3 tipe pilihan kelas yang kami tawarkan kepada anda yakni kelas (1) Utama = Rp10.000.000, kelas (2) Bisnis = Rp5.000.000 kelas (3) ekonomi = Rp2.000.000")
print("Silahkan pilih tipe kelas penerbangan anda")
i = 1
urutan = 1
if i <= 5:
    kelas = int(input())
    if kelas == 1:
        print("Berapa jumlah tiket yang di inginkan")
        penumpang = int(input())
        total = penumpang * 10000000
        for kelas in range(1, 5 + 1, 1):
            print("Kelas Utama seharga Rp" + str(total))
    else:
        if kelas == 2:
            print("Berapa jumlah tiket yang di inginkan")
            penumpang = int(input())
            total = penumpang * 5000000
            while urutan <= penumpang:
                print("kelas Bisnis seharga Rp" + str(total))
                urutan = urutan + 1
        else:
            if kelas == 3:
                print("Berapa jumlah tiket yang di inginkan")
                penumpang = int(input())
                total = penumpang * 2000000
                print("Kelas Ekonomi seharga Rp" + str(total))
            else:
                print("kelas tak tersedia")
    print("Pembayaran anda berhasil. Terimakasih dan sampai jumpa di penerbangan berikutnya")
