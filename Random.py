# bu program "random modulünün kullanışlı methodlarını içermektedir"

import random

a = [i for i in dir(random) if "_" not in i]
#Bu sayede içerisinde "_" bulunan methodlardan kurtuluyoruz
# * içeren methodlar anlatılmıştır
"""
BPF
LOG4
Random
SystemRandom
TWOPI
betavariate
choice *
choices
expovariate
gammavariate
gauss
getrandbits *
getstate
lognormvariate
normalvariate
paretovariate
randint *
random *
randrange *
sample *
seed
setstate
shuffle *
triangular
uniform *
vonmisesvariate
weibullvariate
"""
print(a)

#random methodu rastgele float tipinde sayı seçer
print(random.random(), "\trandom ")

#randint methodu belirttiğiniz aralıkta rastgele int türünde bir sayı seçer
print(random.randint(0,3),"{:<22}randint".format(" "))

#uniform methodu belirttiğiniz aralıkta rastgele bir ondalıklı sayı seçer
print(random.uniform(1,12), "\tuniform")

#randrange methodu belirttiğiniz aralıktan bir sayı seçer (46 dahil değildir)
print(random.randrange(0,46), "{:<15}\trandrange".format(" ") )

#choice methodu bir rastgele seçim yapacaktır
ciftsayilar = [d for d in range(100) if not d%2 ]
print(random.choice(ciftsayilar),"{:<15}\tchoise".format(" "))

#  şu şekilde de kullanılabilir
print(random.choice("qweasdzxc"),"{:<15}\tchoise".format(" "))
print(random.choice([1,"a",3,4]),"{:<15}\tchoise".format(" "))

#sample methodu ile istediğiniz adette rastgele liste elemanı seçebilirsiniz
rakamlar = [1,"g",2,3,4]
print(random.sample(rakamlar,2),"{:<9}\tsample".format(" "))

#shuffle methodu ile elimizdeki diziyi karıştırabiliriz ve bu değişiklikler listeye aktarılır
rakamlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(rakamlar)
print(list(rakamlar),"\tshuffle".format(" "))

#getrandbits parantez içerisinde belirttiğiniz bit sayısına sahip bir sayıyı rastgele verir
#örn. 150 sayısı 8 bittir. 4 sayısı 3 bittir.
print(random.getrandbits(3))

random.SystemRandom(445652)
