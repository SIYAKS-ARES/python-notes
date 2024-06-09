'''Belirli kurallara göre, devamlı kendi kendini çağıran fonksiyonlara Özyinemeli fonskiyonlar denir.
Recursive fonksiyonların tüm işlemlerini döngüler yardımıyla da yapabiliriz.
Recursive fonksiyonlar çok fazla bellek kullanır ve döngülere göre daha yavaştırlar.
Zamanı da çok iyi yönetemezler.
Kullanım amacı programlama yaparken daha okunabilir ve temiz bir kod yazmaya çalışmaktır. Genel olarak dögüler yapı olarak daha
basit olsa da bazı durumlarda çok karmaşıklaşabiliyor. Eksta olarak Python programalama dilinde en fazla 1000 adet yineleme yapılabiliyor.
Bu sayı arttırılmak istendiğinde Python'un özel dosyalarını kullanmanız gerekir.'''

# Recursive'ler stack/yığın yapısıyla çalışırlar.

def faktoriyel(sayi):
    if sayi == 0 or sayi == 1:
        return 1
    else:
        return sayi * faktoriyel(sayi - 1)

print(faktoriyel(5))

def listSum(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + listSum(list[1:])

'''This line performs the recursive step. It returns the sum of the first element of the list (list[0]) and
the result of calling the listSum function recursively with the remaining elements of the list (list[1:]).
The list[1:] syntax creates a new list that contains all elements of the original list except the first one.
This new list is passed as an argument to the recursive call of listSum.
The recursion continues until the base case (len(list) == 0) is reached, at which point the recursion stops,
and the function starts returning the sum of the elements.
In summary, this function calculates the sum of all elements in a list using recursion. It does this by breaking
down the problem into smaller sub-problems (summing the remaining elements of the list) until the base case (an empty list) is reached.
Then, it combines the results of the sub-problems to get the final sum.'''

print(listSum([1, 2, 3, 4, 5]))

print("Döngüler")

for i in range(5): # Döngü kullanılarak yazılmış versiyonu.
    print('Loop: Çınar Hüseyinoğlu')

print("Recursive")

def adiYaz(int):
    if int == 0:
        return
    else:
        print('Recursive: Çınar Hüseyinoğlu')
        adiYaz(int - 1)

adiYaz(5)
