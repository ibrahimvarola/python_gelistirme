#sayı tahmin oyunu
import random 

tahmin = input("0-100 arasında bir sayı giriniz : ")
sayi , sayac = random.randrange(0,100) , 1

try :
   b = int(tahmin)
except ValueError :
   print("Lütfen sayı giriniz")
   quit()

while True :
      if int(tahmin) > sayi :
         tahmin = input("Daha küçük bir sayı giriniz : ")
         sayac +=1
      
      elif int(tahmin) < sayi :
         tahmin = input("Daha büyük bir sayı giriniz : ")   
         sayac +=1

      if sayac == 10 :
             print("Üzgünüz 10 denemede bulamadınız")
             exit()

      elif int(tahmin) == sayi :
             print("Tebrikler {} denemede buldunuz".format(sayac))
             break
