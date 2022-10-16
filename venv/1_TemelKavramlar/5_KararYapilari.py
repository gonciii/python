# # Karar Yapıları
# # if-else
# # if :verilen koşul True ise ise çalışıcak blok,else: False ise çalışıcak blok
# '''
# if kosul:
#     True iken yapılacak işlemler
#
#
#
# if kosul:
#     True iken yapılacak işlemler
# else :
#     False iken yapılacak işlemler
# 1 girinti =1 tab
# '''
#
# kullanici_adi = input("Kullanıcı adınızı giriniz:").lower()
# if kullanici_adi == "bilgeadam":
#     print("Hoşgeldiniz!")
# else:
#     print("lütfen kullanıcı adını kontrol ediniz.")
#
# '''
# if kosul1:
#    kosul1 True ise yapılacaklar
# elif kosul2:
#    kosul2 True ise yapılacaklar
# elif kosul3:
#    kosul3 True ise yapılacaklar
# else:
#     hiç bir koşul True değilse
# '''
# region Girilen bir sayının negatif/pozitif olması durumunu kontrol ediniz.ve ekranda durumunu gösteriniz.
# cast=convert
# sayi1 = int(input("Bir sayı giriniz:"))
# if (sayi1 < 0):
#     print("Girdiğiniz sayı negatiftir.")
# elif (sayi1 > 0):
#     print("Girdiğiniz sayı pozitiftir.")
# elif (sayi1 == 0):
#     print("Girdiğiniz sayı 0 eşittir.")
# else:
#     print("başka bir sayı giriniz")
# endregion
#
# girilen_sayi = int(input("Bir sayı giriniz"))
# if girilen_sayi > 0:
#     print(f"{girilen_sayi} sayısı pozitiftir.")
# elif girilen_sayi == 0:
#     print(f"{girilen_sayi} sayısı sıfırdır.")
# else:
#     print(f"{girilen_sayi} sayısı negatiftir.")
#
# region Girilen bir sayının çift/tek olmasını bulunuz ve ekrana yazdrınız.
#
# sayi1 = int(input("Bir sayı giriniz:"))
# if sayi1%2==0:
#     print(f"{sayi1} sayısı çifttir.")
# else:
#     print(f"{sayi1} sayısı tektir.")
# #endregion
#
# region Girilen bir x sayısının,yine kullaıcıdan istenen bir y sayısına tam bölünüp bölünmediğini kontrol ediniz ve ekranda göteriniz.
#
# sayi1 = int((input("Bir sayı giriniz:")))
# sayi2 = int((input("İkinci sayıyı giriniz:")))
# if sayi2 == 0:
#     print("Lütfen 0 dışında bir sayı giriniz.")
# else:
#     islem = sayi1 % sayi2
#     if islem == 0:
#         print(f"{sayi1},{sayi2}'in tam katıdır.")
#     else:
#         print(f"{sayi1}'in,{sayi2}'e bölümünden kalan {islem}'dir.")
# endregion
#
# Girilen iki sayıdan hangisinin büyük olduğunu bulan uygulamayı yazınız.
# sayi1 = int(input("Birinci sayıyı giriniz:"))
# sayi2 = int(input("İkinci sayıyı giriniz:"))
# if (sayi1 > sayi2):
#     print(f"{sayi1} büyüktür.")
# elif (sayi1 < sayi2):
#     print(f"{sayi1},küçüktür.")
# else:
#     print("sayılar biribine eşittir")
#
# Girilen vize notunun 0-100 arasında olmasını kontrol ediniz.eğer doğru giriş yapıldıysa giriş başarılı uyarsını gösterelim.eğer ortalama 50 ve üzerinde ise geçti değilse kaldı yazdıralım.
# veya kısaca
# if 0 <= vize <=100 and 0<= final <=100)
#
# vize_notu = float(input("Vize notunuzu giriniz:"))
# final_notu=float(input("Final notunu giriniz:"))
# if (vize_notu >=0 and vize_notu <= 100) and (final_notu >=0 and final_notu <=100 ) :
#     print("giriş başarılıdır.")
#     ortalama=(vize_notu * 0.4)+(final_notu * 0.6 )
#     print(f"ortalamanız:{ortalama}")
#     if (ortalama > 50):
#         print("not geçerlidir.")
#     else:
#         print("not geçersizdir.")
#
# else:
#     print("lütfen 0-100 aralığında bir sayı giriniz)
'''
 Eğer ortalama:
  0-30 aralığında ff
  31-50 DD
  51-70 CC
  71-90 BB
  91-100 AA
harf notunu belirleyen ve ortalama ile birlikte ekranda gösteren uyglamayı yazınız.
'''

# vize_notu = float(input("Vize notunuzu giriniz:"))
# final_notu=float(input("Final notunu giriniz:"))
# ortalama=(vize_notu*0.4)+(final_notu*0.6)
# print(f"ortalamanız:{ortalama}")
# if (ortama >=91 and ortalama <=100): # 91<=ortalama<=100
#    print("Harf notu AA'dır.")
# elif (ortalama >=71 and ortalama <=90):
#    print("Harf notu BB'dir.")
# elif (ortalama >=51 and ortalama <=70):
#    print("Harf notu CC'dir.")
# elif (ortalama >=31 and ortalama <=50):
#    print("Harf notu DD'dir.")
# else:
#    print("Harf notu FF'dir.")

# ekranda çıktıyı vize notu:{} final notu:{} ortalama:{} harf notu:{} şeklinde gösteriniz.
# vize_notu = float(input("Vize notunuzu giriniz:"))
# final_notu=float(input("Final notunu giriniz:"))
# if (vize_notu >=0 and vize_notu <= 100) and (final_notu >=0 and final_notu <=100 ) :
#     ortalama=(vize_notu * 0.4)+(final_notu * 0.6 )
#     harf_notu=""
#     if ortalama>=0 and ortalama<=30:
#        harf_notu="FF"
#     elif ortalama >30 and ortalama <=50:
#        harf_notu="DD"
#     elif ortalama >50 and ortalama <=70:
#        harf_notu="CC"
#     elif ortalama <70 and ortalama <=90:
#        harf_notu="BB"
#     else:
#        harf_notu="AA"
#        print(f"Vize notu:{vize_notu}\n final notu:{final}\n ortalama:{ortalama}\n harf notu:{harf_notu}")
# else:
#     print("Lütfen 0-100 aralığında bir not giriniz.")



# kullanıcıdan kullanıcı ve şifre istedikten sonra ka:admin ve şifre:1234 ise giriş başarılı değilse,hangi bilgi hatalıysa onun uyarısını veren bir uygulama yazınız.
#
# ka=input("Kullanıcı adınızı giriniz:")
# sifre=input("Kullanıcı şifrenizi giriniz:")
#
# if (ka=="admin"and  sifre=="1234"):
#    print("Giriş kullanıcı ismi ve şifre başarılıdır.")
# elif (ka!="admin" and sifre=="1234"):
#        print("Girdiğiniz kullanıcı adı hatalıdır.")
# elif (ka=="admin" and sifre!="1234"):
#        print("Girdiğiniz şifre hatalıdır.")
# else:
#    print("Girdiğiniz bilgileri kontrol ediniz.")


# ka="admin"
# pwd="1234"
# mesaj=""
# if kullanici_adi==ka and sifre==pwd:
#    mesaj="GİRİŞ BAŞARILIDIR."
# elif kullanici_adi!=ka and sifre!=pwd:
#    mesaj="Kullanıcı adı ve şifreniz hatalıdır."
# elif kullanici_adi!=ka:
#    mesaj="Kullanıcı adınız hatalıdır."
# else:
#    mesaj="Şifreniz hatıldır."
#
# print(mesaj)

# Kullanıcıdan sipariş etmek istediğin kitap sayısını alarak indirim uygulayan ve müşteriye ödemesi gereken tutarı,indirim oranını ve indirimsiz fiyatı gösteren uygulamayı yazınız.İndirim oranları aşağıdadır:
'''
birim fiyatı:10 tl
kitap sayısı;
20'den az ise %5 indirim 
20-50 ise %10
50-100 ise %15
100'den fazla ise %24 indirim
'''

# siparis_sayisi=int(input("Sipariş etmek istediğiniz kitap sayısını giriniz:"))
# birim_fiyat=10
# indirim_orani=0
# if 0< siparis_sayisi <= 20:
#    indirim_orani=0.05
# elif 20< siparis_sayisi <=50:
#    indirim_orani=0.10
# elif 50 < siparis_sayisi <=100:
#    indirim_orani=0.15
# else:
#    indirim_orani=0.25
#
# indirimsiz_tutar=birim_fiyat*siparis_sayisi
# indirimli_tutar=(indirimsiz_tutar-(indirimsiz_tutar*indirim_orani))
#
# print(f"Toplam={indirimsiz_tutar},İndirim Oranı={indirim_orani*100},"
#       f"Ödenecek Tutar={indirimli_tutar}")


# Kullanıcıdan almak istediği ürünü isteyerek ürünün hangi reyonda olduğunu gösteren bir uygulama yapınız.
'''
Domates,biber,patlıcan ->Sebze reyonu
Parfüm,diş macunu,şampuan ->Kozmetik
Cep Telefonu,bilgisayar,ses sistemleri ->Teknoloji reyonu
bunlar dışında bir giriş yapılırsa "ürün bulunmamaktadır" uyarısı vericektir.
'''


# urun=input("Almak istediğiniz ürünü giriniz:").lower()
# mesaj=""
# else_bloguna_girdi_mi=False
# if (urun =="domates" or urun=="biber" or urun=="patlıcan"):
#    mesaj="Sebze."
# elif(urun=="parfum" or urun=="sampuan" or urun=="dis macunu"):
#    mesaj="Kozmetik."
# elif(urun=="cep telefonu" or urun=="bilgisayar" or urun=="ses sistemleri"):
#    mesaj="Teknoloji."
# else:
#    mesaj="Ürün bulunmamaktadır."
#    else_bloguna_girdi_mi=True
#
# if not else_bloguna_girdi_mi:
#    print(f"{mesaj} ,reyonuna ilerleyiniz")
# else:
#    print(mesaj)




# rastgele sayı üretmek için :
# import random #dışarıdan bir dosyayı kullanmak için kullanırız.
# r1=random.randint(1,10)
#
# import random as rnd
#
# r2=rnd.randint(1,20)
# print(r1,r2)

# 1-10 arasında rastgele üretilen 3 adet sayının hangisinin büyük olduğuna bulan ve ekranda hem sayıları hem en büyük sayı:{x} gibi yazdıran uygulamayı yazınız.

# import random
# r1=random.randint(1,10)
# r2=random.randint(1,10)
# r3=random.randint(1,10)
# if (r1>r2 and r1>r3):
#     print(f"En büyük sayı:{r1}'dir,{r1},{r2},{r3}")
# elif (r2>r1 and r2>r3):
#     print(f"En büyük sayı:{r2}'dir.{r1},{r2},{r3}")
# else:
#     print(f"En büyük sayı:{r3},dir.{r1},{r2},{r3}")
#
# #Sorunun farklı bir çözümü :
# import random
# r1=random.randint(1,10)
# r2=random.randint(1,10)
# r3=random.randint(1,10)
# en_buyuk_sayi=0
# if (r1>=r2 and r1>=r3):
#     en_buyuk_sayi=r1
# elif (r2>=r1 and r2>=r3):
#     en_buyuk_sayi=r2
# else:
#     en_buyuk_sayi=r3
# print(f"r1={r1}\n r2={r2}\n r3={r3} en büyük olan={en_buyuk_sayi}")
#
# #metot ile yapılan çözümü:
# en_buyuk_sayi=max(r1,r2,r3) #istenilen sayıda parametre alabilir.
# print(en_buyuk_sayi)

# girilen boy ve kilo bilgileri ile beden kitle indekxi hesaplayan bir uygulama yazınız:
# BKI=Kilo/(boy*2)  kilo(kg) boy(m)
'''
# • Beden kitle/kütle indeksi < 18,5 ise Zayıf
# •    18,5 < Beden kitle/kütle indeksi < 24,9 ise Normal
# •    25 < Beden kitle/kütle indeksi < 29,9 ise Fazla kilolu
# •    30 < Beden kitle/kütle indeksi < 34,9 ise I. derece obez
# •    35 < Beden kitle/kütle indeksi < 39,9 ise II. derece obez
# •    Beden kitle/kütle indeksi > 40 ise III. derece obez

'''


#
# kilo=float(input("Kilonuzu giriniz(kg):"))
# boy=float(input("Boyunuzu giriniz(m):"))
# endeks=(kilo/(boy **2),2)
# durum=""
# if endeks < 18.5 :
#     durum="zayıf"
# elif 18.5 <= endeks < 24.9:
#     durum="normal"
# elif 25 <= endeks < 29.9:
#     durum="fazla kilolu"
# elif 30 <= endeks < 34.9:
#     durum="I.derece obez."
# elif 35 <= endeks < 39.9:
#     durum="II.derece obez"
# elif endeks >=40:
#     durum="III.derece obez"
# else:
#     durum="hesaplanamadı"
#
# print(f"Boy:{boy*100}cm Kilo:{kilo} kg Endeks:{endeks} Durum:{durum}")



# Match-case: 3.10 sürümünde geldi.switch case yapısının karşılığıdır.
'''
match karsılastırma_yapilacak_degisken:
    case karsilastirilacak_deger1:
        islemler
    case karsilastirilacak_deger2:
        islemler
    case _:
        hicbirine uymazsa burası çalışır
'''

# kullanıcıdan haftanın her gününü alıp o günün sayısal karşılığını verelim (pazartesi: haftanın 1.günü)
# gun=input("Gün giriniz:")
# if gun=="Pazartesi"
#     print("Haftanın 1.günü")
# elif gun=="salı"
#     print("Haftanın 2.günü")
# # ...
# # else:
# #    print("BÖYLE BİR GÜN BULUNAMADI ,LÜTFEN KONTOL EDİNİZ.)

# gun=input("Gün giriniz:")
# match gun:
#     case "pazartesi":
#         print("Haftanın 1.günü")
#     case "salı":
#         print("Haftanın 2.günü")
#     case "çarşamba":
#         print("Haftanın 3.günü")
#     # ...
#     case _:
#         print("Böyle bir gün bulunamadı.lütfen kontrol ediniz")


# or ile match kullanımı (pipe işareti -alt gr + z'nin solundaki tuş)
# kllanıcıdan alamk istediği ürünü isteyerek ürünün hangi reyonda olduğunu gösteren bir uygulama yapınız.
'''
# Domates,biber,patlıcan ->Sebze reyonu
# Parfüm,diş macunu,şampuan ->Kozmetik
# Cep Telefonu,bilgisayar,ses sistemleri ->Teknoloji reyonu
# bunlar dışında bir giriş yapılırsa "ürün bulunmamaktadır" uyarısı vericektir.
# '''
# urun=input("Aradığınız ürünü giriniz:").lower()
# match urun:
#     case"domates"| "biber"| "patlıcan":
#         print("sebze reyonu")
#     case"parfüm"| "şampuan" |"diş macunu":
#         print("Kozmetik reyonu")
#     case _:
#         print("ürün bulunmamaktadır.")


# and ile match örneği:
# kullanıcıdan kullanıcı ve şifre istedikten sonra ka:admin ve şifre:1234 ise giriş başarılı değilse,hangi bilgi hatalıysa onun uyarısını veren bir uygulama yazınız.

kullanici_adi=input("Kullanıcı adınızı giriniz:")
sifre=input("Kullanıcı şifrenizi giriniz:")
match kullanici_adi:
    case "admin":
        match sifre:
            case"1234":
                print("Giriş başarılıdır")

            case _:
               print("şifreniz yanlıştır")

    case _:
        print("Kullancı adınız yanlış")

# if 1==1:
#    pass

