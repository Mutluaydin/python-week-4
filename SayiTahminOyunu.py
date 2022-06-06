import random

'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
      üzerinden hesaplansın.
'''
sayi = random.randint(1,100)
can = int(input("can sayisini girin: "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("bir sayi giriniz: "))

    if tahmin == sayi:
        print(f"tebrikler bildiniz. Toplam puaniniz: {100 - (100 / can) * (sayac - 1)}" )
        break
    elif sayi > tahmin:
        print("Yukari")
    else:
        print("Asagi")

    if hak == 0:
        print(f"Hakkiniz bitti. Tutulan sayi: {sayi} ")

