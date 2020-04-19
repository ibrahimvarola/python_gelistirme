istenen = int(input("Faktoriyeli hesaplanacak sayıyı giriniz : "))

faktoriyel = 1 

for a in range(1,istenen+1) :
    faktoriyel *= a

print("Sonuç : ",faktoriyel)    