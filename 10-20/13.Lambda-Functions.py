'''Normal fonksiyonların tek satırda yazılmasıdır. Parametre olarak fonksiyon alan fonksiyonlara fonksiyon göndermek için 
kullanılan fonksiyonlara denir. Genellikle kodun daha okunabilir olması için kullanılır. Tek yerde kullanılacak olan
fonksiyonlarda tercih edilir. Genel olarak isim verilmez.'''

karesiniAl = lambda x: x*x

carp = lambda x, y: x*y

print(karesiniAl(karesiniAl(4))) # Tekrar da çağırılabiliyor.

print(carp(carp(3, 4), karesiniAl(4))) # Çağırılan fonksiyonları iki paremetre olarak da çağırabiliyoruz.,

print((lambda x, y: x/y)(2,4)) # İsim vermeden tek satırda bu şekilde kullanılır.

print((lambda x: x%10==0)(30)) # Boolean değerler de döndürebiliyor.



