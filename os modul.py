import os  # operating system'ın kısaltmasıdır

a = [i for i in dir(os) if "_" not in i] 

#name modulü işletim sisteminin adını verir
print(os.name)
"""
eğer windows işletim sisteminde çalıştırırsanız "nt" yanıtını verecektir
linux dağıtımlarında ise "posix" yanıtı dönmektedir
"""


#getcwd programın açıldığı dizini gösterecektir
print(os.getcwd())


#chdir bulunduğunuz dizinden başka bir dizine gitmenizi sağlar 
os.chdir("/home/berkant/Masaüstü")
print(os.getcwd())


#listdir bulunduğunuz dizin içeriğini listeler
print(os.listdir())


#startfile bulunduğunuz dizindeki bir dosyayı açmanızı sağlar. windows üzerinde çalışır
#                   os.startfile('deneme.txt')


#mkdir istediğiniz bir uzantıyı girerek orada dizin oluşturur 
os.mkdir('/home/berkant/Masaüstü/Yeni Dizin')


#makedirs dizin içerisizinde dizin oluşturmanızı sağlar
os.makedirs('/home/berkant/Masaüstü/Yeni Dizin/Python')


"""
Bu komutu hiçbir değişiklik yapmadan 2 kere çalıştırmayı denediğinizde hata alacaksınız.
Çünkü 2. kez çalıştırdığınızda aynı dizini tekrar oluşturmaya çalışır. Zaten varolduğundan hata verip programdan çıkacaktır.
"""

#rename istediğiniz dizinin adını değiştirmenizi sağlar
os.rename('Yeni Dizin', 'asdd')


#remove adından da anlaşılacağı dizindeki dosyayı silmeyi sağlar. Bunu kullanırken dikkatli olmalısınız.
open("/home/berkant/Masaüstü/asd.txt" , "w")
os.remove('/home/berkant/Masaüstü/asd.txt')


#removedirs ise içi içe fazla dizini silmenizi sağlar. Dizinin boş olmasına dikkat ediniz.
os.removedirs('/home/berkant/Masaüstü/asdd/Python')


#rmdir bulunduğunuz dizinde bir dizin silmenizi sağlar. Dizinin içinin boş olması gerekmektedir.
#                      os.rmdir('/home/berkant/Masaüstü/asdd')


#system python üzerinden bir program çalıştırmanızı sağlar
os.chdir('/home/berkant/Masaüstü')
os.system('nmap')


#path.exists bir dosyanın var olup olmadığını sorgular ve duruma göre true false döndürür
print(os.path.exists("modul")) 


#path.isfile girilen parametreye ait bir dosya var mı yokmu onu kontrol eder. True false döndürür
print(os.path.isfile('İsimsiz Belge'))


#path.isdir ise dizin olup olmadığının kontrolünü yapar.
print(os.path.isdir('Linux Notları'))


#path.join girilen parametreleri bir uzantıya dönüştürür
print(os.path.join("home","berkant","Masaüstü")) # home/berkant/Masaüstü


#path.splitext verilen dosyayı uzantısına göre ayırır
print(os.path.splitext("os modul.py"))


#path.dirname dizinin bulunduğu adresi verir
print(os.path.dirname("/bin/bash")) #çıktısı  ==> /bin


#walk belirttiğiniz dizin içerisindeki her şeyin bir listesini çıkarır
for c in os.walk('/home/berkant/Masaüstü') :
    print(c)
"""
3 elemanlı bir demet çıktısı alınır. 
1. eleman bulunduğunuz dizinin patikası (/home/berkant gibi)
2. eleman Bulunduğunuz dizin içerisindeki dizinleri
3. eleman bulunduğunuz dizindeki dosyaların listesini

sonrasında ise içerisinde bulunnan her dizin için bu işlem tekrarlanır
yani dizinini içerisinde ne kadar dizin varsa bu işlem devam edecektir
"""
