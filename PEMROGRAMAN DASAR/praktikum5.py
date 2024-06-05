# perulangan(looping) = akan trs berulang selama syarat yg diminta masih terpenuhi.
#contoh looping while:
i = 1             #i=index

while i < 6:
    print(i)
    i += 1       #untuk memberhentikan dan mengurutkan angka
print()

i = 0
while i < 5:
    i += 1       
    print("Firda cantikk")

print("Looping telah selesai")
print()

#loop dgn while
n = 1

while n <= 5:     #jika n>=5 tdk akan jln krn n=1
    print (f"Angka ke-{n}")
    n += 1        #increment supaya loop tdk berjalan

print("Loop while telah sukses")
print()

n = 10

while n >= 1:    
    print (f"Angka ke-{n}")
    n -= 1        #maka hasilnya akan dikurang, 10,9,8,7

print("Loop while telah sukses 2")
print()

n = 10

while n >= 1:    
    print (f"Angka ke-{n}")
    n -= 1        
    if n== 7:
        break       #ketika masuk di angka ketiga dan seterusnya otomatis ke cut
        #continue    #
        #pass        #hanya sbg 

print("Loop while telah sukses 3")

#for => bisa mengulang beberapa loop jd kita tau brp
#menginterasi string
for i in "unikama":
    print(i)
print()

nilai = [10, 50, 75, 100, 20]
for i in nilai:
    print(i)
print()

nilai = [10, 50, 75, 100, 20]
buah = ["apel", "durian", "pisang", "nangka"]

for i in buah:
    if i == "durian":
        break
    print(i)

print("Proses interasi selesai2!")
print()

#range dgn 1 argumen
for x in range(10):
    print(x)
print()

#range dgn 2 argumen
for x in range(2, 5):  #mulainya dr angka 1
   print(x)
print()

#range dgn 3 argumen
for x in range(1, 10, 2):
    print(x)
print()

#NESTED LOOP = sama seperti if tp yg mjd fokus utama adlh utk membuat peruangan dlm peruangan, beda penempatan(konotasi)
for outer in ["satu", "dua", "tiga"]:   #outer, variabel yg digunakan
    print(outer)
    for inner in range(1,4):
        print(inner)
        inner += 1

print("Loop telah selesai!")
print()

#PROGRAM SIMPEL PERULANGAN

nAbsen = ["Ferdi", "Sambo", "Pandu", "Nabilla", "Leuna", "Mamat"]
absenCari = input("Masukkan nama mahasisxwa :")

i = 0
while i < len(nAbsen):  #menghitung pjg dr variabel nabsen
    if nAbsen[i].lower() == absenCari.lower():  #lower utk lihat absencari ada di nabsen apa nggk
        print("Nama ketemu di index", i)
        break
    
    print("Bukan", nAbsen[i])
    i += 1

else:
    print('Maaf, nama absen yang anda cari tidak ditemukan')
print()

#menampilkan bilangan ganjil dan genap
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i, "adalah bilangan genap")
    else:
        print(i, "adalah bilangan ganjil")
    i += 1
print()




