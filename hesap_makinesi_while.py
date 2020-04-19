giriş = """
1- Topla
2- Çııkar
3- Çarp
4- Böl
5- Kare Hesapla
6- Karekök Hesapla
q- Çıkış
"""
while True:
    
    print(giriş)
    soru = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")

    if soru == "1":
        sayi1 = int(input("Lütfen birinci sayıyı giriniz: "))
        sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        print (sayi1, "+", sayi2, "=", sayi1+sayi2)

    elif soru == "2":  
        sayi1 = int(input("Lütfen birinci sayıyı giriniz: "))
        sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        print (sayi1, "-", sayi2, "=", sayi1-sayi2)

    elif soru == "3":
        sayi1 = int(input("Lütfen birinci sayıyı giriniz: "))
        sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        print (sayi1, "*", sayi2, "=", sayi1*sayi2)

    elif soru == "4":
        sayi1 = int(input("Lütfen birinci sayıyı giriniz: "))
        sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        print (sayi1, "/", sayi2, "=", sayi1/sayi2)

    elif soru == "5":
        sayi1 = int(input("Lütfen karesi alınacak sayıyı giriniz: "))
        print (sayi1, "^ 2 =", sayi1 ** 2)

    elif soru == "6":
        sayi1 = int(input("Lütfen karekökü alınacak sayıyı giriniz: "))
        print (sayi1, "^ 0.5 =", sayi1 ** 0.5)
    
    elif soru == "q":
        print("Çıkış yapılıyor...")
        break 

    else:
        print("Yanlış giriş.")