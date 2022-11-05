#DÖNGÜLER
# ---------> 1.For
# Belli bir collection içinde gezinerek,dönerek tekrarlı olarak yapılması istenen işlemleri gerçekleştirir.
# liste tanımı:[1,2,3,4,5] ---->python yazımı
# range(n):[0,1,2,.....,n)----->python yazımı değil matematiksel gösterimi.
'''
for iterasyon_name in collection:
    tekrarlı olarak yapılacak işlemler

# collection içinde okunacak veri kalmayana dek döner.
'''
# for isim in ["damla","gonca","aykut","arif","neslihan","tayfun"]:
#     print(isim)
#
# # rakamlar listesi oluşturup ekranda alt alta yazınız.
# for rakam in ["1","2","3","4","5","6","7","8","9"]:
#     print(rakam)
# for rakam in [1,2,3,4,5,6,7,8,9,0]:
#     print(rakam**2)
# rakamlar_listesi=[1,2,3,4,5,6,7,8,9,0]
# for rakam in rakamlar_listesi:
#     print(rakam**2)
# range(10)--->[0,1,2,3,4,5,6,7,8,9]
# for i in range(10):
#     print(i)
# 10 kez merhaba dünya yazdırınız.
# for i in range(10,):
#     print(f"{i+1}.merhaba dünya!")

# 50-100 aralığındaki çift sayıları yazınız.
# for i in range(50,101):
#     if i % 2==0:
#         print(i)
#
# # range(5,10)--->[5,6,7,8,9]
# # range(10,20,2)--->[10,12,14,16,18]
# for i in range(50,101,2):
#     print(i)
# # TEKLER İÇİN:
# for i in range(51,101,2):
#     print(i)

# for örnekleri:
# 10-20 arasındaki sayıları geriden yazdırınız.20-19-18-...11
#for i in range (20,10,-1):
#    print(i)

# 0-20 arasındaki tek sayıların toplamını döngü ile bulunuz.
# toplam=0
# for i in range(1,20,2):
#     toplam += i    #toplam=toplam+i
# print(toplam)

# 1-100 arasındaki teklerin  ve çiftlerin ayrı ayrı toplamını aynı döngüde hesaplayınız.
# cift_toplam=0
# tek_toplam=0
# for i in range(1,101):
#     if i % 2==0:  #çift
#         cift_toplam +=i
#     else:
#         tek_toplam +=i
#
# # print(f"TEKLERİN TOPLAMI:{tek_toplam} \n ÇİFTLERİN TOPLAMI:{cift_toplam} ")
# # sum(T): içindeki değerleri toplanarak sonuç döner.
# print(f"teklerin toplamı:{sum(range(1,101,2))}")
# print(f"çiftlerin toplamı: {sum(range(0,101,2))}")
'''
nested loop(iç içe döngüler)
for i in collection1:
    for j in collection2:
        pass
    pass
    
'''
# çarpım tablosunu döngü kullanarak yazdırınız.
# title_list = ["1'ler","2'ler","3'ler","4'ler","5'ler","6'lar","7'ler","8'ler","9'lar","10'lar"]
# for i in range(1,11):
#     print(title_list[i-1])
#     print("_________")
#     for j in range(1,11):
#         print(f"{i}x{j}={i*j}")
#     print("__________")
# end: ne ile biteceğini belirliyor.\t bir tab demek.
# yan yana çarpım tablosunu yazdırma.
# title_list = ["1'ler","2'ler","3'ler","4'ler","5'ler","6'lar","7'ler","8'ler","9'lar","10'lar"]
# for i in title_list:
#     print(i,end="\t"*2)
# for i in range(1,11):
#     print("")
#     for j in range(1,11):
#         print(f"{i}x{j}={i * j}",end="\t")

# # Döngü kırıcı ve ya atlatıcı :
# 1.continue: döngüde continue görüldüğünde o anki iterasyon devam etmez sonraki iterasyona atlanır.

# for i in range(10):
#     if i ==7:
#         continue
#     print(i)
#print kısmını en sona yazmak zorundayız.en başa yazdığımızda continue işe yaramamş olur.
# 2.break: döngüde break görüldüğünde döngüden tamamen çıkılır."yani döngü tamamen kırılmış olur".
# for i in range(10):
#     if i==3:
#         break
#     print(i)
# print("buradaki kodlar okunur.")

# ----------> 2.While:
# while döngüsünde koşul doğru(true) olduğu sürece döngü çalışmaya devam eder.
'''
while kosul:
    #işlemler
    
**** koşulda sonsuz döngüye girecek yapıları yönetmemiz gerekir yoksa sonsuz döngüye gireriz.***  
'''

# while ile 1'den 10' a kadar sayıları yazdırın.
# sayac=1
# while sayac < 10:
#     print(sayac)
#     sayac +=1

# Kullanıcı hayır yazana kadar merhaba dünya yazan uygulamayı yazınız.
# devam_mi="evet"
# while devam_mi=="evet":
#     print("merhaba dünya")
#     devam_mi=input("devam etmek istiyor musunuz? evet/hayır")

# kullanıcı hayır diyene kadar rastgele sayı üreterek (1-100) ekranda gösteren uygulamayı yazınız.

# # 1.yöntem:
# import random as rnd
# while True:
#     print(f"Üretilen:{rnd.randint(1,100)}")
#     input("Çıkmak için hayır yazınız.")
#     if girilen =="hayır":
#         break
#
# # diğer yöntem
# devam_mi="e"
# while devam_mi=="e":
#     print(f"Üretilen :{rnd.randint(1,100)}")
#     devam_mi=input("devam etmek için e yazınız.")

# kullanıcıdan bir sayı alınız,girilen değer 0-10 aralığında ise doğru giriş değilse doğru giriş yapana kadar karşı taraftan bilgi istemeye devam eden programı ekrana yazdırınız.
#  benim yaptığım:
# kullanici=int(input("Bir sayı sayı giriniz:"))
# sayac=0
# while sayac < 10 :
#     print(f"girilen sayı 0-10 arasında : Doğru giriş!")
#     if (kullanici<0) and (kullanici> 10) :
#         print(f"Giriş bilgileriniz doğru değil.")
#     else:
#         print("Tekrar bir sayı giriniz:")


# # 2.yöntem:
# while True:
#     sayi=int(input("Bir sayı giriniz:"))
#     if 0 <= sayi <=10:
#         print("doğru giriş yapıldı.")
#         break
#     else:
#         print("yanlış giriş yapıldı.1-10 arasında bir sayı giriniz.")
#
# # 3.yöntem:
# sayi=-1
# while not 0 <= sayi <= 10 :
#     sayi=int(input("1-10 arasında bir sayı giriniz."))
# print("doğru giriş yapıldı.")

# rastgele 4 haneli bir doğrulama kodu belirleyiniz. ve ekranda bu değer gösteriniz.Kullanıcıdan bu kodu doğru bir şekilde girmesini isteyiniz ve doğru giriş yapılana kadar uyarı veriniz.
# 1000-999
#
# import random as rnd
# kod=rnd.randint(1000,9999)
# print(f"üretilen kod:{kod}")
# giris_dogru_mu=False
# while not giris_dogru_mu:
#     girilen_kod=int(input("Kodu yazınız:"))
#     if girilen_kod != kod:
#         print("Yanlış giriş yapıldı,yeniden deneyiniz.")
#     else:
#         print("giriş başarılı.")
#         girilen_kod=True    ## yerine Break de yazılabilir.
# #
# diğer yöntem:
# geliştirme: her yanlış girildiğinde yeniden kod üretilerek gösterilsin.
# import random as rnd
# kod=rnd.randint(1000,9999)
# print(f"üretilen kod:{kod}")
# girilen_kod=int(input("Kodu giriniz:"))
# while kod !=girilen_kod:
#     kod = rnd.randint(1000, 9999)
#     print(f"üretilen kod:{kod}")
#     girilen_kod=int(input("Kodu giriniz"))
# print("giriş başarılı.")

# rastgele 4 haneli bir doğrulama kodu belirleyiniz. ve ekranda bu değer gösteriniz.Kullanıcıdan bu kodu doğru bir şekilde girmesini isteyiniz ve 3 kez yanlış giriş yapılırsa hakkınız tükendi uyarısını veriniz
# import random as rnd
# kod=rnd.randint(1000,9999)
# print(kod)
# sayac=0
# girilen=int(input("Kodu giriniz:"))
# while kod !=girilen:
#     sayac+=1
#     if sayac == 3:
#         print("3 giriş hakkınız tükendi")
#         break
#     else:
#         girilen=int(input("Kodu giriniz:"))
# if kod ==girilen :
#     print("giriş başarılı.")

# vize final notları girilirken 0-100 aralığında girilmesini isteyiniz.eğer vize doğru girildiyse final notunu isteyiniz.her bir notu girerken 0-100 aralığında alana kadar notları yeniden isteyiniz.
# her ikisi de doğru girildiyse ortalama hesaplayıp gösteiniz.

# #  bu benim yaptığım :
# vize=float(input("0-100 aralığında ki vize notunu giriniz:"))
# final=float(input("0-100 aralığındaki final notunu giriniz:"))
# ortalama=(vize*0.4+final*0.6)
# sayac=0
# while vize < 100:
#     print("Vize notunu tekrar giriniz.")
#     if vize>=0 and vize <=100:
#         print("vize notunuzu doğru girdiniz")
#         while final< 100:
#             print("final notunu tekrar giriniz")
#             if final>=0 and final <=100:
#                 print("final notunuzu doğru girdiniz.")
#             else:
#                 print(final)
#                 break
#     else:
#         print(vize)
#
# print(f"vize:{vize},final:{final},ortalama:{ortalama}")


# # hocanın çözümü:
# vize=-1
# while not 0 <=vize <=100:
#     vize=float(input("vize giriniz:"))
#
# final=-1
# while not 0<= final <=100:
#     finaş=float(input("final giriniz:"))
#
# ort=vize*0.4+final*0.6
# print(ort)


# Ödev:
# sayı tahmini uygulaması
# 1-10 arasında rastgele bir sayı üretilir ekranda gösterilmez.kullanıcıdan o sayıyı tahmin etmesi istenir
# .3 kez tahmin etme hakkı olur.Hakları bittiğinde game over!yanlış girdikçe yeni tahminler( kalan hakkı kadar) yapabilir.
# sayıyı bildiğinde ise tebrikler uyarası verilir.

import random as rnd
rasgele_sayi=rnd.randint(1,10)
tahmin_sayi = 0
while True:
    sayi = int(input("Lütfen 1-10 arasında bir rasgele sayı giriniz:"))
    tahmin_sayi+=1
    if  tahmin_sayi==3:
        print("Game over")
    elif sayi==rasgele_sayi:
        print("Tebrikler")
        break
    else:
        print("Lütfen tekrar giriniz:")

# Hocanın çözümü:
import random as rnd
rastgele_uretilen_sayi=rnd.randint(1,10)
print(rastgele_uretilen_sayi)
for i in range (3):
     kullanicinin_tahmini=int(input("Tahmini giriniz:"))
     if kullanicinin_tahmini==rastgele_uretilen_sayi:
        print("bildiniz")
        break
     else:
        print("Yanlış tahmin ettiniz.")

# Alternatif çözümü:
kalan_hak=3
while kalan_hak >0 :
    kalan_hak-=1
    kullanicinin_tahmini=int(input("Tahmini giriniz:"))
    if kullanicinin_tahmini==rastgele_uretilen_sayi:
        print("bildiniz")
        break
    else:
        print("Yanlış tahmin ettiniz.")
    if kalan_hak==0:
        print("game over")

# --------------------------------------------
import random as rnd

rastgele_uretilen_sayi = rnd.randint(1, 10)
kalan_hak = 3
girilen = "e"
while girilen != "h":
    kalan_hak -= 1 # 3 2   2 1   1 0
    kullanicinin_tahmini = int(input("Tahmini giriniz:"))
    if kullanicinin_tahmini == rastgele_uretilen_sayi:
        print("bildiniz")
        break
    else:
        if kullanicinin_tahmini > rastgele_uretilen_sayi:
             print("Tahmini düşürün!")
        else:
            print("Tahmini büyütün!")
    if kalan_hak == 0:
        print("game over!")
        girilen = input("Yeni bir oyun oynamak istiyor musunuz? e/h")
        rastgele_uretilen_sayi = rnd.randint(1, 10)
        kalan_hak = 3










