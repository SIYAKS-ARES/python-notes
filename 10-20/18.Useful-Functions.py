################################################################

# ZIP FUNCTION

# Verilen iki listenin de tüm elemanlarını gezerek bir tuple oluşturur.

from sympy import reduced

xZip = [1,2,3,4,5,6,7,8,9]
yZip = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

z = list(zip(xZip, yZip)) # Eğer girilen listelerin uzunlukları eşit olmazsa karşılığı olmayan elemanı göstermez.
t = dict(zip(xZip, yZip)) # Dönüştürmede çoğunlukla liste olarak değil, key ve value bileşenlerine sahip olan dictionary kullanılır.

print(z)
print(t)

###############################################################

# MAP FUNCTIONS

'''
Fonksiyonel proglamanın önemli fonksiyonlarından biri olan MAP fonksiyonu,
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

# FILTER fonksiyonu, verilen true-false döndüren bir fonksiyonun ve iterable edilebilen koşulu sağlayan elemanları yeni bir veri setine kaydeder.

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

#############################################################

from functools import reduce

# REDUCE FUNCTION

'''REDUCE fonksiyonu bir tane fonksiyon ve iterable edilebilen veri kümesi alır ardından sadece tek bir sonuç verir.
Bunu elemanları eksilterek, kendinde toplayarak yapar.
'''

lst = [12, 46, 54, 62, 7634, 8324, 966, 810]

def topla2(sayi1, sayi2):
    return sayi1 + sayi2

print(reduce(topla2, lst))
# sayi1 ile sayi2'yi toplar ardından sonucu sayi1'e atar ve sıradaki sayıyı sayi2'ye atayarak devam eder. Ve son sonucu verir.

print(reduce(lambda n, m: n + m, [12, 46, 54, 62, 7634, 8324, 966, 810])) # Lamda kullanılarak yapılan hali.

#############################################################

# REDUCE FUNCTION

# REDUCE fonksiyonu, verilen iterable edilebilen veri kümesinin elemanlarını birbirinden bir sonraki elemanla toplayarak bir sonuç elde eder.

xReduce = [1, 2, 4, 8, 12, 7, 5]

def carp(sayi1, sayi2):
    return sayi1 * sayi2

print(reduce(topla2, xReduce))
print(reduce(carp, xReduce))
# `reduce` is not suitable for `ciftMi2` and `kareAl2` since they do not combine two values.
# Hence, providing alternative meaningful `reduce` examples.

#############################################################

# ALL FUNCTION

'''ALL fonksiyonu, verilen iterable edilebilen veri kümesinin tüm elemanlarına true döndüren bir fonksiyonun
sonucunu döndürür.
'''

xAll = [1, 2, 4, 8, 12, 7, 5]
yAll = [3, 6, 9, 12, 15, 18, 21]

def ciftMi3(sayi):
    return True if  sayi % 2 == 0 else False

def kareAl3(sayi):
    return sayi ** 2

print(all(map(ciftMi3, xAll)))
print(all(map(kareAl3, xAll)))

#############################################################

# ANY FUNCTION

# ANY fonksiyonu, verilen iterable edilebilen veri kümesinin herhangi bir elemanına true döndüren bir fonksiyonun sonucunu döndürür.

xAny = [1, 2, 4, 8, 12, 7, 5]
yAny = [3, 6, 9, 12, 15, 18, 21]

def ciftMi4(sayi):
    return True if  sayi % 2 == 0 else False

def kareAl4(sayi):
    return sayi ** 2

print(any(map(ciftMi4, xAny)))
print(any(map(kareAl4, xAny)))

#############################################################

# SUM FUNCTION

# SUM fonksiyonu, verilen iterable edilebilen veri kümesinin elemanlarının toplamını döndürür.

xSum = [1, 2, 4, 8, 12, 7, 5]
ySum = [3, 6, 9, 12, 15, 18, 21]

def ciftMi5(sayi):
    return True if  sayi % 2 == 0 else False

def kareAl5(sayi):
    return sayi ** 2

print(sum(map(ciftMi5, xSum)))
print(sum(map(kareAl5, xSum)))

#############################################################

# MIN FUNCTION

# MIN fonksiyonu, verilen iterable edilebilen veri kümesinin en küçük elemanını döndürür.

xMin = [1, 2, 4, 8, 12, 7, 5]
yMin = [3, 6, 9, 12, 15, 18, 21]

def ciftMi6(sayi):
    return True if  sayi % 2 == 0 else False

def kareAl6(sayi):
    return sayi ** 2

print(min(map(ciftMi6, xMin)))
print(min(map(kareAl6, xMin)))

#############################################################

# MAX FUNCTION

# MAX fonksiyonu, verilen iterable edilebilen veri kümesinin en büyük elemanını döndürür.

xMax = [1, 2, 4, 8, 12, 7, 5]
yMax = [3, 6, 9, 12, 15, 18, 21]

def ciftMi7(sayi):
    return True if  sayi % 2 == 0 else False

def kareAl7(sayi):
    return sayi ** 2

print(max(map(ciftMi7, xMax)))
print(max(map(kareAl7, xMax)))

#############################################################