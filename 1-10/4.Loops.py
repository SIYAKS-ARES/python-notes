for i in range(10): # "range()" fonksiyonunda içine yazılan sayıya kadar gider, o sayıyı dahil etmez.
    print(i)
    
#Eğer "range(a, b)" şeklinde verilirse a'dan başlayıp, b'ye kadar sayar.
#Eğer "range(a, b, c)" şeklinde verilirse a'dan başlayıp, b'ye kadar c'şey sayar.
print("Ara")

index = 0
toplam = 0
while index <=10:
    toplam += index
    index += 1
print(toplam)
