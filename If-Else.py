# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
count = float(input("sayi: "))
if(count >= 0 and count <=100):print(f"{count} degeri 0-100 arasindadir")
else:print(f"{count} degeri 0-100 arasinda degildir")
# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
if(count > 0 and count % 2 == 0):print(f"{count} degeri pozitif bir cift sayidir")
else:print(f"{count} degeri pozitif bir cift sayi degildir")
# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = "email@gmail.com" 
parola = "abc123"
girEmail = input("email: ")
girPass = input("password: ")
if(email == girEmail.lower().strip()) and (parola == girPass.strip()):print("email ve parola gecerli")
else:print("Email ya da parola yanlis. Lütfen tekrar deneyin")
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if(a > b and a > c):print(f"{a} sayisi {b} ve {c} büyüktür")
elif(b > a and b > c):print(f"{b} sayisi {a} ve {c} büyüktür")
elif(c > a and c > b):print(f"{c} sayisi {a} ve {b} büyüktür")
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
vize1= float(input("1. vize: "))
vize2= float(input("2. vize: "))
final= float(input("final: "))
ort= (((vize1 + vize2) / 2) * 0.6)  + (final * 0.4)
print(f"dersin Ortalamasi: {ort}")
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
if(ort >= 50):print("Gecti")
else:print("Kaldi")
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
if(ort >= 50 and final >= 50):print("Gecti")
else:print("Kaldi")
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
if(ort >= 50 or final >=70):print("Gecti")
else:print("Kaldi")
# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
name = input('adınız: ')
kilo = float(input('kilonuz: '))
boy = float(input('boyunuz: '))
#    Formül: (Kilo / boy uzunluğunun karesi)
indeks = kilo / (boy ** 2)
if(indeks >=0 and indeks <=18.4):print(f"{name} boy-kilo indeksin: {indeks} Zayifsin ")
elif(indeks >18.4 and indeks <=24.9):print(f"{name} boy-kilo indeksin: {indeks} Normalsin ")
elif(indeks >24.9 and indeks <=29.9):print(f"{name} boy-kilo indeksin: {indeks} Kilolusun ")
elif(indeks >29.9 and indeks <=34.9):print(f"{name} boy-kilo indeksin: {indeks} Obezsin ")
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)


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

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.


# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.