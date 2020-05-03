numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)
print(val)

val = max(numbers)
print(val)

#append metodu bir dizinin üzerine veri eklememizi sağlar

numbers.append("deneme")
print(numbers)

#insert metodu dizinin istediğimiz indexine veri yerleştirmemizi sağlar

numbers.insert(1, 78)
print(numbers)

#pop metodu istediğimiz indexteki veriyi siler default olarak son elemanı siler

numbers.pop()
numbers.pop(3)
print(numbers)

#remove metodu istediğimiz veriyi silmemizi sağlar

letters.remove("a")
print(letters)

#sort metodu dizideki verilerin sıralanmasını sağlar

numbers.sort()
letters.sort()

print(numbers)
print(letters)

#reverse metodu dizinin ters çevrilmesini sağlar

#count metodu içine yazılan verinin dizi içinde kaç kez tekrarlandığını verir

#clear metodu dizi içindeki verilerin temizlenmesini sağlar

#index metodu içine yazılan verinin indexini verir