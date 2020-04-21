istenen = input("İstedğiniz basamak sayısını giriniz : ")
c = int(istenen)
try :
    b = int(istenen)
    b += 4
except ValueError :
    print("Lütfen sayı giriniz")

for a in range(1,int(istenen)+1,2) :
    c -= 1
    print(" " * c, "*" * a )  

for d in range(1,int((int(istenen)+1)/2),2) :
    print(" " * (int(istenen)-3) , " | | " )