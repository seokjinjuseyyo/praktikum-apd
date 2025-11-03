# import math
# from math import sqrt
# import math as m

# import math
# print(math.sqrt(16))
# print(math.factorial(4))

# import random
# print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4
# pilih_acak = ["pisang", "rambutan", "manggis"]
# acak = "apcb"
# print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
# print(random.choice(acak)) # memilih 1 karakter acak pada string
# memasukkan satu persatu nilai dari kumpulan_angka
# ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
# kumpulan_angka = "1234567890"
# hasil = ""
# for i in range(4):
#     hasil += random.choice(kumpulan_angka)
# print(hasil)

# acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
# random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang
# print(acak_kartu)

# from prettytable import PrettyTable
# table = PrettyTable()

# table.fields_names = ["NIM", "Nama", "prodi"]
# table.add_row(['092', 'seokjin', 'ganteng'])
# table.add_row(['097', 'jungkook', 'keren'])
# print (table.get_string(sortby="Nama"))

# import inquirer
# # deklarasi struktur dictionary
# data = {
#     'nama': [],
#     'nim': [],
#     'no_hp': []
# }
# def tambahData():
#     questions = [
#         inquirer.Text('nama', message="Input nama mu"),
#         inquirer.Text('nim', message="Input NIM kamu"),
#         inquirer.Text('no_hp', message="Input nomor hp kamu",)
# # hasil dari semua input diatas adalah:
# # {'name': 'nilai dari input name', 'nim': 'nilai dari input nim',
# ]
#     answers = inquirer.prompt(questions) # hasil input akan disimpan ke
# # tambahkan isi dari list, sesuai key nya masing-masing
#     data['nama'].append(answers['nama'])
#     data['nim'].append(answers['nim'])
#     data['no_hp'].append(answers['no_hp'])
# # panggil fungsi
# tambahData()
# # contoh jika ingin melihat isi dari dictionary data dengan key 'nama'
# print(f"List nama:")
# for i, nama in enumerate(data['nama']):
#         print(f"{i+1}. {nama}") 

import func as nf

def main():
    while true:
        load()
        mood = input('\nBagaimana mood kalian hari ini')
        print