
print('\n')
biodata = { 'nama'  : 'Muhammad Irfandy Imran',
'nim'   : '231031121',
'kelas' : 'S123D',
'tempat,tanggal lahir' : 'parepare,25 juli 2005',
'jenis kelamin' : 'laki-laki',
'agama' : 'islam',
'alamat': 'jalan industri kecil no 64',
'email' : 'fandicuteimram@gmail.com'
}

print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:3])
print(selected_biodata)





