def konversi_mata_uang(nominal, tipe):
    tipe_uang = {'dollar': 13500, 'ringgit': 22000, 'yen': 120, 'real': 4500, 'euro': 12000}
    hasil = nominal / tipe_uang[tipe]
    return hasil

print("Hasil konversi:")
print("1.000.000 rupiah ke dollar   :", konversi_mata_uang(1000000, 'dollar'))
print("1.000.000 rupiah ke ringgit  :", konversi_mata_uang(1000000, 'ringgit'))
print("1.000.000 rupiah ke yen      :", konversi_mata_uang(1000000, 'yen'))
print("1.000.000 rupiah ke real     :", konversi_mata_uang(1000000, 'real'))
print("1.000.000 rupiah ke euro     :", konversi_mata_uang(1000000, 'euro'))