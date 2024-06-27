def kareAl(sayi):
    return sayi * sayi
kendisiyleCarp = kareAl
print(kendisiyleCarp(3))

def parkEt(aracTipi):
    def motorsikletUcretiHesaplama(saat):
        return saat * 3
    def arabaUcretiHesaplama(saat):
        return saat * 6
    def kamyonetUcretiHesaplama(saat):
        return saat * 9

    if aracTipi.lower() == "motorsiklet" or aracTipi.lower() == "motor":
        return motorsikletUcretiHesaplama
    elif aracTipi.lower() == "araba":
        return arabaUcretiHesaplama
    elif aracTipi.lower() == "kamyonet":
        return kamyonetUcretiHesaplama
    else:
        raise ValueError("Geçersiz araç tipi")

arac_tipi = input("Lütfen araç tipini giriniz (Motorsiklet/Araba/Kamyonet): ")
saat = int(input("Lütfen park etmek istediğiniz saati giriniz: "))
ucret_hesapla = parkEt(arac_tipi)
print("Toplam ücret:", ucret_hesapla(saat))

############ Second Example

def isimVeYas(isim, yas):
    if yas < 0:
        raise ValueError("Yaş sıfırdan küçük olamaz")
    return f"İsim: {isim}, Yaş: {yas}"
def kisiOlustur(isim):
    def kisi(yas):
        return isimVeYas(isim, yas)
    return kisi
kisi = kisiOlustur("Ahmet")