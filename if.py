k_ad = "ibrahimvarola"
sifre = "123456"

#giris_kad = input("kullanıcı adını giriniz: ")
if (input("kullanıcı adını giriniz: ") == k_ad) & (input("şifreyi giriniz: ") == sifre):
    print("""Hoşgeldiniz {}
Bugün neler yapmak isterseniz? 
    """.format(k_ad))

else:
    print("Kullanıcı adı veya şifre hatalı!")