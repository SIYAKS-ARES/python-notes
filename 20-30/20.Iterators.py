# Iterator'lar kısaca döngüye sokulabilecek objelerdir. Günlük hayatlarda sayılabilir nesnelere karşılık gelir.

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

iterlist = iter(List)

print(next(iterlist))
print(next(iterlist))
print(next(iterlist))
print(next(iterlist))
print(next(iterlist))

'''
Bunlar döngüler vs. yardımıyla da gerçekleştirilebilirlerdi lakin, liste boyutu(10M,15M...) çok büyükse bu yaklaşım çok uzun sürebilir, ayrıca
bu yaklaşımda döngüye sokulduğu objenin boyutu kadar döngüye girmesi gerekir, yani bu listenin hepsini işlemek, programın tüm elemanlara
ihtiyacı olmamasına rağmen bellekte tutmak bellek israfına sepeb olur. Örnekteki "next" ifadesi sadece çağırılınca veri alır.'''

'''
iki dezavantajı bulunur, ilki önceki elemana dönememesi ve son eleman için tüm elemanları gezmesinin gerekmesi.'''

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


