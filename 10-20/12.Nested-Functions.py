'''
Bir fonksiyon içerisinde birden fazla ve farklı işlemleri gruplamak ihtiyacı doğduğunda,
daha temiz kod yazmak istendiğinde işe yarayan bir yöntemdir.
'''

def yasalKisitlar(yas):
    def ehliyetAlabilme(y):
        return y >= 18
        '''if yas >= 18:
            print("Ehliyet alabilir!")
        else:
            print("Ehliyet alamaz!")'''

    def emekliOlabilme(y):
        return y >= 65

    def milletVekiliOlabilme(y):
        return y >= 25

    print(ehliyetAlabilme(yas)) # Burada değer verilmez ana fonksiyonun parametresi verilir.
    print(emekliOlabilme(yas))
    print(milletVekiliOlabilme(yas))
    # Eğer fonksiyonların içersinde olan fonksiyonda çağırılmazlarsa program hata verir.

yasalKisitlar(11) # Tekrardan print ile yazdırmaya gerek yok.