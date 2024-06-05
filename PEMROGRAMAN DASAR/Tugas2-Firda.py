harga_barang = [17000, 24000, 37000]
persentase_diskon = 10

# Menghitung harga setelah diskon untuk setiap barang
harga_setelah_diskon = [(harga - (persentase_diskon / 100) * harga) for harga in harga_barang]

print("--------------------LIST HARGA BUAH---------------------")
print(f"Apel    : Rp. {harga_setelah_diskon[0]:,.2f}")
print(f"Mangga  : Rp. {harga_setelah_diskon[1]:,.2f}")
print(f"Semangka: Rp. {harga_setelah_diskon[2]:,.2f}")
print("---------------------------------------------------------")