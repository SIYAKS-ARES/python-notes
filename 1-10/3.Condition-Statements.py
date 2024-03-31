sayi = 10

if(sayi == 0):# "=" atama operatörüyken (Ps. işaretin sağındaki değeri alıp soldakine atama), "==" karşılaştırma operatörüdür.
    print ("Sayi 0'a eşittir.")
    #Python'da çıkıntı kavrami vardir. Koşulun bir alt çıkıntısı içeriye girildiği zaman yapılacak kodları barındırır.
elif(sayi < 0):
    print("Sayi sifirdan kucukutur")
elif(sayi > 0):
    print("Sayi sifirdan buyuktur")
else:
    print ("Sayi 0'a esit degildir.")
    
###############Condition Statement Examples

#İlk örnek doğum tarihine göre ehliyet alıp alamayacağını gösteren yapı

dogumTarihi = 2000  #Bu şekilde ilk harf küçük, sonraki kelimenin harfi büyük olan yapılara "Camel Case" denir.
tarih = 2024
yas = tarih - dogumTarihi
if(yas >= 18):
    print(yas, "Oldugu ve 18 yasindan buyuk oldugunuz icin ehliyet alabilirsiniz!")
else:
    print(yas, "Oldugu ve 18 yasindan kucuk oldugunuz icin ehliyet alamazsiniz!")
    
#İkinci örnek sisteme giriş yapma yapısı

#kullaniciAdi = "SIYAKSARES" #Tırnak işareti unutulmamalıdır.
#kullaniciSifresi = "1234" #Burada da matematiksel bir işlem yapılmayacağı için tırnak içine alınır.

#Ayrıca kullanıcıdan da giriş bilgileri istenebilir.
kullaniciAdi = input("Kullanici adini giriniz: ")
kullaniciSifresi = input("Kullanici sifresini giriniz: ")

if(kullaniciAdi == "SIYAKSARES" and kullaniciSifresi=="1234"):
    print("Girilen bilgiler dogru, giris yapiliyor!")
else:
    print("Girilen bilgiler hatali, cikis yapiliyor!")
    
###############Kısa Yazılan Koşul İfadeleri
import math

sayi2 = int(input("Lutfen bir sayi giriniz: ")) #Gelen String değerini integer değere çevirmek için başına "int(" getirilir.

filtreliSayi = sayi2 if sayi2 >= 0 else math.fabs(sayi2) #"math.fabs()" fonksiyonu ondalıklı değerle mutlak değerini alır.
print("Sayiniz: " , filtreliSayi)

sayi3 = int(input("Lutfen bir sayi giriniz: "))
islenmisDeger = sayi3 if sayi3 == 10 else sayi3*2 if sayi3 > 10 else sayi3/2 #Burada da koşulun gerçekleşmeme koşulunu koşula bağlamış olduk.
#Sayı 10 iken 10'u, 12 iken 24'ü, 8 iken 4'ü verir.
print("Yeni sayiniz: " , islenmisDeger)