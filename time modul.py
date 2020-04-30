import time

#time 1970 yılından beri geçen süreyi saniye cinsinden ekrana yazdırır
# Bir işe yaramıyor gibi görünebilir ama belirli komutlarla işimize yarar hale getirebiliyoruz.
zaman = time.time()
print(zaman)


#localtime biraz önce kullandığımız time.time() verisini parametre olarak girdiğimizde 
#bu program parçasının çalıştığı zamanı bize vermektedir
simdiki = time.localtime(zaman)
print(simdiki)


#asctime bir önceki çıktı biraz karmaşık durabilir. Bunu daha düzgün bir hale getirmek için kullanıyoruz
print(time.asctime(simdiki))


#ctime ile üstteki işlemleri yapmaya gerek kalmadan okunabilir zaman çıktısınız alabilirisiniz
print(time.ctime())



#clock programın çalışma süresini saniye cinsinden ekrana yazdırır
print(time.clock())


#sleep saniye cinsinden bekleme yapmamızı sağlar
time.sleep(1)


