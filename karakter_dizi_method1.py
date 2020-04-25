#replace() metodu (syntax= karakter_dizisi.replace(eski_karakter_dizisi, yeni_karakter_dizisi, degistirilecek_krktr_sayisi))

dizi1 = "ibrahim"
print(dizi1.replace("i", "İ", 1), "\n")

#split(), rsplit(), splitlines() metodları

dizi2 = "Türkiye Büyük Millet Meclisi"
print(dizi2.split(), "\n")

for i in dizi2.split():
    print(i)

for i in dizi2.split():
    print(i[0], end="")
print("\n")

dizi3 = "elma, armut, kavun, karpuz, ayva"
for i in dizi3.split(", "):
    print(i)
