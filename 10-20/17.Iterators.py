# Iterator'lar kısaca döngüye sokulabilecek objelerdir. Günlük hayatlarda sayılabilir nesnelere karşılık gelir.

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

iterlist = iter(List)

print(next(iterlist))
print(next(iterlist))
print(next(iterlist))
print(next(iterlist))
print(next(iterlist))

print("")
print("")

'''
Bunlar döngüler vs. yardımıyla da gerçekleştirilebilirlerdi lakin, liste boyutu(10M,15M...) çok büyükse bu yaklaşım çok uzun sürebilir, ayrıca
bu yaklaşımda döngüye sokulduğu objenin boyutu kadar döngüye girmesi gerekir, yani bu listenin hepsini işlemek, programın tüm elemanlara
ihtiyacı olmamasına rağmen bellekte tutmak bellek israfına sepeb olur. Örnekteki "next" ifadesi sadece çağırılınca veri alır.'''


# iki dezavantajı bulunur, ilki önceki elemana dönememesi ve son eleman için tüm elemanları gezmesinin gerekmesi.

text = "Hello World"

itertext = iter(text)

print(next(itertext))
print(next(itertext))
print(next(itertext))
print(next(itertext))
print(next(itertext))

# Hata verir çünkü son elemana dönmez, eleman bitmesine rağmen yeni eleman çekmeye çalışması. Bu yüzden "StopIteration" hatası alırız.
while True:
    try:
        print(next(itertext))
    except StopIteration:
        break

print("")
print("SINIFLAR")
print("")

# İterasyon Sınıfları

'''
Sınıflar, metodları gruplayan aaraçlardır, belirli işlemleri yapan metodları aynı sınıfta topluyoruz.
Sınıfların içerisindeki metodların çağırılması, sınıfın içerisindeki metodların çağırılmasıdır.
'''

class Ciftler: # Sınıf isimleri büyük harfle başlamalıdır.
    def __iter__(self): # __iter__ metodu, sınıfın içerisindeki metodların çağırılması için kullanılır. "Encapsulation" denir.
        # Sadece bu sııfta kullanılabilmesini sağlar.
        self.first_number = 0 # "self." ile tüm sınıfın erişimine açarız.
        return self

    def __next__(self):
        self.first_number += 2
        # x = self.a
        # self.a += 2
        if self.first_number > 10:
            raise StopIteration
        return self.first_number

ciftler = Ciftler()

ciftlerIter = iter(ciftler)

print(next(ciftlerIter))
print(next(ciftlerIter))
print(next(ciftlerIter))

print("")
print("GENERATORS")
print("")

# Generators

urunFiyatlari = [250, 300, 350, 400, 450, 500]

def indirimYap(fiyatlar):
    indirimliListe = list()
    for item in fiyatlar:
        indirimliListe.append(item - (item * 0.1))

    return indirimliListe

print(indirimYap(urunFiyatlari))

print("")
print("Yield")
print("")

# Bu yöntem büyük listelerde zaman kaybına sebep olur veya yeni ürün ekleneceği zaman çok uzun sürebilir. Performans düşük olur.
# Generators'ların avantajı, ilk elemanı çekmek için gerekli olan tüm işlemleri gerçekleştirmeye gerek kalmadan sonraki elemanı çekmeye başlayabilir.
def indirimYap2(fiyatlar):
    for item in fiyatlar:
        yield item - (item * 0.1) # Her çağırıldığında listeden yeni bir eleman alıp bunu döndürür.

indirimliListe = indirimYap2(urunFiyatlari)

#  print(next(indirimliListe))

for i in indirimliListe:
    print(i)

print("")
print("FIBONACCI WITH ITERATOR CLASS")
print("")

class Fibonacci:
    def __iter__(self):
        self.f1 = 0
        self.f2 = 1
        return self

    def __next__(self):
        # self.f1, self.f2 = self.f2, self.f1 + self.f2
        # return self.f2
        fib = self.f1 + self.f2
        self.f1 = self.f2
        self.f2 = fib
        return fib

fibonacci = Fibonacci()
fibonacciIter = iter(fibonacci)

print(next(fibonacciIter))

for i in range(10):
    print(next(fibonacciIter))

print("")
print("FIBONACCI WITH YIELD")
print("")

def fibonacci2(n): # n: Fibonacci'un kaçıncı elemanına kadar çekmek istediğimizi belirtir.
    f1 = 0
    f2 = 1
    i = 0
    while i < n:
        f1, f2 = f2, f1 + f2
        yield f1
        i += 1
    else:
        raise StopIteration

x = fibonacci2(5)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# print(next(x)) # Burada StopIteration hatası verir.

print("")
print("FIBONACCI IN ONE LINE")
print("")

# x = (x for x in range(100) if x % 2 == 0)

x2 = [0, 1]
x3 = [0, 1]

y = [x2.append(x2[i-1] + x2[i]) for i in range(1, 10)]

'''
# Generate Fibonacci sequence
fib = (x3.append(x3[-1] + x3[-2]) or x3[-1] for _ in range(10))

# Filter even Fibonacci numbers
even_fib = filter(lambda x: x % 2 == 0, fib)
'''

even_fib = [0] + [x3[-1] for _ in range(2, 10) if not x3.append(x3[-1] + x3[-2]) and x3[-1] % 2 == 0]

print(x2)
print(x3)
print(even_fib)