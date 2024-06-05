#Logika Percabangan => didlm nya memuat:
#IF(kondisi yg akan di eksekusi oleh)
#jika program bernilai benar atau TRUE

nilai = 3

#jika kondisi benar/TRUE maka program akan mengeksekusi perintah dinawahnya
if (nilai > 7) :
    print("Selamat anda lulus")
else:
    print("Maaf anda tidak lulus")

#dan jika kondisi salah/FALSE maka program tdk akan mengeksekusi perintah dibawahnya


#IF ELSE(bisa membedakan mana yg salah dan mana yg benar)
print()
nilai = int(input("Masukkan nilai anda :"))
print("Nilai anda adalah:", nilai)

if (nilai > 7) :
    print("Selamat anda lulus")
else:
    print("Maaf anda tidak lulus")


#IF ELIF() contoh:

hari_ini = (input("Masukkan Hari : "))
print("yang bisa dilakukan :",hari_ini)

print()
hari_ini = "Minggu"
if(hari_ini == "Senin") :
    print("Saya akan kuliah")
elif(hari_ini == "Selasa") :
    print("Saya akan kuliah")
elif(hari_ini == "Rabu") :
    print("Saya akan kuliah")
elif(hari_ini == "Kamis") :
    print("Saya akan kuliah")
elif(hari_ini == "Jum'at") :
    print("Saya akan kuliah")
elif(hari_ini == "Sabtu") :
    print("Saya akan kuliah")
else:
    print("Saya akan libur")
print()

#penerapan IF ELSE utk studi kasus cuaca
cuaca = input("Masukkan cuaca:")
print("cuaca hari ini :", cuaca)

#penerapan IF ELIF
if cuaca == "Hujan" :
    print("Memakai payung")

elif cuaca == "Cerah" :
    print("Tidak memakai payung")

else:
    print("Memakai pakaian renang")
print()

nilai_a = int(input("Masukkan nilai a :"))
nilai_b = int(input("Masukkan nilai b :"))

if nilai_a > nilai_b :
    print("A lebih besar dari b")
elif nilai_a == nilai_b :
    print("A sama dengan B")
else :
    print("A lebih kecil dari b")
print()

umur = int(input("Masukkan umur anda :"))
bekerja = str(input("Status bekerja? [ya/tidak]"))
pendapatan = int(input("Masukkan pendapatan "))
sekolah = str(input("Status sekolah? [ya/tidak]"))

if (umur >= 18) :
    if(bekerja == "ya") :
        if(pendapatan <= 500000):
            print("Penduduk Kurang Mampu")
        else : 
            print("Penduduk Mampu")
    else:
        if(sekolah == "ya") :
            print("Penduduk Mampu")
        else:
            print("Penduduk Kurang Mampu")
else:
    print()
