#FUNCTION
def tambah(a,b):
    print(a+b)  #nmanya parameter

tambah(5,5)
print()

def lemariku(*loker):
    print("Isi di dalam loker : ",loker[2])

lemariku("Baju", "Celana", "Kaos Kaki", "Tas", "Topi")
print()

def lemariku(*loker):
    return loker[4] #return utk mjd value

print(lemariku("Baju", "Celana", "Kaos Kaki", "Tas", "Topi"))
print()

def hitung_rata(a):
    rata_rata = (a/7)*0.15
    return rata_rata

#INI MENGGUNAKAN FUNGSI 
print("Nilai Bambang :", hitung_rata(700))
print("Nilai Zami :", hitung_rata(600))
print()

#INI TDK MENGGUNAKAN FUNGSI
print("Nilai Bambang :", (700/7)*0.15)
print("Nilai Zami :", (600/7)*0.15)
print()

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

def volume_kubus(sisi):
    volume = luas_persegi(sisi)*sisi
    return volume

print(volume_kubus(6))
print()

