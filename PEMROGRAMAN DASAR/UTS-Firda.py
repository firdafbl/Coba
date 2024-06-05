# Mencari luas balok tanpa tutup :
def luas_balok_tanpa_tutup(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

panjang = 5
lebar = 4
tinggi = 3

luas = luas_balok_tanpa_tutup(panjang, lebar, tinggi)
print("-------------------------------------------------------")
print(f"Luas permukaan balok tanpa tutup    : {luas} unit persegi")
print()

# Mencari keliling balok tanpa tutup :
def keliling_balok_tanpa_tutup(panjang, lebar, tinggi):
    return 4 * (panjang + lebar + tinggi)

panjang = 5
lebar = 4
tinggi = 3

keliling = keliling_balok_tanpa_tutup(panjang, lebar, tinggi)
print(f"Keliling balok tanpa tutup          : {keliling} unit")
print("-------------------------------------------------------")