class Balok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
    def luas_permukaan(self):
        luas_sisi = 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)
        return luas_sisi
    def keliling(self):
        keliling = 4 * (self.panjang + self.lebar + self.tinggi)
        return keliling

balok1 = Balok(10, 8, 4)

luas_permukaan = balok1.luas_permukaan()
keliling = balok1.keliling()

()
print("--------------------Balok Tanpa Tutup--------------------")
print(f"Balok dengan panjang {balok1.panjang}, lebar {balok1.lebar}, dan tinggi {balok1.tinggi}: ")
print(f"Luas permukaan = {luas_permukaan}")
print(f"Keliling = {keliling}")
print("---------------------------------------------------------")

