'''
Lambda fonksiyonları, basit fonksiyonların tek satırda yazılmasıdır. Parametre olarak başka fonksiyonlar alabilen ve bu fonksiyonlara
başka fonksiyonlar göndermek için kullanılan fonksiyonlardır. Genellikle kodun daha okunabilir olması için tercih edilirler.
Lambda fonksiyonları genellikle tek bir yerde kullanılacak olan fonksiyonlar için uygundur ve bu nedenle isim verilmez.
İşlevselliği artırmak ve kodun daha kısa ve öz olmasını sağlamak amacıyla kullanılırlar.
'''

karesiniAl = lambda x: x*x

carp = lambda x, y: x*y

print(karesiniAl(karesiniAl(4))) # Tekrar da çağırılabilirer.

print(carp(carp(3, 4), karesiniAl(4))) # Çağırılan fonksiyonları iki paremetre olarak da çağırabilirler.

print((lambda x, y: x/y)(2,4)) # İsim vermeden tek satırda bu şekilde kullanılırlar.

print((lambda x: x%10==0)(30)) # Boolean değerler de döndürebilirler.