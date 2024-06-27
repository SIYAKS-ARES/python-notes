isimler = ["Ali","Veli","Deli","Özgür","Samet"] # Listelere String değerlerin yanına integer değerler de eklenebilir.
print ("0:",isimler[0])
print ("1:",isimler[1])
print ("2:",isimler[2])
print ("-1:",isimler[-1])
print ("-2:",isimler[-2])
print ("-3:",isimler[-3])

print (isimler[:2]) # Başına ":" getirilince en baştan başla o sayıya kadar git demek.
print (isimler[2:]) # Sonuna ":" getirilince sayıdan başla o sona kadar git demek.
print (isimler[::-1]) # Baştan başla, sona kadar git ve tersten git demek.
print (isimler[::1]) # Tüm listeyi baştan başlayarak yazdırır.

print(len(isimler)) # Listemizin kaç elemanlı olduğunu gösterir.

ogrenciler = [["Özgür", 12],  ["Samet", 13], ["Ali", 14]]
print(ogrenciler[2][0])
ogrenciler[2][1] = 11

############## ÖRNEK

fiyatlar = [100, 2342, 2133, 234, 2341]
satisFiyatlari = list()
for i in fiyatlar: # Bu for dögüsünde i ile ilk elemandan başlayıp her elemanı tek tek gezmeyi tanımlar.
    yuzde = i*18/100
    satisFiyatlari.append(i + yuzde) # ".append" metodu listeye eleman eklemek için kullanılır. Sondan eklenir.

print(satisFiyatlari)

fiyatlar.sort() # ".sort" metodu ile liste küçükten büyüğe doğru kalıcı olarak sıralar.
print(fiyatlar)

fiyatlar.reverse() # ".reverse" metodu ile liste kalıcı olarak ters çevrilir.
print(fiyatlar)

fiyatlar.insert(1, 1001) # ".insert" metodu ile listeye eleman eklenir. Virgülden önceki kısma gelen sayı hangi index'e ekleneceğini belirtir.
print(fiyatlar)