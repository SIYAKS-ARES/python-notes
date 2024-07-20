# Kalıtım(Inheritance)

Kalıtım (inheritance), nesne yönelimli programlamada (OOP) kullanılan bir özelliktir ve Python'da da bu kavramı kullanarak kodunuzu daha verimli ve düzenli hale getirebilirsiniz. Kalıtım, bir sınıfın özelliklerini ve metotlarını başka bir sınıfa aktararak kod tekrarını önler ve kodunuzu daha modüler hale getirir.

## Kalıtım Nedir?

Kalıtım, bir sınıfın (alt sınıf veya türeyen sınıf olarak da adlandırılır) başka bir sınıfın (üst sınıf veya temel sınıf olarak adlandırılır) özelliklerini ve metotlarını devralmasını sağlar. Bu, alt sınıfın üst sınıfın tüm işlevselliğini kullanabilmesi anlamına gelir.

### Temel Kavramlar

1. **Üst Sınıf (Base Class / Parent Class):** Diğer sınıfların kalıtım aldığı sınıftır. Temel özellikler ve metotlar burada tanımlanır.

2. **Alt Sınıf (Derived Class / Child Class):** Üst sınıftan kalıtım alarak özellikleri ve metotları genişleten veya değiştiren sınıftır. Üst sınıftan devralınan özellikler ve metotları kullanabilir ve üzerine eklemeler yapabilir.

### Basit Bir Örnek

```python
# Üst sınıf
class Hayvan:
    def __init__(self, ad):
        self.ad = ad

    def sesCikar(self):
        return "Bir ses çıkarıyor."

# Alt sınıf
class Kedi(Hayvan):
    def __init__(self, ad, tur):
        super().__init__(ad)  # Üst sınıfın __init__ metodunu çağırır
        self.tur = tur

    def sesCikar(self): # Süper class'ın metodunu override ediyoruz/eziyoruz
        return "Miyav!"

# Kullanım
hayvan = Hayvan("Genel Hayvan")
kedi = Kedi("Pamuk", "Siyah")

print(hayvan.sesCikar())  # "Bir ses çıkarıyor."
print(kedi.sesCikar())   # "Miyav!"
```

#### Açıklamalar

1. **Üst Sınıf Tanımlaması:**
   - `Hayvan` sınıfı, `ad` adında bir özellik ve `sesCikar` adında bir metot içerir.

2. **Alt Sınıf Tanımlaması:**
   - `Kedi` sınıfı `Hayvan` sınıfından kalıtım alır.
   - `super().__init__(ad)` ifadesi, üst sınıfın `__init__` metodunu çağırarak `ad` özelliğini ayarlar.
   - `sesCikar` metodu, üst sınıfın metodunu geçersiz kılarak (`override`) kendi özel `Miyav!` değerini döner.

3. **Kullanım:**
   - `Hayvan` sınıfından bir nesne oluşturulur ve genel bir ses çıkarma işlevi gösterir.
   - `Kedi` sınıfından bir nesne oluşturulur ve kendi özel ses çıkarma işlevini gösterir.

### Başka Bir Örnek

Tabii, araba temalı bir örnek üzerinden kalıtımın nasıl çalıştığını detaylı bir şekilde açıklayalım. Bu örnekte, genel bir araba sınıfı ve farklı türde araçları temsil eden alt sınıflar oluşturacağız.

#### Senaryo: Araçlar

1. **Temel Sınıf:** `Araba` sınıfı, tüm araçların ortak özelliklerini ve metotlarını tanımlar.
2. **Alt Sınıflar:** `Sedan` ve `SUV` sınıfları, `Araba` sınıfından türetilir ve bazı özel özellikler ekler.

##### Python Koduyla Detaylı Örnek

```python
# Üst sınıf
class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgi_ver(self):
        return f"{self.marka} {self.model}, {self.yil} model."

    def hizlan(self, hiz):
        return f"Araba {hiz} km/s hıza ulaştı."

# Alt sınıf: Sedan
class Sedan(Araba):
    def __init__(self, marka, model, yil, bagaj_hacmi):
        super().__init__(marka, model, yil)  # Üst sınıfın __init__ metodunu çağırır
        self.bagaj_hacmi = bagaj_hacmi

    def bilgi_ver(self):
        # Üst sınıfın bilgi_ver metodunu geçersiz kılar ve bagaj hacmini ekler
        bilgi = super().bilgi_ver()
        return f"{bilgi} Bagaj hacmi: {self.bagaj_hacmi} litre."

    def uzun_yol(self):
        return "Sedan araç uzun yola uygundur."

# Alt sınıf: SUV
class SUV(Araba):
    def __init__(self, marka, model, yil, cekis_sistemi):
        super().__init__(marka, model, yil)  # Üst sınıfın __init__ metodunu çağırır
        self.cekis_sistemi = cekis_sistemi

    def bilgi_ver(self):
        # Üst sınıfın bilgi_ver metodunu geçersiz kılar ve çekiş sistemini ekler
        bilgi = super().bilgi_ver()
        return f"{bilgi} Çekiş sistemi: {self.cekis_sistemi}."

    def offroad_yetenegi(self):
        return "SUV araç off-road yeteneğine sahiptir."

# Kullanım
sedan = Sedan("Toyota", "Camry", 2023, 500)
suv = SUV("Land Rover", "Defender", 2024, "4x4")

print(sedan.bilgi_ver())     # "Toyota Camry, 2023 model. Bagaj hacmi: 500 litre."
print(sedan.hizlan(120))     # "Araba 120 km/s hıza ulaştı."
print(sedan.uzun_yol())      # "Sedan araç uzun yola uygundur."

print(suv.bilgi_ver())       # "Land Rover Defender, 2024 model. Çekiş sistemi: 4x4."
print(suv.hizlan(150))       # "Araba 150 km/s hıza ulaştı."
print(suv.offroad_yetenegi()) # "SUV araç off-road yeteneğine sahiptir."
```

##### Araçlar Örneğinin Açıklamaları

1. **`Araba` Sınıfı:**
   - **`__init__` Metodu:** `marka`, `model`, ve `yil` gibi temel özellikleri başlatır.
   - **`bilgi_ver` Metodu:** Arabanın temel bilgilerini döner.
   - **`hizlan` Metodu:** Arabayı verilen hızda hızlandırır.

2. **`Sedan` Sınıfı:**
   - **Kalıtım:** `Araba` sınıfından türetilir.
   - **`__init__` Metodu:** Üst sınıftan gelen `marka`, `model`, ve `yil` özelliklerine ek olarak `bagaj_hacmi` özelliğini ekler.
   - **`bilgi_ver` Metodu:** Üst sınıfın `bilgi_ver` metodunu geçersiz kılar ve `bagaj_hacmi` bilgisini ekler.
   - **`uzun_yol` Metodu:** Sedan araçlarının uzun yol için uygun olduğunu belirtir.

3. **`SUV` Sınıfı:**
   - **Kalıtım:** `Araba` sınıfından türetilir.
   - **`__init__` Metodu:** Üst sınıftan gelen `marka`, `model`, ve `yil` özelliklerine ek olarak `cekis_sistemi` özelliğini ekler.
   - **`bilgi_ver` Metodu:** Üst sınıfın `bilgi_ver` metodunu geçersiz kılar ve `cekis_sistemi` bilgisini ekler.
   - **`offroad_yetenegi` Metodu:** SUV araçlarının off-road yeteneğini belirtir.

4. **Kullanım:**
   - `Sedan` ve `SUV` sınıflarından nesneler oluşturulur ve her iki sınıfın da genel ve özel metotları kullanılarak sonuçlar yazdırılır.

Bu örnek, kalıtımın nasıl çalıştığını ve Python'da nasıl kullanıldığını kapsamlı bir şekilde açıklar. Üst sınıftan özelliklerin ve metotların nasıl devralındığını, alt sınıflarda nasıl özelleştirilebileceğini ve yeni özelliklerin nasıl eklenebileceğini gösterir.

### `pass` Kullanımı

`pass` anahtar kelimesi, Python'da boş bir blok veya yer tutucu olarak kullanılan bir komuttur. Genellikle kodun ilerleyen bölümlerinde eklenmesi gereken kodları yer tutmak veya geçici olarak bir bloğu tamamlamak için kullanılır. İşte farklı kullanım senaryolarıyla birlikte `pass` anahtar kelimesinin nasıl kullanılacağını gösteren detaylı bir örnek:

#### Örnek Senaryosu: Araçlar ve Bakım

Bu örnekte, araçların genel özelliklerini ve bazı temel fonksiyonları temsil eden bir `Arac` sınıfı ve bu sınıftan türeyen `Araba` ve `Motorsiklet` sınıflarını oluşturacağız. Ayrıca, bazı metotların geçici olarak implementasyonları tamamlanmamış olacak ve `pass` anahtar kelimesi kullanılarak yer tutucular ekleyeceğiz.

```python
# Temel sınıf
class Arac:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgi_ver(self):
        return f"{self.marka} {self.model}, {self.yil} model."

    def bakım_yap(self):
        pass  # Bu metodun implementasyonu daha sonra yapılacak

# Alt sınıf: Araba
class Araba(Arac):
    def __init__(self, marka, model, yil, kapı_sayisi):
        super().__init__(marka, model, yil)
        self.kapı_sayisi = kapı_sayisi

    def bilgi_ver(self):
        bilgi = super().bilgi_ver()
        return f"{bilgi} Kapı sayısı: {self.kapı_sayisi}."

    def bakım_yap(self):
        print("Araba bakımı yapılıyor.")
        # Geçici olarak sadece bir mesaj yazdırır

# Alt sınıf: Motorsiklet
class Motorsiklet(Arac):
    def __init__(self, marka, model, yil, tipi):
        super().__init__(marka, model, yil)
        self.tipi = tipi

    def bilgi_ver(self):
        bilgi = super().bilgi_ver()
        return f"{bilgi} Tipi: {self.tipi}."

    def bakım_yap(self):
        print("Motorsiklet bakımı yapılıyor.")
        # Geçici olarak sadece bir mesaj yazdırır

# Kullanım
araba = Araba("Toyota", "Corolla", 2023, 4)
motorsiklet = Motorsiklet("Yamaha", "MT-07", 2024, "Spor")

print(araba.bilgi_ver())        # "Toyota Corolla, 2023 model. Kapı sayısı: 4."
print(motorsiklet.bilgi_ver())  # "Yamaha MT-07, 2024 model. Tipi: Spor."

araba.bakım_yap()               # "Araba bakımı yapılıyor."
motorsiklet.bakım_yap()         # "Motorsiklet bakımı yapılıyor."
```

#### `pass` Kullanım Alanları

1. **Yoksa Bir Kod Blokunun Geçici Olarak Boş Bırakılması:**

   ```python
   def bakım_yap(self):
       pass
   ```

   Bu metod, henüz implementasyonu yapılmamış bir metodun yer tutucusudur. Metodun implementasyonu gelecekte eklenecektir.

2. **Geçici Sınıf Tanımları:**

   ```python
   class Araç:
       pass  # Araç sınıfının henüz içeriği tanımlanmadı
   ```

   Boş bir sınıf tanımı yaparak, daha sonra bu sınıfa özellikler ve metotlar eklemek için yer tutucudur.

3. **Koşul ve Döngüler İçin Boş Bloklar:**

   ```python
   for i in range(10):
       if i % 2 == 0:
           pass  # Geçici olarak yapılacak iş yok
   ```

   Bu kullanım, bir döngü veya koşul yapısında henüz yapılacak iş olmadığı veya işlerin gelecekte yapılacağı bir durum için yer tutucudur.

4. **Geçici Olarak Boş Metodlar veya Fonksiyonlar:**

   ```python
   def placeholder_function():
       pass  # Fonksiyonun içeriği daha sonra eklenecek
   ```

   Fonksiyonun şimdilik boş bırakılmasını sağlar, işlevsellik gelecekte eklenebilir.

#### `pass` Özet

`pass`, Python'da yer tutucu olarak kullanılır ve kodun belirli bölümlerinin geçici olarak boş bırakılmasını sağlar. Bu, kodun yapı taşlarını oluştururken ve ileride ekleme yaparken faydalıdır. Ayrıca, metodlar, sınıflar, döngüler veya koşullar gibi çeşitli yapılar içinde kullanılarak geçici boşluklar sağlar.

### Genel Özet

Kalıtım, bir sınıfın başka bir sınıfın işlevlerini devralmasını ve gerektiğinde bu işlevleri değiştirmesini sağlar. Bu, kodun tekrarını azaltır ve daha modüler bir yapı oluşturur. Python'da kalıtım `class` anahtar kelimesi ile sağlanır ve `super()` fonksiyonu, üst sınıfın metotlarını ve özelliklerini çağırmak için kullanılır.
