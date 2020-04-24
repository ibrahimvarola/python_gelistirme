dizi = "Karakter Dizisi"

#Karakter dizisinin eleman sayısı

print("Karakter sayısı:", len(dizi), "\n")

#Karakter dizisi elemanlarına erişme : 

print(dizi[0])
print(dizi[4])
print(dizi[9], "\n")

#Döngü ile erişim

for i in range(len(dizi)):
    print("Dizinin {}. elemanı= {}" .format(i+1, dizi[i]))
print("\n")

#Karakter dizisini dilimleme: (syntax= karakter_dizisi[alınacak_ilk_öğenin_sırası:alınacak_son_öğenin_sırasının_bir_fazlası])

print(dizi[0:8])
print(dizi[9:15], "\n")

site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"

for isim in site1, site2, site3, site4:
    print("site: ", isim[4:-4])
print("\n")

#Karakter dizisini ters çevirme: (syntax: kardiz[ilk_karakter:son_karakter:atlama_sayısı])

dizi1 = "You don' t know the power of the Dark Side."
print(dizi1[::-1])