from abc import ABC, abstractmethod

class Manusia(ABC):

    @abstractmethod
    def Menari(self):
        pass
    
    def berkata(self):
        print("Aku Manusia")

class Jawa(Manusia):
    def Menari(self):
        print("Serimpi")

    def berkata(self):
        super().berkata()
        print("Aku Orang suku Jawa")

class Sunda(Manusia):
    def Menari(self):
        print("Jaipong")

#Orang=Manusia=>tdk bisa dipanggil krn termasuk abstract

Paidi=Jawa()

Paidi.Menari()
Paidi.berkata()

Nenden=Sunda()
Nenden.Menari()

#class abstract=boleh diisi bbrp method spt ortu dan anak
#method abstract=tdk perlu isi