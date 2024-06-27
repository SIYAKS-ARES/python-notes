for i in range(10): # "range()" fonksiyonunda içine yazılan sayıya kadar gider, o sayıyı dahil etmez.
    print(i)

# Eğer "range(a, b)" şeklinde verilirse a'dan başlayıp, b'ye kadar sayar.
# Eğer "range(a, b, c)" şeklinde verilirse a'dan başlayıp, b'ye kadar c kadar sayar.
print("Ara")

index = 0
toplam = 0
while index <=10:
    toplam += index
    index += 1
print(toplam)

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
