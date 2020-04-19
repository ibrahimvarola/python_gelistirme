istenen = int(input("Faktoriyeli hesaplanacak sayıyı giriniz : "))

faktoriyel,sayac = 1,1

while True :
    sayac += 1
    faktoriyel *= sayac
    if sayac == istenen :
        print("Sonuç", faktoriyel, sep=" = ")
        break