LemariUna = ["One Piece", "Koe No Katachi", "Kimi No Nawa", "Jujutsu kaisen", "Naruto", 'Boruto', "Spirited Away", "Spy x Family", "No Game No Life"]

print()
print("---------------------------")
print("Rak yang bernilai ganjil:")
for i in range(len(LemariUna)):
    if i % 2 != 0:
        print(i, LemariUna[i])
print("---------------------------")
print("Rak yang bernilai genap:")
for i in range(len(LemariUna)):
    if i % 2 == 0:
        print(i, LemariUna[i])
print("---------------------------")



