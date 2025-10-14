#ini list nama nama pemain yang terjebak dan harus melewati game dead or alive
pemain = ["Arisu", "Karube", "Chota", "Shibuki", "Gadis SMA"]
#ini list status para pemain jadi kita bisa tau siapa aja yang masih hidup dan yang sudah tewas
statuspemain = ["hidup", "hidup", "hidup", "hidup", "hidup"]

#ini list ruangan yang harus dilewati pemain untuk memenangkan permainan
ruangan = [
    "Ruang Lift",
    "Koridor Gelap", 
    "Ruang Penyimpanan",
    "Tangga Darurat",
    "Pintu Keluar"
]
#ini pakai tuple untuk jawaban benar setiap ruangan karena jawaban ini sudah pasti dan tidak akan diganti lagi
jawaban = ("DEATH", "LIVE", "DEATH", "LIVE", "DEATH")
#set ini dipakai buat nyimpan ruangan yang sudah dilewati pemain jadi tidak akan terulang lagi
ruangan_dikunjungi = set()

ruangan_sekarang = 0 #maksudnya ini si pemain itu ulau dari index 0 yaitu ruang lift
jumlah_ruangan = 5 #total ruangan yang harus dilewati pemain
pemain_hidup_total = 5 #awalnya semua pemain masih hidup kan pemainnya ada 5 jadi total yang hidup di awal ada 5
salah = 0 
benar = 0
gadis_sma_tewas = False #ini khusus buat kasus gadis sma di index 4 yang tewas di ruangan pertama

#ini itu tampilan awal game nya
print("\n" + "="*40)
print("|         ALICE IN BORDERLAND          |")
print("|    THREE OF CLUBS: DEAD OR ALIVE     |")
print("="*40)
# ini daftar pemain beserta deskripsi pekerjaannya
print("\nPemain:")
print("- Arisu (Gamer)")
print("- Karube (Bartender)")
print("- Chota (pegawai IT)")
print("- Shibuki (Veteran)")
print("- Gadis SMA (Siswi SMA)")

game_berjalan = True
# loop utama dalam game ini yang akan terus berjalan selama game_berjalan = true dan akan berhenti kalau game_berjalan = false yang berarti menang atau kalah si pemain
while game_berjalan:
    #ini buat nampilin status dari pemainnya
    print("\n=== STATUS PEMAIN SAAT INI===")
    #ini loop untuk kita cek setiap pemain (i = 0 sampai 4)
    for i in range(len(pemain)):
        if statuspemain[i] == "hidup":
            print(f"[O] {pemain[i]}") #jadi kalau pemain selamat maka akan keluar output [O] nama pemain
        else:
            print(f"[X] {pemain[i]} (tewas)") #kalau ini jika pemain gagal maka akan keluar output [X] nama pemain dan keterangan Tewas
    print()
    
    #ini tampilan info ruangannya
    nama_ruangan = ruangan[ruangan_sekarang]
    
    #ini dipakai buat ambil nama ruangan sesuai dengan index ruangan_sekarang
    print(f"\n>>> RUANGAN {ruangan_sekarang + 1}: {nama_ruangan}")
    print("TIME LIMIT: 2:00")
    print("CHOOSE THE CORRECT DOOR")
    print("CONFIRM VIA DEVICE")
    print("1. LIVE")
    print("2. DEATH")
    
    pilihan_valid = False
    while not pilihan_valid: #loop while ini akan jalan terus selama pilihan_valid = false
        pilih = input("\nMasukkan pilihan (1 atau 2): ") #nah disini pemain diminta kasih input 1 yaitu pintu live atau 2 untuk pintu death
        
        if pilih == "1":
            pilihan = "LIVE"
            pilihan_valid = True
        elif pilih == "2":
            pilihan = "DEATH"
            pilihan_valid = True
        else:
            print("Pilih pintu yang benar!")
    
    benar_jawaban = jawaban[ruangan_sekarang] #ini buat cek jawabannya benar atau salah berdasarkan tuple di line 15
    
    if pilihan == benar_jawaban:
        print("\n[BENAR] Pintu terbuka dengan aman!") #muncul output pintu terbuka dengan aman kalau pintu yang dipilih benar
        ruangan_dikunjungi.add(ruangan_sekarang) #kita tambahkan ruangannya ke set ruangan_dikunjungi
        ruangan_sekarang += 1 #naik ke ruangan berikutnya
        benar += 1
    else:
        print("\n[SALAH] Jebakan aktif!") #muncul output jebakan aktif! apabila pemain memilih pintu yang salah
        salah += 1
        
        # ini case kusus menikuti alur cerita yang dimau dan hanya terjadi kalau masih diruangan indeks 0 dan gadis sma masih hidup
        if ruangan_sekarang == 0 and statuspemain[4] == "hidup" and not gadis_sma_tewas:
            statuspemain[4] = "mati"
            gadis_sma_tewas = True
            print("\n>>> Gadis SMA itu panik dan berlari ke pintu LIVE!")
            print(">>> LASER MENEMBAK!")
            print(">>> Gadis SMA itu telah TEWAS!")
    
    # ini perhitungan total pemain yang masih hidup
    jumlah_hidup = 0
    for i in range(len(statuspemain)):
        if statuspemain[i] == "hidup":
            jumlah_hidup += 1
    pemain_hidup_total = jumlah_hidup
    
    #disini kita menghitung pemain utama yang masih bertahan
    pemain_utama_hidup = 0
    for i in range(4): 
        if statuspemain[i] == "hidup":
            pemain_utama_hidup += 1
    
    #disini kita cek kondisinya apakah menang atau kalah
    if pemain_utama_hidup == 0: #semua pemain mati
        kondisi = "KALAH"
        game_berjalan = False
    elif ruangan_sekarang >= jumlah_ruangan: #pemain sudah sampai / berhasil melewati ruangan terakhir
        kondisi = "MENANG"
        game_berjalan = False
    else:
        kondisi = "LANJUT"
print("\n" + "="*40)

# ini yang muncul di hp nya pemain pada saat sebelum ending
if kondisi == "MENANG":
    print("|             GAME CLEAR               |")
    print("|      DEAD OR ALIVE - COMPLETED       |")
    print("|     DIFFICULTY: THREE OF CLUBS       |")
    print("|        REWARD: +3 DAYS VISA          |")
    print(f"|       PLAYERS SURVIVED: {pemain_hidup_total}/5          |") 
    print("|          CARD OBTAINED: 3            |")
if kondisi == "KALAH":
    print("|              GAME OVER               |")
    print("|        ALL PLAYERS ARE DEAD          |")

print("="*40)