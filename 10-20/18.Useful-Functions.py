################################################################

# ZIP FUNCTION

# Verilen iki listenin de tüm elemanlarını gezerek bir tuple oluşturur.

xZip = [1,2,3,4,5,6,7,8,9]
yZip = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

z = list(zip(xZip, yZip)) # Eğer girilen listelerin uzunlukları eşit olmazsa karşılığı olmayan elemanı göstermez.
t = dict(zip(xZip, yZip)) # Dönüştürmede çoğunlukla liste olarak değil, key ve value bileşenlerine sahip olan dictionary kullanılır.


print(z)
print(t)

################################################################

# MAP FUNCTIONS

'''Fonksiyonel proglamanın önemli fonksiyonlarından biri olan MAP fonksiyonu,
önceden çoklu verileri depolamak için (listeler, setler, kümeler) kullanmıştık, şimdi ise fonksiyonlar ile harmanlanarak kullanılacak.
MAP fonksiyonu, verilen nesneyi verilen fonksiyona uygular ve sonucu bir map objesi olarak döndürür.
'''
print("Before MAP")
xMap = [1, 2, 4, 8, 12, 7, 5]
yMap = [3, 6, 9, 12, 15, 18, 21]

def kareAl(sayi):
    return sayi ** 2

for i in xMap:
    print(kareAl(i))

# Önceden bu şekilde kareAl ve for yazarak listenin tüm elemanlarının karesi alınıp yazdırılırdı. Şimdi bunu MAP kullanarak yapalım.

print("After MAP")

# newList = set(map(kareAl, x))
newList = list(map(kareAl, xMap)) # MAP fonksiyonu kodun okunabilirliğini arttırır.

# Kısa olan fonksiyonları "lamda" kullanarak da MAP fonskiyonunun içine yazabiliriz.
# newList2 = list(map(lambda n : n**2, xMap))
newList2 = list(map(lambda n : n**2, [1, 2, 4, 8, 12, 7, 5])) # Bu şekilde tek satırda kod toparlanabilir.

# İki adet nesne verileceği zaman,

def topla(num1, num2):
    return num1 + num2

# newList3 = list(map(topla, xMap, yMap))
newList3 = list(map(lambda n,m: n + m, xMap, yMap)) # Lamda kullanılarak yapılan hali.

print(newList)
print(newList2)
print(newList3)

##############################################################

# FILTER FUNCTION

'''FILTER fonksiyonu, verilen true-false döndüren bir fonksiyonun ve iterable edilebilen koşulu
sağlayan elemanları yeni bir veri setine kaydeder.
'''

'''
FILTER fonksiyonu, verilen true-false döndüren bir fonksiyonun ve iterable edilebilen veri kümesinin koşulu
sağlayan elemanlarından oluşan yeni bir veri kümesi oluşturur.
'''

xFilter = [1, 2, 4, 8, 12, 7, 5]
yFilter = [3, 6, 9, 12, 15, 18, 21]

def ciftMi(sayi):
    return True if  sayi % 2 == 0 else False

m = list(filter(ciftMi, xFilter))
n = list(filter(lambda n : n % 2 == 0, yFilter)) # Lamda kullanılarak yapılan hali.
hataliSifreler = list(filter(lambda n: n.__contains__(".") or n.__contains__("?"), ["msH,aasd123", "sauhasSf.234", "ASfhasuo?"]))

print(m)
print(n)
print(hataliSifreler)
