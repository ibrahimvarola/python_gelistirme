#-*-coding=UTF 8 -*-
#asal sayı kontrolü
import sys

if sys.version_info.major < 3 :
    print("Python versiyonunuz = {}.{} \nLütfen 3.x üstünde çalıştırınız".format(sys.version_info.major,sys.version_info.minor))
    quit()

d = 0
a = input("Sayı giriniz : ")

try :
    b = int(a)
except ValueError :
    print("Sayı girmelisiniz")
    quit()

for c in range(1,int(a)+1) :
    if int(a)%c == 0 :
        d += 1

if d == 2 :
    print("Sayı asal")
else :
    print("Asal değil")
