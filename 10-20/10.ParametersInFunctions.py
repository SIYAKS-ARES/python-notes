def topla(x, y): # Parametrelere varsayılan değerler (x=0,y=0) şeklinde verilebilir.
    return x + y

print(topla(10,5)) # Parametrelerin yerini değiştirmek için (y=10,x=15) şeklinde yazılabilir.

'''Bu şekilde fonksiyona verilecek parametrelerin sayısı belli değilken hata almanın önüne geçilebilir. "*args" içerisinde bir
tuple listesi tutar. Gelen verileri bir tuple listesi olarak tutar. Kullanıcı bu şekilde istediği kadar parametre girebilir
'''

def yuzdeAl(yuzdeOranı, *args): # "args" arguments'in kısaltmasıdır. Bu tek yıldızlı örneğidir.
    yuzdesiAlinanSayilar = list()
    for i in args:
        yuzdesiAlinanSayilar.append(i * yuzdeOranı / 100)
    return yuzdesiAlinanSayilar # Don't you ever forget to add return value!!! This is so embarrassing!
    # Bu bir liste olduğu için for döngüsünden çıktıktan sonra return etmelisin, ki değerler listeye eklenmiş olsun.
print(yuzdeAl(18, 3212123, 2131, 3242, 36327, 632427, 25*4)) # Bu şekilde fonksiyonun parametre değerinde bile işlem yaptırabiliyoruz.

def yazdir(**kwargs): # Sözlük olarak geri döndürür. İsim, soyisim, yaş verisi alınırken kullanılabilir.
    print(kwargs)

yazdir(x = 2, a = 212, y = 213) # {'x': 2, 'a': 212, 'y': 213} çıktısını verir.