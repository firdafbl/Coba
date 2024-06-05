gaji = int(input("Masukkan gaji pandu :"))
aset1 = (input("Apakah pandu mempunyai aset mobil? [ya/tidak]"))
aset2 = (input("Apakah pandu mempunyai aset motor? [ya/tidak]"))

if (gaji >= 500000) :
    if(aset1 == "ya") :
        if(gaji >= 500000):
            print("Pandu wajib membayar pajak ")
        else:
            print("Pandu tidak wajib pajak ")

if (gaji <= 500000) :
    if(aset2 == "ya") :
        if(gaji <= 500000):
            print("Pandu tidak wajib pajak ")
        else:
            print("Pandu wajib membayar pajak ")

if gaji == 0 and aset1 == "tidak" and aset2 == "tidak":
    print("Pandu masih pelajar")
else:
    print()
    