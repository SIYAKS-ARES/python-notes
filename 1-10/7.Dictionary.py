# Web'ten veri çekerken, aynı zamanda JSON veri tipi ile bu veri tipi çok uyumlu olmasından dolayı da sık sık kullanılır.
sozluk = {"Book": "Kitap", "Dictionary":"Sözlük", "Collection": "Koleksiyon"}
# Sözlüklerde her bir eleman iki tane veri tutuar, key ve value. Key değerler kullanılarak value değerlerine ulaşılır.
print (sozluk["Collection"]) #Indis'lere ulaşmak için her zaman köşeli parantez kullanılır.

insan = {
    "İsim": "Özgür",
    "Soyisim" : "Akça",
    "Yaş" : 21,
    "Meslekler" : ["Bilgisayar mühendisliği", "Proje Yöneticiliği"]
}
print (insan["Yaş"])
print (insan["Meslekler"])
print (insan.keys())
print (insan.values())

for k, v in insan.items(): # ".items()" fonksiyonu kullanılmak zorundadır.
    print ("Kişinin {} keyinin değeri: {}".format(k, v))