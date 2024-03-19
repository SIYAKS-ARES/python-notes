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
    
    