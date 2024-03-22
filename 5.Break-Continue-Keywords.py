############### BREAK
toplam = 0

while (True):
    sayi = int(input("Bir sayi giriniz: "))
    if sayi == 0:
        break
    else:
        toplam = toplam + sayi

print ("toplam: ",toplam)

############### CONTINUE

sayac = 0
while (sayac <= 10):
    sayac += 1
    if sayac % 2 != 0:
        continue
    print (sayac)
    
############### ÖRNEK

sayi = int(input("Asalligi kontrol edilecek sayiyi giriniz: "))

for i in range(2, sayi):
    if (sayi % i == 0):
        print (sayi, "sayisi asal degildir.")
        break
else:
    print (sayi, "sayisi asaldir.")
    
