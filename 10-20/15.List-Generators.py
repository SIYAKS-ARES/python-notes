sayilar = list(range(1, 20, 2))
# Aynı durum "list" gibi "tuple" ve "set" için de geçerlidir lakin "dictionary" için geçerli değildir çünkü "key" ve "value" olmadığı için hata verir.

sayilar2 = [i for i in range(1, 20, 2)]

sayilar3 = [i**2 for i in range(1, 20, 2)]

sayilar4 = [{str(i):i**2} for i in range(1, 20, 2)] # Bu şekilde ise "dictionary" oluşturulabilir. "key" değerlerini string olarak kaydetiyoruz.

ayiklanacak_liste = ["a", 1, 2, 3, 4, "b", 5, 6, 7, "c", 8, 9]

# integer_liste = [i for i in ayiklanacak_liste] bu şekilde liste kopyalanır.
integer_liste = [i for i in ayiklanacak_liste if str(i).isdigit()] # Bu şekilde listemizi bütün karakterlerden arındırmış oluyoruz.

sifreler = ["alibahadir.", "masdj.asd", "123nasd", "sakpdap231", "asdan.asdnajd", "msh.1234"]

filitreli_liste = [i for i in sifreler if i.__contains__(".")] # Bu şekilde veya
filitreli_liste2 = [i for i in sifreler if "." in i] # Bu şekilde sadece içerisinde "." olan şifreler ayıklanır.
filitreli_liste3 = [i for i in sifreler if len(i) >= 8] # Bu şekilde sadece sekiz karakter ve üstü olan şifreler ayıklanır.

matrix_1th_line = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matrix_2th_line = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

matrix_final = [[i, k] for i in matrix_1th_line for k in matrix_2th_line]

myList = [i**2 if i >5 else i*i for i in range(10)] # "for" dan önce olursa değere sonra olursa listeye müdahele etmiş oluruz.

# PS: "range" fonksiyonu da bir liste oluşturur.

print(sayilar)
print(sayilar2)
print(sayilar3)
print(sayilar4)
print(integer_liste)
print(filitreli_liste)
print(filitreli_liste2)
print(filitreli_liste3)
print(matrix_final)
print(myList)





