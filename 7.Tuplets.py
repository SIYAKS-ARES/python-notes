# Demetler ile liste gibi yapılar oluşturulur tek fark eklenen veriler değiştirilemez.
# Kullanım alanları: Büyük projerlerde birçok yazılım/programcı çalışıtığı ve birbirlerinin verilerini bozma ihtimalinin önüne geçmek,
# çözmesi en zor olan mantıksal hataları minimuma indirmek için kullanılır.

sabitler = (3.12, 3.13, 3.14, 3.15) # Listede "[3]" kullanılırken tuple'larda "()" kullanılır.
print (sabitler)
print (type(sabitler)) # "type()" fonksiyonu ile sabitlerin türü yazdırılabilir. <class "tuple">
print (sabitler.count(3.14)) # ".count" fonksiyonu ile kaç defa geçtiğini görebiliriz. 
print (sabitler.index(3.14)) # ".index" fonksiyonu ile kaçıncı index'te olduğunu görebiliriz. 