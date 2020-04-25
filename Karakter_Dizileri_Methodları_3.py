a = "ece"
b = "kavak"
# strip() methodu belirtilen ifadeyi başında ve sonunds keser

print(a.strip("e")) # Çıktı ==> c

# lstrip() methodu da aynı işlevi görmektedir fakat sadece soldan kesme yapacaktır

print(b.lstrip("k")) # Çıktı ==> avak

#rstrip ise sağdan kesecektir

print("asdfg".strip("g")) # Çıktı ==> asdf
