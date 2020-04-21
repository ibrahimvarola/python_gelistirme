istenen = input("İstedğiniz basamak sayısını giriniz : ")

try :
    c = int(istenen)
    
except ValueError :
    print("Lütfen sayı giriniz")
    exit()

for a in range(1,int(istenen)+1,2) :
    c -= 1
    print(" " * c, "*" * a )  

for d in range(1,int((int(istenen)+1)/2),2) :
    print(" " * (int(istenen)-3) , " | | " )