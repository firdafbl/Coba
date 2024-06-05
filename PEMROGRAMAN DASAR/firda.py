#PAKAI FUNGSI   
def LemariUna(*LemariUna):
      for i in range(len(LemariUna)):
       if i % 2 == 0:
        print(i, LemariUna[i], "adalah buku genap")
       else:
        print(i, LemariUna[i], "adalah buku ganjil")
        

LemariUna("One Piece", "Koe No Katachi", "Kimi No Nawa", "Jujutsu kaisen", "Naruto", 'Boruto', "Spirited Away", "Spy x Family", "No Game No Life")




