print("Break")
toplam = 0

while (True):
    sayi = int(input("Bir sayi giriniz: "))
    if sayi == 0:
        break
    else:
        toplam = toplam + sayi

print ("toplam: ",toplam)

print("Continue")

sayac = 0
while (sayac <= 10):
    sayac += 1
    if sayac % 2 != 0:
        continue
    print (sayac)
    
