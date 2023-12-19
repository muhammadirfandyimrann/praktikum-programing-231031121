a = [2,3,1,0,3,1,1,2,1]
    #0,1,2,3,4,5,6,7,8
    #-9,-8,-7,-6,-5,-4,-3,-2,-1

#akses item
print(a)
print(f'item indeks:0 {a[0]}')
print(f'item indeks:3 {a[3]}')
print(f'item indeks:terakhir {a[len(a)-1]}')

#akses item indeks negatif
print(f'item indeks:terakhir(-1) {a[-1]}')
print(f'item indeks:pertama (-9) {a[-len(a)]}')
print(f'item indeks:1 -8 {a[-8]}')
print(f'item indeks:5 -4 {a[-4]}')

#indeks batas
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:1,2... {a[1:]}')
print(f'item indeks:3,4... {a[3:]}')
print(f'item indeks:0,1,2,3,4 {a[:5]}')
print(f'item indeks:semua {a[:]}')

#pengirisan indeks
print(f'item indeks:1,2,3 {a[1:4]}')
print(f'item indeks:2,3,4 {a[2:5]}')
print(f'item indeks:[1:8]{a[1:-1]}')

#nested list
kelas = [('kaldas1',3),
         ('bahasa',2),
        ('pemrograman',3)]
print(f'data kelas {kelas}')
kelas.append(('cinta',2))
print(f'data kelas {kelas}')

#nama mata kuliah 1: kaldas1 dengan jumlah sks: 3
#nama mata kuliah 2: Bahasa dengan jumlah sks: 2
#nama mata kuliah 3: pemrograman dengan jumlah sks: 3
#nama mata kuliah 4: cinta dengan jumlah sks: 2

print('\nTUGAS PRAKTIKUM-D4')

data = [('Muhammad Irfandy imran',2023,'Aktif'),
        (90,88,93,89,100),
        (20,22),
        ('S1-Reguler','Sistem Informasi D','Ganjil')]
# Nama Mahasiswa: Muhammad Irfandy imran
print(f'Nama Mahasiswa: {data[0][0]}')

# NIM Mahasiswa: 231031121
print(f'NIM Mahasiswa: {a[0]}{a[1]}{a[2]}{a[3]}{a[4]}{a[5]}{a[6]}{a[7]}{a[8]}')

# Program pendidikan : Sistem Informasi D S1-Reguler
print(f'Program Pendidikan: {data[3][1]} {data[3][0]}')

# Angkatan: 2023-Ganjil
print(f'Angkatan: {data[0][1]}-{data[-1][-1]}')

# Jumlah nilai Muhammad Irfandy imran adalah
print(f'Jumlah Nilai Muhammad Irfandy imran adalah: {len(data[1])}')

# Data terbesar Muhammad Irfandy imran adalah
print(f'Data Terbesar Muhammad Irfandy imran Adalah: {max(data[1])}')

# Data Terkecil adalah
print(f'Data Terkecil Muhammad Irfandy imran Adalah: {min(data[1])}')

# Rata-Rata nilai adalah
rata= sum(data[1])/len(data[1])
print(f'Rata-rata Nilai Muhammad Irfandy imran adalah: {rata}')
