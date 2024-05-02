def decorator (func):
    def wrapper ():
        print ("Fonksiyon öncesi")
        func()
        print ("Fonksiyon sonras1")
    return wrapper

@ decorator
def function() :
    print("Fonksiyon calisiyor...")

yeniFonksiyon = decorator(function)
yeniFonksiyon()

print("@ ile olan düzenlemeden sonra...")

function()


# Decorator Example

import time

def calismaSüresiHesapla(func):
    def wrapper(*args, **kwargs):
        baslangicZamani = time.time()
        func(*args, **kwargs)
        bitisZamani = time.time()
        print(bitisZamani - baslangicZamani)
    return wrapper

@ calismaSüresiHesapla
def kareAl(liste):
    for i in liste:
        print(i * i)

@ calismaSüresiHesapla
def ustAl(liste):
    for i in liste:
        print(i ** i)

kareAl([1, 2, 3, 4, 5])
ustAl([1, 2, 3, 4, 5, 6, 7, 8, 9])