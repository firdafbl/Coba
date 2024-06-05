from abc import ABC, abstractmethod

class Bentuk(ABC):

    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

class persegi_panjang(Bentuk):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    def luas(self):
        return self.panjang * self.lebar
    def keliling(self):
        return 2 * self.panjang + self.lebar

P1 = persegi_panjang(10,8) 
print ("Luas persegi panjang:", P1.luas())
print ("Keliling persegi panjang:", P1.keliling())

#class yg tdk ada @abstractmethod nya = abstrak
#class yg ada @abstractmethod nya = interface
#def __init__ = constructor
#pass = tidak ada kode untuk dieksekusi
#def = membuat suatu fungsi
#constructor = fungsi anggota kelas yg namnya sama dgn kelas utama