pandu_apel = 10
pandu_harga = 7000
zami_mangga = 10
zami_harga = 5000

# Total harga kedua nya
total_harga_pandu = pandu_apel * pandu_harga * 0.9
total_harga_zami = zami_mangga * zami_harga * 0.9

# Hasil boolean perbandingan
hasil_boolean = total_harga_pandu >= total_harga_zami

# Hasil total harga yang dipangkatkan dengan angka 2
total_harga_pangkat_2 = total_harga_pandu ** 2
total_harga_zami_pangkat_2 = total_harga_zami ** 2

# Hasil boolean perbandingan apakah total harga buah pandu lebih kecil dari total harga buah milik zami DAN apakah total harga buah keduanya kurang dari 100000
hasil_boolean_bandingan_kedua = total_harga_pandu < total_harga_zami and total_harga_pandu + total_harga_zami < 100000

# Mencetak hasil
print('-----------------------------------------------------------')
print(f"Total harga Pandu                          : {total_harga_pandu}")
print(f"Total harga Zami                           : {total_harga_zami}")
print(f"Hasil boolean perbandingan                 : {hasil_boolean}")
print(f"Total harga pangkat 2 Pandu                : {total_harga_pangkat_2}")
print(f"Total harga pangkat 2 Zami                 : {total_harga_zami_pangkat_2}")
print(f"Hasil boolean perbandingan bandingan kedua : {hasil_boolean_bandingan_kedua}")
print('------------------------------------------------------------')