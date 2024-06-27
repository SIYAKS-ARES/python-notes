'''
Bazen hatalar kodun kendisinden kaynaklanmayabilir, kullanıcı bazlı, database bazlı hatalar/istisnalar kaynaklanabilir.
"İyi bir yazılım" da bu tür hatalara, isitsnalara karşı önlem alır. Kısaca hata ile karşılaşınca uygulanacak senaryolar tanımlanır.
'''

'''
Bazen hatalar kodun kendisinden kaynaklanmayabilir, kullanıcı bazlı, veritabanı bazlı hatalar/istisnalar kaynaklanabilir.
"İyi bir yazılım" bu tür hatalara, istisnalara karşı önlem alır. Hata ile karşılaşınca uygulanacak senaryolar tanımlanır.
'''

try:
    sayi3 = int(input("Sayi 3: "))
    sayi4 = int(input("Sayi 4: "))

    sonuc = sayi3 / sayi4

except ValueError:
    # Kullanıcı sayı yerine geçersiz bir giriş yaparsa bu blok çalışır
    print("ValueError: Lütfen sayısal bir değer giriniz.")
except ZeroDivisionError:
    # Kullanıcı ikinci sayıyı sıfır girerse bu blok çalışır
    print("ZeroDivisionError: Lütfen ikinci sayıyı 0 girmeyin.")
else:
    # Hiçbir hata oluşmazsa sonuç yazdırılır
    print(f"Sonuç: {sonuc}")

print("\n")

try:
    # Kullanıcıdan alınan veri her zaman string olarak alınır.
    sayi1 = int(input("Bir sayı giriniz: "))
    sayi2 = int(input("Bir sayı daha giriniz: "))

    sonuc = sayi1 / sayi2

except ValueError:
    # Kullanıcı sayı yerine geçersiz bir giriş yaparsa bu blok çalışır
    print("ValueError: Lütfen sayısal bir değer giriniz.")
except ZeroDivisionError:
    # Kullanıcı ikinci sayıyı sıfır girerse bu blok çalışır
    print("ZeroDivisionError: Lütfen ikinci sayıyı 0 girmeyin.")
else:
    # Hiçbir hata oluşmazsa sonuç yazdırılır
    print(f"Girilen değerlerin birbirine bölümü: {sonuc} İşlem başarılı.")
finally:
    # Hata olsun veya olmasın bu blok her zaman çalışır
    print("İşlem tamamlandı.")

print("\n")

try:
    sayi1 = int(input("Birinci sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))

    sonuc = sayi1 / sayi2

except ValueError as ve:
    # Kullanıcı sayı yerine geçersiz bir giriş yaparsa bu blok çalışır
    print(f"ValueError: {ve}")
except ZeroDivisionError as zde:
    # Kullanıcı ikinci sayıyı sıfır girerse bu blok çalışır
    print(f"ZeroDivisionError: {zde}")
except Exception as e:
    # Beklenmeyen diğer hatalar için genel bir except bloğu
    print(f"Beklenmeyen bir hata oluştu: {e}")
else:
    # Hiçbir hata oluşmazsa sonuç yazdırılır
    print(f"Sonuç: {sonuc}")
finally:
    # Hata olsun veya olmasın bu blok her zaman çalışır
    print("İşlem tamamlandı.")

'''
sayi3 = int(input ("Sayi 3: "))
sayi4 = int(input ("Say 4: "))

try:
    sonuc = sayi3 / sayi4
except:
    print("Hata olustu! Lütfen ikinci sayiy 0 girmeyin.")
else:
    print(sonuc)
'''
# sayi1 = int(input("Bir sayı giriniz: ")) # Kullanıcıdan alınan veri her zaman String olarak alınır.
# sayi2 = int(input("Bir sayı giriniz: "))

# print(sayi1 / sayi2) # İki değere de sayı girildiği zaman hata alınmaz.

'''
try:
    sonuc = sayi1 / sayi2
except ValueError:
    print("ValueError: invalid literal for int() with base 10: 'String'")
else:
    print(f"Girilen değerlerin birbirine bölümü: {sonuc} İşlem başarılı.")
try:
    print(sayi1 / sayi2) # İki değerden birine veya ikisine sayı dışında bir harf veya kelime vs. girildiğinde,
except ValueError:# "ValueError" hatası alıncaktır ama bu try/except bloğu sayesinde program hata verip durmak yerine devam edebilecek.
    print("Lütfen değerleri sayı olarak giriniz.") # Bu hatayı kullanıcıya göstermek için yazıldı.
'''
'''
# Hata Yönetimi Örnekleri

# Bazen hatalar kodun kendisinden kaynaklanmayabilir, kullanıcı bazlı, veritabanı bazlı hatalar/istisnalar kaynaklanabilir.
# "İyi bir yazılım" bu tür hatalara, istisnalara karşı önlem alır. Hata ile karşılaşınca uygulanacak senaryolar tanımlanır.

# Basit Bölme İşlemi ve Hata Yönetimi
def divide_numbers():
    try:
        sayi3 = int(input("Sayi 3: "))
        sayi4 = int(input("Sayi 4: "))

        # Bölme işlemini yapmaya çalışıyoruz
        sonuc = sayi3 / sayi4

    except ValueError:
        # Kullanıcı sayı yerine geçersiz bir giriş yaparsa bu blok çalışır
        print("ValueError: Lütfen sayısal bir değer giriniz.")
    except ZeroDivisionError:
        # Kullanıcı ikinci sayıyı sıfır girerse bu blok çalışır
        print("ZeroDivisionError: Lütfen ikinci sayıyı 0 girmeyin.")
    else:
        # Hiçbir hata oluşmazsa sonuç yazdırılır
        print(f"Sonuç: {sonuc}")

divide_numbers()

# Kullanıcıdan Alınan Verilerin Bölünmesi ve Hata Yönetimi
def divide_user_input():
    try:
        # Kullanıcıdan alınan veri her zaman string olarak alınır.
        sayi1 = int(input("Bir sayı giriniz: "))
        sayi2 = int(input("Bir sayı daha giriniz: "))

        # Bölme işlemini yapmaya çalışıyoruz
        sonuc = sayi1 / sayi2

    except ValueError:
        # Kullanıcı sayı yerine geçersiz bir giriş yaparsa bu blok çalışır
        print("ValueError: Lütfen sayısal bir değer giriniz.")
    except ZeroDivisionError:
        # Kullanıcı ikinci sayıyı sıfır girerse bu blok çalışır
        print("ZeroDivisionError: Lütfen ikinci sayıyı 0 girmeyin.")
    else:
        # Hiçbir hata oluşmazsa sonuç yazdırılır
        print(f"Girilen değerlerin birbirine bölümü: {sonuc} İşlem başarılı.")
    finally:
        # Hata olsun veya olmasın bu blok her zaman çalışır
        print("İşlem tamamlandı.")

divide_user_input()

# Gelişmiş Hata Yönetimi ve Kullanıcı Geri Bildirimi
def advanced_divide():
    try:
        sayi1 = int(input("Birinci sayıyı giriniz: "))
        sayi2 = int(input("İkinci sayıyı giriniz: "))

        # Bölme işlemini yapmaya çalışıyoruz
        sonuc = sayi1 / sayi2

    except ValueError as ve:
        # Kullanıcı sayı yerine geçersiz bir giriş yaparsa bu blok çalışır
        print(f"ValueError: {ve}")
    except ZeroDivisionError as zde:
        # Kullanıcı ikinci sayıyı sıfır girerse bu blok çalışır
        print(f"ZeroDivisionError: {zde}")
    except Exception as e:
        # Beklenmeyen diğer hatalar için genel bir except bloğu
        print(f"Beklenmeyen bir hata oluştu: {e}")
    else:
        # Hiçbir hata oluşmazsa sonuç yazdırılır
        print(f"Sonuç: {sonuc}")
    finally:
        # Hata olsun veya olmasın bu blok her zaman çalışır
        print("İşlem tamamlandı.")

advanced_divide()

# Genel Açıklamalar:
# - try bloğu içerisinde hata oluşturabilecek kodlar yer alır.
# - except blokları, belirli hata türlerini yakalamak ve bu hatalarla başa çıkmak için kullanılır.
# - else bloğu, try bloğu hatasız çalışırsa çalışır.
# - finally bloğu, hata olsun veya olmasın her zaman çalışır.
```

Bu dosya, üç farklı örnekle hata yönetimi konseptlerini göstermektedir:
1. **Basit Bölme İşlemi ve Hata Yönetimi**: Temel bölme işlemi ve iki tür hata (ValueError ve ZeroDivisionError) yönetimi.
2. **Kullanıcıdan Alınan Verilerin Bölünmesi ve Hata Yönetimi**: Kullanıcıdan alınan verilerin işlenmesi ve hata yönetimi, finally bloğu ile işlem tamamlanması.
3. **Gelişmiş Hata Yönetimi ve Kullanıcı Geri Bildirimi**: Daha kapsamlı hata yönetimi, beklenmeyen hataların genel yakalanması ve kullanıcıya geri bildirim sağlanması.

Bu kod örnekleriyle, kullanıcı hatalarına karşı nasıl önlem alabileceğinizi ve
programın hata durumlarında nasıl davranması gerektiğini öğrenebilirsiniz.'''