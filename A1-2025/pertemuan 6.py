# buah = {"apel", "jeruk", "mangga", "apel"}
# # print(buah)
# for i in bush:
#     print (i, end='')

# angka = [1,1,2,5,2,3,6]

# unik = set(angka)
# print(unik)

# Daftar_buku = {
# "Novel" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }

# print(Daftar_buku["buku1"])
# print(Daftar_buku)

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {"Instagram" : "daffahrhap"}
# }

# for i, j in Biodata.items():
#      print (i)
#      print (j)
#     print (i, j)

# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get("Nama"))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"}
#Sebelum Ditambah
#print(Film)
# Film["Zombieland"] = "Comedy" #jadi yang sebelumnya gak ada jadi nambah dianya
# Film.update({"Hours" : "Thriller"}) #kalau ada key sebelumnya dia nimpa aja jadi gapapa pakai key lama
# #Setelah Ditambah
# print(Film)

# hapus = film('The conjuring')
# print (hapus)

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][0])

# a = {10, 11, 12}
# b = {11, 13, 14}
# c = a | b

# print(c)

#mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# perulangan for untuk mendapatkan semua elemen
# for i in mahasiswa:
#     for j in i :
#         print (j)