sayi = float(input("Lütfen bir sayı giriniz: "))
sonuc = 1
for i in range(366):
    sonuc*=sayi
print(sonuc)

'''from decimal import Decimal, getcontext

# Hassasiyet ayarını yap (365 üssünü alacağımız için biraz fazla hassasiyet ayarlayalım)
getcontext().prec = 400

# Kullanıcıdan bir sayı al
sayi = Decimal(input("Bir sayı giriniz: "))

# Başlangıçta sonuc değeri 1 olarak ayarlanır
sonuc = Decimal(1)

# 365 defa üssünü almak için döngü
for _ in range(365):
    sonuc *= sayi

# Sonucu ekrana yazdır
print("Sonuç:", sonuc)'''