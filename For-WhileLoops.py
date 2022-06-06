from itertools import count


sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?
for sehir in sehirler:
    if (len(sehir) <= 5):
        print(sehir)

urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]

# 5- Ürünlerin fiyatları toplamı nedir ?
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
print(f"toplam fiyat:  {toplam}")

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?
for urun in urunler:
    if (int(urun['price']) <= 5000):
        print(urun['name'])

sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.
i = 0
while (i < len(sayilar)):
    print(sayilar[i])
    i += 1
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.
bas = int(input('baslangic: '))
fin = int(input('bitis: '))
while bas < fin:
    bas += 1
    if (bas % 2 == 1):
        print(bas)


# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
i = 100
while(i > 0):
    print(i)
    i -= 1

# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.
sayi = []
for i in range(5):
    i += 1
    count = int(input(f"{i}.sayi girin: "))
    sayi.append(count)
sayi.sort()
print(sayi) 
# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
urunler = []
totalproduct = int(input("Kac ürün eklemek istiyorsunuz: "))
i = 0
while (i < totalproduct):
    name = input("Urunun adi: ")
    price = input("Urunun fiyati: ")
    urunler.append({
        "name": name,
        "price": price
    })
    i += 1   
for urun in urunler:
    print(f"urun adi: {urun['name']} urunun fiyati: {urun['price']}")
    