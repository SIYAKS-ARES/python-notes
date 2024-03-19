'''
Değişkenlerin ismi sayi ile başlayamaz,
Değişkenlerin içerisinde arasinda boşluk olamaz,
Türkçe karakterler kullanilamaz
'''
sayi = 20 #Bu şekilde hafızada sayi isminde bir alan oluşturuldu ve bu alanda 20 sayisi tutuluyor.
print (sayi)
isim = "SIYAKSARES" #String yapılarında da aynı şekilde değişken oluşturulur, tek fark "" açmanin gerektiğidir.
print (isim)


#3.VAT-Sale-Example
fiyat = 100
kdv = 18
kdvTutari = fiyat * kdv / 100
satisFiyati = fiyat + kdvTutari
print ("Urunun satis fiyati: ",satisFiyati)