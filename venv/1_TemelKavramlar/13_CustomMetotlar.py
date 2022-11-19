#Custom Metotlar:
# Pythonda metot tanımlamak için "def" anahtar kelimesi kullanılır.
# Metotlar çağırılarak çalıştırılırlar.
# Sıralama önemlidir
# Önce metot tanımlanacak !
# Parametreli veya parametresiz metotlar tanımlanabilir.
# Eğer parametre alıyorsa veri tipinin tanımlaması zorunlu değildir.

# 1-)GERİ DEĞER DÖNMEYEN METOTLAR
# 1.a-) PARAMETRESİZ
'''
KULLANIM ŞEKLİ;
# metot adı: snake_case notasyonu ile tanımlanır.
def metot_adi():
    metodun yapacağı işlemler

-metot=fonksiyon
-fonksiyon kendi başına tanımlanan bir yapıdır.
-metot da bir fonksiyondur.
-Bir classın içinde tanımlanıyorsa metot oluyor.
-ikiside aynı şeyi yapıyor.
-ÖNCE ÇAĞIR SONRA TANIMLA

'''
# NOT: ÇOĞU ZAMAN EMİR KİPLERİ ŞEKLİNDE KULLANILIR.
# bir kez tanım yapıyoruz çoğu kez kullanıyoruz.
# metot overload yoktur.overload:aynı metot adı ile parametreleri değişicek şekilde birden fazla metot yazılmasıdır.
# aşırı yükleme yapılmıyor.
# --------------Örnek:
# def selamla():
#            print("Merhaba Dünya!")
# selamla()    #Merhaba Dünya!
#
# # 1.b-) PARAMETRELİ
# # --------------Örnek:
# def selamla1(mesaj:str):
#     #mesaj değişkenini metot içinde istediğimiz gibi kullanabiliriz.
#     print(mesaj)
#
# selamla()  #statik olarak : #Merhaba Dünya!
# selamla1("Hello World!")    #Hello World!
# selamla1("Naber?")          #Naber?
# # Örnek:Toplama işlemi metodu yazalım.
# def topla():
#     print(4+5)
# def summary(a:int,b:int):
#     try:
#         a=int(a)
#         b=int(b)
#         toplam=a+b
#         print(toplam)
#     except:
#         print("çevrilmeyen bir değer gönderildi")
# topla()
# summary("1a0","20")         #çevrilemeyen bir  değer göndrildi.
# summary(10,20)             #30
# #summary("10",20)          #error verir.
#
#
# #
# # # 2-) GERİ DEĞER DÖNEN METOTLAR
# # # 2.a-) PARAMETRESİZ
# # # return:geriye değer döndürüyor.
# # def topla1()-> float:
# #     '''sabit olarak 4 ve 5 değerini toplayarak sonucu döner.'''
# #     toplam=4+5
# #     return float(toplam)  #float sayesinde 9.0 döndürürüz.
# #
# # t=topla1()
# # print(t)    #9
# # print(topla1())   #9
# # #print(topla())    #None:değer dönmüyormuş demektir.ancak çağırım yapabilir.
# #
# # # bir metottan bir değer döner.
# # # return toplam,fark,üs gibi birden fazla değer döndüremez.
# # # Dict kullanarak yapabiliriz.
# #
# #
# #
# # # 2.b-) PARAMETRELİ
# #
# # def summary1(a:int,b:int) -> float:
# #     toplam=a+b
# #     return float(toplam)
# #     print("bitti")
# # # returnden sonra kodlar çalışmaz.
# # # Tek bir değeri vardır.değer döndürmek !!
# # t2=summary1(10,20)
# # print(t2)     #30.0
# # print(t2**2)  #900.0
#
# #NOT : sistemde hazır olamayan kodları daha modüler kullanabilmek için aslında custom metotları kullanıyoruz.!!
#
# # Örnek:
# # s1:2 float parametre alarak bu sayıların farkını alan ve ekranda
# # gösteren bir metot tanımlayınız.(geri değer dönmeyen)
# # def fark_al(sayi1:float,sayi2:float):
# #     fark=sayi1-sayi2
# #     print(fark)
#
# # fark_al(10,20.4) #-10.399999999999999---->>  #burda metotu çağırıyoruz,tekrar print dememize gerek yok.
# # fark_al(50,21)  #29
# # ---------------------------------------------
# # s1=float(input("Birinci sayıyı giriniz:"))
# # s2=float(input("İkinci sayıyı giriniz:"))
# # fark_al(s1,s2)
# # ----------------------------------------------
# # Programlama dillerinde uyulması gereken 5 tane prensib.
# # Not: SOLID: S,O,L,I,D hepsi farklı bir kuraldır.
# # S:single responsibility:tek sorumluluk prensibi,yazılan bir kodun(class,method vb)tek bir amaca hizmet etmesi.
# # def dort_islem_yap(a,b):
# #     toplam=a+b
# #     fark=a-b
# #     bolum=a/b
# #     carpim=a*b
# #     sonuc={
# #         "toplam":toplam,
# #         "fark":fark,
# #         "carpim":carpim,
# #         "bolum":bolum
# #
# #     }
# #     return sonuc
# # print(dort_islem_yap(10,20))
#
# # olması gereken :
# def topla(sayi1:float,sayi2:float):
#     toplam=sayi1 + sayi2
#     return toplam
# def cikar(sayi1:float,sayi2:float):
#     fark=sayi1-sayi2
#     return fark
# def carp(sayi1:float,sayi2:float):
#     carpim=sayi1*sayi2
#     return carpim
# def bol(sayi1:float,sayi2:float):
#     try:
#         bolum = sayi1 / sayi2
#         return bolum
#     except:
#         raise Exception("sayi2 0 olamaz !")
#
# # diğer bir yazım şekli:
# def dort_islem(a:float,b:float):
#     toplam=topla(a,b)
#     fark=cikar(a,b)
#     carpim=carp(a,b)
#     bolum=bol(a,b)
#     sonuc={
#      "toplam": toplam,
#      "fark":fark,
#      "carpim":carpim,
#      "bolum":bolum
#     }
#     return sonuc
# # burda 10,0 gibi bir şey yaparsak.0'a bölme hatası verir.
# s=dort_islem(10,20)
# print(s)
# print(s["fark"])
# print(s["bolum"])
# print(bol(10,20))
#
# # ÖRNEK:
# # 1-) 1'den dışarıdan parametre olarak alınan bir sayıya kadar olan çift sayıları ekrana gösteren bir metot yazınız.
# # 2-)update:Listeye atan ve o listeyi dönen metot yazınız.
#
# # 1-) çözümü:
# # parametre alan ve geri değer döndürmüyor
# def ciftleri_yazdir(bitis:int):
#     for i in range(1,bitis+1):
#         if i%2==0:
#             print(i)
# ciftleri_yazdir(10)
#
# # listeye atan ve o listeyi dönen metot:
# def ciftlerin_listesini_getir(bitis:int)->list:
#     liste=[]    #ramde listenin ölmesi için bu kısma gelmesi lazım.
#     for i in range(1,bitis+1):
#         if i%2==0:
#             liste.append(i)
#     return liste
#
# ciftler=ciftlerin_listesini_getir(10)
# print(ciftler)
#
# # ÖRNEK:
# # parametre olarak ad,soyad,uzanti alarak ad.soyad@uzanti şeklinde
# # mail oluşturan ve dönen bir metot tanımlayınız.
# # (türkçe karakterleri dönüştürünüz tümü küçük harf olmalı)
# # ÇÖZÜM:
# def turkce_karakterli_cevir(metin:str):
#     metin=metin.replace("ö","o").replace("ü","u").replace("ç","c").replace("ğ","g").replace("ş","s").replace("ı","i")
#     return metin
# def mail_olustur(ad:str,soyad:str,uzanti:str):
#     #ad=turkce_karakterleri_cevir(ad)
#     #soyad=turkce_karakterleri_cevir(soyad)
#     mail=turkce_karakterli_cevir(f"{ad}.{soyad}@{uzanti}".lower().replace(' ',""))
#     return mail
# #print(mail_olustur("gonca gül","çomak","bilgeadam.com"))
#
# # Türkçe karakterleri eng.karaktere çeviren bir metot tanımlayabilirsiniz ve mail oluşturucunun içinde kullanabilrsiniz.
#
# personel_listesi=[
#     {
#         "ad":"nur",
#         "soyad":"öztürk"
#     },
#     {
#         "ad":"damla",
#         "soyad":"kahraman"
#
#     },
#     {
#         "ad":"mert",
#         "soyad":"boylu"
#      },
#     {
#         "ad":"neslihan",
#         "soyad":"kaptan yorübulut"
#     }
#
# ]
# # bilgeadam.com -> yukarıdaki listede yer alan tüm personellere mail oluşturucu metot yardımı ile
# # mailler oluşturunuz ve listeye ekleyiniz.
#
# mail_listesi=[]
# for personel in personel_listesi:
#     pa=personel["ad"]  #personel.get("ad")
#     ps=personel["soyad"]
#     mail=mail_olustur(pa,ps,"bilgeadam.com")
#     mail_listesi.append(mail)
#
# print(mail_listesi)
#
# # update:dışarıdan parametre olarak bir dict. listesi alan ve tüm listedeki
# # çalışanlar için mail oluşturupu liste olarak dönen method yazınız.
# # sürekli liste geldiğini düşünerek methoda çevirmek.
# def mail_olustur1(personel_listesi:list):
#     mailler=[]
#     for personel in personel_listesi:
#         mailler.append(mail_olustur(personel["ad"],personel["soyad"],"bilgeadam.com"))
#         return mailler

#print(mail_olustur1(personel_listesi))
#print(mail_olustur("gonca","çomak","bilgeadam.com"))

# ['nur.ozturk@bilgeadam.com', 'damla.kahraman@bilgeadam.com', 'mert.boylu@bilgeadam.com', 'neslihan.kaptanyorubulut@bilgeadam.com']
# bu formatta gelen mail listesinin ad ve soyadı ayrıştırıp personel listesi şeklinde dönen bir metot yazınız.
# p_list=[{"ad":"nur","soyad":"öztürk"}]
# split kullanıcaz.

def mailleri_ayristir(mailler:list)->list:#liste şeklinde tanımlıyoruz.
    personeller=[]
    for mail in mailler:  #mailler listesi içinde dolaşıyoruz.
        ilk_eleman=str(mail).split("@")[0]  #nur.öztürk
        ayrismis_elemanlar=ilk_eleman.split(".") #0-> ad 1-> soyad
        personel={
            "ad":ayrismis_elemanlar[0],
            "soyad":ayrismis_elemanlar[1]
        }
        personeller.append(personel)
        return personeller

mailler=['nur.ozturk@bilgeadam.com', 'damla.kahraman@bilgeadam.com', 'mert.boylu@bilgeadam.com', 'neslihan.kaptanyorubulut@bilgeadam.com']
mailleri_ayristir(mailler)
#print(mailleri_ayristir(mailler))
#geri değer dönmeyen metotları print ettirmek isterseniz None değeri döner.

#Örnek:
#Bir metot istiyoruz; parametre olarak bir metin(str) alan ve bu metin içindeki sesli ve sessiz harfleri ayırarak hem sayısını hem harfleri gösteren bir metor yazınız.
# merhaba dünya ! ->sesliler:e,a,a  sessizler :m,r,b
# a,e,ı,i,o,ö,u,ü
#kaç tane a vardr gibi bir şey de olucak,
# {
#     sesliler:....,
#     sessizler:...,
#     seslilerin_sayisi:x
#     sessizlerin_sayisi:y
# }

# def sesli_sessiz_ayir(metin:str):
#     sesli_harfler=["a","e","ı","i","o","ö","u","ü"]
#     metindeki_sesli_harfler=set()   #set içinde tekrar yapmadığı için list yerine set kullanılır.
#     metindeki_sessiz_harfler=set()
#     sesli_sayisi=0
#     sessiz_sayisi=0
#     for harf in metin:      #metnin içideki harflerin içinde dolaşıyoruz.
#         if harf.isalpha():   #içinde boşluk ve sembol olduğu için isalpha kullanılır.
#             if sesli_harfler.count(harf) >0:
#                 metindeki_sesli_harfler.add(harf)  #set için append değil add ile ekliyoruz.
#                 sesli_sayisi +=1
#             else:
#                 metindeki_sessiz_harfler.add(harf)
#                 sessiz_sayisi +=1
#     return {
#        "sesliler":metindeki_sesli_harfler,
#        "sessizler": metindeki_sessiz_harfler,
#        "seslilerin_sayisi":sesli_sayisi,
#        "sessizlerin_sayisi":sessiz_sayisi
#     }
#
# yazi="merhaba dünya!"
# print(sesli_sessiz_ayir(yazi))  # çıktı: {'sesliler': {'a', 'ü', 'e'}, 'sessizler': {'h', 'm', 'd', 'n', 'r', 'b', 'y'}, 'seslilerin_sayisi': 5, 'sessizlerin_sayisi': 7}
# sesli_sessiz_ayir("merhaba dünya")
# girilen=input("bir metin giriniz:")
# sesli_sessiz_ayir(girilen) # bu şekilde sona ekleyerek fonksiyon çağırabiliriz ya da dışardan input alabiliriz.

#başka bir versiyonu:
# def metin_incele(metin:str)->dict:
#     sesliler_listesi=["a","e","ı","i","o","ö","u","ü
#bla bla bunu sonra dene !


# ÖRNEK:
#parametre olarak '1980-10-12' gibi bir doğum tarihi olarak yaş hesaplayan ve bu değeri geri dönen bir metot yazınız:
#hataya düşmemek için: #def yas_hesapla(yil:int,ay:int,gun:int)-->int:
# def dogum_tarihi_hesapla(dogum_tarihi:str)->int:
#  from datetime import datetime as dt
#  dogum_tarihi_date=dt.strptime(dogum_tarihi,"%Y-%m-%d")
#  simdiki_zaman = dt.now()
#  fark=simdiki_zaman - dogum_tarihi_date
#  return round(fark.days/365)

#print(dogum_tarihi_hesapla("1980-10-12")) #42
#print(dogum_tarihi_hesapla("1997-04-11")) #26 :(

#emeklilik yaş hesabı:
#emekliliğe kaç yıl kaldığını hesaplamaya kaç yıl kaldığını hesaplayan bir metot yazınız:
#kadın :58 erkek:65
#"sevgili Nur,2022 tarihi itibariyle emekliliğine 40 yıl kalmıştır."

#hocanın çözümü=
# def emeklilik_yasi_hesapla(ad: str, cinsiyet: str, dogum_tarihi: str) -> str:
#     from datetime import datetime as dt
#     emeklilik_yasi = 65
#     if cinsiyet == "k":
#         emeklilik_yasi = 58
#     kisinin_yasi = yas_hesapla(dogum_tarihi)
#     emeklilige_kalan_yil = emeklilik_yasi - kisinin_yasi
#     sonuc = f"Sevgili {ad.capitalize()}, {dt.date.today().year} tarihi itibariyle emekliliğine {emeklilige_kalan_yil} yıl kaldı."
#     return sonuc
#print(emeklilik_yasi_hesapla("gonca", "k", '1997-04-11'))
# ad = input("adınızı giriniz: ")
# cinsiyet = input("cinsiyetiniz (k/e): ")
# dogum_tarihi = input("doğum tarihiniz (yıl-ay-gün): ")
# print(emeklilik_yasi_hesapla(ad, cinsiyet, dogum_tarihi))
#dışarıdan böylede bilgi girilebilir.
# personeller = [
#     {
#         "ad":"nur",
#         "cinsiyet":"k",
#         "dt":'1980-10-12'
#     },
#     {
#         "ad": "ahmet",
#         "cinsiyet": "e",
#         "dt": '1990-10-12'
#     }
# ]
# for personel in personeller:
#     print(emeklilik_yasi_hesapla(personel["ad"], personel["cinsiyet"], personel["dt"]))

'''
def func(param1:datatype,param2:datatype=value):
   pass
func(10,20) ->param2=20
func(10)-> param2=value
'''
#parametre olarak yarıçap alan ve dairenin alanını hesaplayıp dönen metor yazınız.(eğer pi sayısı girilmezse math içindeki kullanılsın)


def dairenin_alanini_hesapla(yaricap:float,pi_sayisi:float=None):
    import math as m
    if pi_sayisi is None:
        pi_sayisi = m.pi
    alan=pi_sayisi*m.pow(yaricap,2)
    return alan
print(dairenin_alanini_hesapla(10))    #314.1592653589793
print(dairenin_alanini_hesapla(10,3))  #300.0

#alternatif:
import math as m
def dairenin_alanini_hesapla1(yaricap:float,pi_sayisi:float=m.pi):
    alan=pi_sayisi*m.pow(yaricap,2)
    return alan
print(dairenin_alanini_hesapla1(10,2)) #200.0
print(dairenin_alanini_hesapla1(10,3))  #300.0

#NOTE:opsiyonel parametreler metodun sonunda yer alır.
#bu parametrenin sonuna required alan bir parametre konulamaz.
#opsiyonel metot tanımlaması: overlood varmış gibi davranır,normalde pythonda overlood yok çünkü.
# def topla(sayi1,sayi2=10,sayi3=20):
#     toplam=sayi1+sayi2+sayi3
#     print(toplam)
# topla(4)
# topla(4,5)
# topla(4,5,6) #sayi1 belli zaten ,sayi2:5 sayi3 :6
# topla(4,sayi3=5,sayi2=6) #metot içinde tanımlanan ismiyle kullanılır.

#'*paramname' şeklinde parametre alan bir metot tanımlayalım.*args:içine birden çok parametre alır.
# PARAMETRE SAYISINI BİLMİYORSAK BUNU KULLANIRIZ:
def topla(*sayilar): #def topla(*args)
    toplam=0
    for i in sayilar:
        toplam += i
    print(toplam)
topla(1)    #1
topla(1,2,3,4,5,6,7)   #28
topla(1,2)             #3

# '**kwargs' isimlendirilir.
def func(**kwargs): #veritipi dict[str,Any] 'dir. value kısmı any old için istenilen yazılabilir.sınır yok giriş için.key,value şeklinde değer tanımlıycaz.
    for key,value in kwargs.items():
        print(key,value)
func(ad="gonca",soyad="çomak",mezuniyet=True)

#nested functions: method içinde metot tanımlası yapabilir.
#parametre alıp alması önemli değil.
def func1():
    a=10
    def func2():
        b=20
        return a+b
    func2()       #bu fonksiyonu çağıramayız.çünnkü artık o global değil.

func1()

#recursive funcs:kullanımı zordur,debug yapmasıda .en ünlüsü faktöriyel hesabıdır.
def func1():
    #kodlar
    func1()

#faktöriyel hesabı:
def factorial(x):
    if x==1:
        return 1    #1 olmasıda aslında durdurma işlemidir.Menü içinde menü yapılması gibi şeylerde kullanılabilir.
    else:
        return (x*factorial(x-1))
num=3
print(factorial(3))
print(factorial(4))



























































