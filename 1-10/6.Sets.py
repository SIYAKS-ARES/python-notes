# Bir küme içerisinde aynı elemandan yalnızca bir tane olabilir.
küme = {1,2,3,4,5,6,7,8,9,1,2,3,4,5} # Süslü parantez kullanılır.
print (type(küme))
############### Set'ler indexlenemezler ###############
print (len(küme)) #"len()" fonksiyonu kümenin sayısını yazdırır.
# 'küme."***"' ile çıkan fonksiyonar yapılabilir, bunlar; kaldırma, fark, kopyala, kesişim gibi normal küme mantığı ile yapılabilecek işlemlerdir.
numaralar = {1,2,3}
print (küme.difference(numaralar))