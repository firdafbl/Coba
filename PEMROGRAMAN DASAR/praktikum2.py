x = y = z = 5
print(x)
print(y)
print(z)

#Jumlah=6
#Satuan="Orang"
#print(Jumlah + Satuan)  #error krn gabungan int+str

print() #sbg enter
Jumlah=6
Satuan=5
Jalan="kembang"
print(Jumlah+Satuan)
print() #sbg enter
print(Jalan)

print()
data_integer = 1
print("Data :", data_integer)
print("Data ini bertipe :", type(data_integer))
print()

print()
data_string = "Unikama"
print("Kampus :", data_string)
print("Data ini bertipe :", type(data_string))
print()

print()
data_float = 2.5
print("Data :", data_float) #tipe data array berupa list
print("Data ini bertipe :", type(data_float)) #utk memunculkan tipe data di output/terminal
print()

nama_siswa = ["Budi", "Mamad", "Jordi", "Reihan"]
print(nama_siswa)
print(nama_siswa[2])
print(nama_siswa[1])

data_boolean = True
data_boolean = False
print("Data :", data_boolean)
print("Data 2 :", data_boolean)
print("Data ini bertipe :", type(data_boolean)) #bernilai true/false
print()

merk_mobil = {"ferrari", "BMW", "Lamborgini"} #tapel sifatnya tdk dpt diubah, brp kurung kurawal
print(merk_mobil)
print("Data ini bertipe :", type(merk_mobil))
print()

data_duplikat = (1,2,2,3,4,4,5) #tipe data set,untuk mengidentifikasi data duplikat agar hasilnya satu
data_unik = set(data_duplikat)
print(data_unik)
print()

nama_desa = frozenset({"getasrejo", "karangmalang", "siti"})
print(nama_desa)
print("Data ini bertipe :", type(nama_desa))
print()

#aritmatika => (+)=tambah, (-)=kurang, (/)=bagi, (**)=pangkat, (//)=bisa dibagi, (%)=sisa bagi (*)=kali

nama="firda"
umur=19
print(f"Nama saya {nama} umur saya {umur}") #f untuk format/digabung
print()

# Harga barang
harga_barang = [17000, 24000, 37000]

# Persentase diskon
persentase_diskon = 10

# Menghitung harga setelah diskon untuk setiap barang
harga_setelah_diskon = [(harga - (persentase_diskon / 100) * harga) for harga in harga_barang]

print("--------------------LIST HARGA BUAH---------------------")
print(f"Apel: Rp. {harga_setelah_diskon[0]:,.2f}")
print(f"Mangga: Rp. {harga_setelah_diskon[1]:,.2f}")
print(f"Semangka: Rp. {harga_setelah_diskon[2]:,.2f}")
print("---------------------------------------------------------")