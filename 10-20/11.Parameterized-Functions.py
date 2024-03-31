# Parametreli fonskiyonlar ise tam tersi olarak parantez içine parametre alan fonksiyonlardır.
# Fonksiyonların içine belirli komutlar eklenip isimler de onlara göre verilir. Genelleme yapılmamalıdır.
# Fonksiyon isimleri de elbette diğer isim belirleme aşamları gibi Türkçe karakter içermemelidir.
def isimYazdir(ad, soyad):
    print ("İsim: {} \nSoyisim: {}".format(ad, soyad))
    
isimYazdir("Samet","Yasit") # Fonskiyon çağırıldıktan sonra çift nokta almaz.

# "def" , "definition" un kısaltmasıdır.

def karesiniAl(x):
    print ("Girmiş olduğunuz" , x,"sayısının karesi:",x*x)
    
karesiniAl(4)

# Bunlar geri değer döndürmeyen fonskiyonlar, döndürenlerde return key'i kullanılır.

def bolme(sayi1,sayi2):
    sonuc = 0
    if sayi2 == 0:
        print("İkinci sayı sıfır girilemez!")
    else:
        sonuc = sayi1/sayi2
        return sonuc
        
print(bolme(1,2))

islemSonucu = bolme(1,0)

def resitMi(yas):
    sonuc = False
    if yas>=18:
        sonuc = True
    return sonuc

if(resitMi(18)):
    print("Oy kullanabilir!")
else:
    print("Oy kullanamaz!")
    
############### Önceki derslerde yapılan kdv örneğinin fonksiyon metoduyla yapılışı:

def kdvHesapla(kdv,fiyat):
    kdvTutari = fiyat * kdv / 100
    satisFiyati = fiyat + kdvTutari
    print ("Urunun satis fiyati: ",satisFiyati)
    
kdvHesapla(18,100)

def reverse_numbers(numbers):
    return numbers[::-1]

try:
    num_count = int(input("Enter the number of integers: "))
    num_list = []
    for i in range(num_count):
        num = int(input(f"Enter integer {i + 1}: "))
        num_list.append(num)
    reversed_list = reverse_numbers(num_list)
    print("Reversed list of integers:", reversed_list)
except ValueError:
    print("Invalid input. Please enter valid integers.")