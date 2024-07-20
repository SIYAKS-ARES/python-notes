'''Girilen iki adet eşit eleman sayısına sahip sayı listesini önce birleştirip daha sonra
ilk n elemanı büyükten küçüğe sonraki n elemanı küçükten büyüğe olarak birleştiren
fonksiyonu yazınız.'''


# Kullanıcıdan girdi alırken listenin doğru formatta alınması için aşağıdaki kodu kullanabiliriz.
# Kullanıcıdan girdi alırken listenin doğru formatta alınması için aşağıdaki kodu kullanabiliriz.


liste1 = list(map(int, input("Lütfen bir n elemanlı liste giriniz (elemanları boşluk ile ayırın): ").split()))
liste2 = list(map(int, input("Lütfen ikinci bir n elemanlı liste giriniz (elemanları boşluk ile ayırın): ").split()))


def nTersCevir(liste1, liste2):
    if len(liste1) != len(liste2):
        print("Listelerin eleman sayıları eşit değil")
    else:
        n = len(liste1)
        merge_list = liste1 + liste2

        for i in range(n):
            for j in range(0, n-i-1):
                if merge_list[j] < merge_list[j+1]:
                    merge_list[j], merge_list[j+1] = merge_list[j+1], merge_list[j]

        for i in range(n, 2*n):
            for j in range(n, 2*n-1):
                if merge_list[j] > merge_list[j+1]:
                    merge_list[j], merge_list[j+1] = merge_list[j+1], merge_list[j]

        print("Birleşik ve sıralı liste: ", merge_list)

nTersCevir(liste1, liste2)