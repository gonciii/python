# #SIFIRDAN PYTHON DERSLERİ
# # FONKSİYONLAR
# # ÇOK SATIRLI İŞLEMLER İÇİN ASLINDA DAHA ERİŞEBİLİR VE KOLAY OLMASINI SAĞLAR.
# # KULLANIMI
# def bilgi_ver(): #fonskiyonumu tanımlıyoruz.
#     print("İşlem başarılıdır.")
#
# bilgi_ver() #fonskiyonu çağırıyoruz.
#
# def selamla():
#     print("Merhaba")
#
# selamla()  #yine çağırma işlemi yapılır.her çağırdığımda aynı şey gelicek.
#
# # fonksiyona parametre eklersek:
# def selamla(isim): #fonskiyona parametre ekledik.
#     print("Merhaba "+ isim)
# selamla("gonca") #parametre ile çağırdık.
# # 2 tane parametre eklersek:
# def topla(x,y):
#     print(f"x+y={x+y}")
# topla(10,15)   #x+y=25
#
# def carp(x,y):
#     print(f"x*y={x*y}")
# carp(10,10)  #x*y=100
#
# def cikarma(x,y):
#     print(f"x-y={x-y}")
# cikarma(8.7,3) #x-y=5.699999999999999
#
# def bolme(x,y):
#     print(f"x/y={x/y}")
# bolme(8,2) #4.0
#
# def ortalama_goster(liste):
#     toplam=sum(liste)
#     adet=len(liste)
#     ortalama=toplam/adet
#     print(f"Girilen listenin ortalaması:{ortalama}")
# ortalama_goster([1,2,3,4,5,6,7])
#
# def buyuk_harfe_cevir(metin):
#     metin=metin.upper()
#     print(metin)
# buyuk_harfe_cevir("abc") #ABC
# buyuk_harfe_cevir("gonca") #GONCA
#
# def kucuk_harfe_cevir(metin):
#     metin=metin.lower()
#     print(metin)
# kucuk_harfe_cevir("GONCAGÜL") #goncagül
#
# def selamla(mesaj,isim="Anonim"):
#     print(f"{mesaj} {isim}")
#
# selamla("Merhaba") #Merhaba Anonim
# # varsayılan neyse onu kullanıcak.
#
# def indirim_yap(urun,yuzde):
#     indirim_orani=urun*(yuzde/100)
#     indirimli_fiyat=urun-indirim_orani
#     print(f"Ürünün indrimli fiyatı :{indirimli_fiyat},Ürünün indirim oranı :{indirim_orani}")
# indirim_yap(100,10) #Ürünün indrimli fiyatı :90.0,Ürünün indirim oranı :10.0
#
# # return:geri döndürmek istediğimizde kullanırız.
# def ortalama_hesapla(x,y):
#     return (x+y)/2
# ortalama_hesapla(8,10)  #ekranda göstermiyor ama arka planda hesaplıyor.
# print(ortalama_hesapla(8,10)) # hesapladı ve yazdırdık 9.0
# a=ortalama_hesapla(2,4)
# b=ortalama_hesapla(3,7)
# print(ortalama_hesapla(a,b))  #4.0
#
# def buyuk_harfe_cevir(metin):
#     return metin.upper()
# print(buyuk_harfe_cevir("gonca")) #GONCA
# b=buyuk_harfe_cevir("çomak")
# print(b) #ÇOMAK
#
# # geçen haftanın tekrarı:
# #Mtematiksel metotlar:
# #random sayı tanımlarken nasıl import random as rnd gibi bir şey tanımlıyorsak burda da math method için:
# # "import math " tanımlamasını yapıyoruz.
# #örneğin pi sayısını nasıl hesaplarız ?
# # import math
# # pi_sayisi=math.pi
# # print(pi_sayisi)  # 3.141592653589793 ya da
# # import math as m
# # pi_sayisi=m.pi
# # print(pi_sayisi)  #3.141592653589793
# # import math as e
# # e_sayisi=e.e
# #print(e_sayisi)   #2.718281828459045
# # KULLANILAN METOTLAR NELERDİR?
# #1-) floor(): bir alt tamsayına yuvarlanmasını sağlar.floor içine bir değer almak zorunda.
#
# import math as m
# pi_sayi1=m.pi
# print(pi_sayi1)  #3.141592653589793
# print(m.floor(pi_sayi1))  #3 --->bir alt tamsayıya yuvarladı.
# print(m.ceil(pi_sayi1))   #4 --->bir üst tam sayıya yuvarladı.
#
# #2-) ceil(): bir üst tam sayıya yuvarlanmasını sağlar aynı şekilde ceil da içine bir değer alır.
# import math as eular
# e_sayisi=eular.e
# print(e_sayisi)   #2.718281828459045
# print(eular.ceil(e_sayisi))  #3
# print(eular.floor(e_sayisi)) #2
#
# #3-) round():ondalıklı sayının ondalık kısmı eğer 50 ise sayıyı çifte yuvarlar.
# sayi1=float(2.50)
# print(sayi1.__round__())  #---> 2
# sayi2=float(15.50)
# print(sayi2.__round__())  #----> 16
# sayi3=3.758
# print(sayi3.__round__())  #---> 4
#
# # min,max,any,sum,len...diğer metotlar
#
# #4-) fabs():mutlak değeri alır.içine değer alır.
# import math as a
# print(a.fabs(-100))  #--->100.0
# print(a.fabs(-1234))  #1234.0
#
# # 5-)pow üssünü almak için kullanılır.içine değer alır.
# import math as x
# print(x.pow(2,2))  #4
# print(x.pow(4,4))  #256
#
# # 6-) sqrt():kareköküünü verir
# print(x.sqrt(256))  #16
# print(x.sqrt(16))   #4
#
# #7-) fsum(): içindeki değerleri toplar.
# print(x.fsum([10,11,20]))  #41.0
#
# #8-) radians(): radians aslında trigonometrik dönüşümleri yapabilmek için kullanıyoruz.
#
# import math as x
# print(x.sin(x.radians(30)))   #0.49999999999999994
# print(x.cos(x.radians(30)))   #0.8660254037844387
# print(x.tan(x.radians(30)))   #0.5773502691896257
#
# # 9-) sin,cos,tan :parametre olarak radyan cinsinden değer alır
# # print(m.sin(30)) #tam değer vermez
# # print(m.cos(m.radians(180)))  #-1.0
#
# #10-) degree():derece cinsine cevirir.
#
# # print(m.degrees(r_30))    #29.999999999999996
#
# #11-) factorial(): faktöryel alır
#
# import math as f
# print(f.factorial(5))  #120
# print(f.factorial(3))  #6
#
# #12-) exp(): e sayısının üssünü alır
# import math as e_sayi
# print(e_sayi.exp(2))   #7.38905609893065
#
# #13-) isnan():float ya da int değer alır. #NaN:not a number
# import math as a
# print(a.isnan(10))  #false
# print(a.isnan(a.nan))  #true -----> NaN:not a number.!!

#DATETİME METOTLARI:

'''
date time metotlarında : zaman,saat ve tarihle ilgili işlemler yapılabilir.
date sınıfı: tarihle ilgili işlemler
time sınıfı: zamanla ilgili işlemler
datetime sınıfı :date ve time sınıflarının birleşimde ki işlemleri yapmak için kullanılır.
#pythonda c:class v:variable ve f:function anlamına gelir.
#rastgele sayı üretirken: import random as rnd
#matematiksel metotlarda : import math as m
#datetime metotlarda ise : import datetime as dt kullanılır.
'''
import datetime as dt
# dt.date.fromtimestamp() : içinde ayrıntılı tarih bilgsi barındıran bir zaman damgasıdır.
# dt.date.strftime() : tarih ve zaman bilgileri.iki parametre alır.
# dt.date.replace()  :
# dt.time.strptime() :
#gibi uzun uzun yazmak yerine :
#----from datetime import datetime #komutunu vererek datetime modülü içindeki datetime adlı sınıfı içeri aktarırız.

from datetime import datetime as dt
# ŞİMDİKİ ZAMAN :
print(dt.now())   #2022-11-18 16:25:43.482948
# BUGÜNÜN TARİHİ :
print(dt.today()) #2022-11-18 16:26:50.472552

from datetime import date as d
print(d.today())  #2022-11-18

# tarih nasıl oluşturulur ? "2022-11-12"
import datetime as dtm
print(dtm.date(2022,11,12))  #2022-11-12

'''
NOTE: TR de gün-ay-yıl
      EN de ay-gün-yıl
gun=tam_zaman.day
yil=tam_zaman.year
ay=tam_zaman.month
FORMAT İÇİN KULLANILAN KISALTMALAR:
%Y :year --yıl
%m :month --ay
%d :day --gün
%H: hour----saat
%M :minute---dakika
%S :seconda---saniye
      
'''
#date kısmını anlamadım ayrıca video izle.....


#CUSTOM METOTLAR:
'''
# Pythonda metot tanımlamak için "def" anahtar kelimesi kullanılır.
# Metotlar çağırılarak çalıştırılırlar.
# Sıralama önemlidir
# Önce metot tanımlanacak !
# Parametreli veya parametresiz metotlar tanımlanabilir.
# Eğer parametre alıyorsa veri tipinin tanımlaması zorunlu değildir.
'''
#1-) GERİ DEĞER DÖNMEYEN METOTLAR:
#1.A) PARAMETRESİZ :
def selamla(): # önce fonksiyonu tanımlıyoruz,parametre yok !
    print("Hello WORLD !")  # yazdırmak isteiğimiz mesaj
selamla()                   #fonksiyonu çağırıyoruz.. #Hello WORLD !

def seslen():
    print("HOŞGELDİNİZ !!")
seslen()     #HOŞGELDİNİZ !!

#1.B) PARAMETRELİ :
def selamla1(mesaj:str):
    print(mesaj)
selamla1("selam")

def topla():
    print(5+8)
topla()    #13

def summary(a:int,b:int):
    print(f"a+b={a+b}")
summary(5,6)   #a+b=11

# 2-)GERİ DEĞER DÖNEN METOTLAR:
#1.A) PARAMETRESİZ:
#return anahtar kelimesi geriye değer döndürüyor.
def topla1() ->float:
    toplam=4+5
    return float(toplam)
topla1()
print(topla1())   #9.0
t=topla1()
print(t)          #9.0
# # bir metottan bir değer döner.
# # return toplam,fark,üs gibi birden fazla değer döndüremez.
# # Dict kullanarak yapabiliriz.

def bol()->float:
    bolme=12/2
    return float(bolme)
bol()
print(bol())  #6.0

#2.B) PARAMETRELİ:
def summary1(a:int,b:int)->float:
    toplam=a+b
    return float(toplam)
    #print("it is over") ---->>>> returnden sonraki kodlar çalışmaz....
summary1(5,9)
print(summary1(5,9))     #14.0
t2=summary1(90,54)
print(t2)                #144.0
#NOT : sistemde hazır olamayan kodları daha modüler kullanabilmek için aslında custom metotları kullanıyoruz.!






























