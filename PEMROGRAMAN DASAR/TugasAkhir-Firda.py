print("============= KONVERSI TIPE DATA =============")
print()

def nominal (jumlah):
    angka = jumlah
    panjang = (len(angka))
    hasil = "Rp. "

    for i in range(panjang):
        hasil += angka[i]
        if (panjang - i - 1) % 3 == 0 and i != panjang - 1:
            hasil += "."
    return hasil
while True :
    input_angka = input ("Masukkan nominal :")
    output_rupiah = nominal (input_angka)
    print("Total :", output_rupiah)