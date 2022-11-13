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
#
# # 2-) GERİ DEĞER DÖNEN METOTLAR
# # 2.a-) PARAMETRESİZ
# # return:geriye değer döndürüyor.
# def topla1()-> float:
#     '''sabit olarak 4 ve 5 değerini toplayarak sonucu döner.'''
#     toplam=4+5
#     return float(toplam)  #float sayesinde 9.0 döndürürüz.
#
# t=topla1()
# print(t)    #9
# print(topla1())   #9
# #print(topla())    #None:değer dönmüyormuş demektir.ancak çağırım yapabilir.
#
# # bir metottan bir değer döner.
# # return toplam,fark,üs gibi birden fazla değer döndüremez.
# # Dict kullanarak yapabiliriz.
#
#
#
# # 2.b-) PARAMETRELİ
#
# def summary1(a:int,b:int) -> float:
#     toplam=a+b
#     return float(toplam)
#     print("bitti")
# # returnden sonra kodlar çalışmaz.
# # Tek bir değeri vardır.değer döndürmek !!
# t2=summary1(10,20)
# print(t2)     #30.0
# print(t2**2)  #900.0

#NOT : sistemde hazır olamayan kodları daha modüler kullanabilmek için aslında custom metotları kullanıyoruz.!!

# Örnek:
# s1:2 float parametre alarak bu sayıların farkını alan ve ekranda
# gösteren bir metot tanımlayınız.(geri değer dönmeyen)
# def fark_al(sayi1:float,sayi2:float):
#     fark=sayi1-sayi2
#     print(fark)

# fark_al(10,20.4) #-10.399999999999999---->>  #burda metotu çağırıyoruz,tekrar print dememize gerek yok.
# fark_al(50,21)  #29
# ---------------------------------------------
# s1=float(input("Birinci sayıyı giriniz:"))
# s2=float(input("İkinci sayıyı giriniz:"))
# fark_al(s1,s2)
# ----------------------------------------------
# Programlama dillerinde uyulması gereken 5 tane prensib.
# Not: SOLID: S,O,L,I,D hepsi farklı bir kuraldır.
# S:single responsibility:tek sorumluluk prensibi,yazılan bir kodun(class,method vb)tek bir amaca hizmet etmesi.
# def dort_islem_yap(a,b):
#     toplam=a+b
#     fark=a-b
#     bolum=a/b
#     carpim=a*b
#     sonuc={
#         "toplam":toplam,
#         "fark":fark,
#         "carpim":carpim,
#         "bolum":bolum
#
#     }
#     return sonuc
# print(dort_islem_yap(10,20))

# olması gereken :
def topla(sayi1:float,sayi2:float):
    toplam=sayi1 + sayi2
    return toplam
def cikar(sayi1:float,sayi2:float):
    fark=sayi1-sayi2
    return fark
def carp(sayi1:float,sayi2:float):
    carpim=sayi1*sayi2
    return carpim
def bol(sayi1:float,sayi2:float):
    try:
        bolum = sayi1 / sayi2
        return bolum
    except:
        raise Exception("sayi2 0 olamaz !")

# diğer bir yazım şekli:
def dort_islem(a:float,b:float):
    toplam=topla(a,b)
    fark=cikar(a,b)
    carpim=carp(a,b)
    bolum=bol(a,b)
    sonuc={
     "toplam": toplam,
     "fark":fark,
     "carpim":carpim,
     "bolum":bolum
    }
    return sonuc
# burda 10,0 gibi bir şey yaparsak.0'a bölme hatası verir.
s=dort_islem(10,20)
print(s)
print(s["fark"])
print(s["bolum"])
print(bol(10,20))

# ÖRNEK:
# 1-) 1'den dışarıdan parametre olarak alınan bir sayıya kadar olan çift sayıları ekrana gösteren bir metot yazınız.
# 2-)update:Listeye atan ve o listeyi dönen metot yazınız.

# 1-) çözümü:
# parametre alan ve geri değer döndürmüyor
def ciftleri_yazdir(bitis:int):
    for i in range(1,bitis+1):
        if i%2==0:
            print(i)
ciftleri_yazdir(10)

# listeye atan ve o listeyi dönen metot:
def ciftlerin_listesini_getir(bitis:int)->list:
    liste=[]    #ramde listenin ölmesi için bu kısma gelmesi lazım.
    for i in range(1,bitis+1):
        if i%2==0:
            liste.append(i)
    return liste

ciftler=ciftlerin_listesini_getir(10)
print(ciftler)

# ÖRNEK:
# parametre olarak ad,soyad,uzanti alarak ad.soyad@uzanti şeklinde
# mail oluşturan ve dönen bir metot tanımlayınız.
# (türkçe karakterleri dönüştürünüz tümü küçük harf olmalı)
# ÇÖZÜM:
def turkce_karakterli_cevir(metin:str):
    metin=metin.replace("ö","o").replace("ü","u").replace("ç","c").replace("ğ","g").replace("ş","s").replace("ı","i")
    return metin
def mail_olustur(ad:str,soyad:str,uzanti:str):
    #ad=turkce_karakterleri_cevir(ad)
    #soyad=turkce_karakterleri_cevir(soyad)
    mail=turkce_karakterli_cevir(f"{ad}.{soyad}@{uzanti}".lower().replace(' ',""))
    return mail
#print(mail_olustur("gonca gül","çomak","bilgeadam.com"))

# Türkçe karakterleri eng.karaktere çeviren bir metot tanımlayabilirsiniz ve mail oluşturucunun içinde kullanabilrsiniz.

personel_listesi=[
    {
        "ad":"nur",
        "soyad":"öztürk"
    },
    {
        "ad":"damla",
        "soyad":"kahraman"

    },
    {
        "ad":"mert",
        "soyad":"boylu"
     },
    {
        "ad":"neslihan",
        "soyad":"kaptan yorübulut"
    }

]
# bilgeadam.com -> yukarıdaki listede yer alan tüm personellere mail oluşturucu metot yardımı ile
# mailler oluşturunuz ve listeye ekleyiniz.

mail_listesi=[]
for personel in personel_listesi:
    pa=personel["ad"]  #personel.get("ad")
    ps=personel["soyad"]
    mail=mail_olustur(pa,ps,"bilgeadam.com")
    mail_listesi.append(mail)

print(mail_listesi)

# update:dışarıdan parametre olarak bir dict. listesi alan ve tüm listedeki
# çalışanlar için mail oluşturupu liste olarak dönen method yazınız.
# sürekli liste geldiğini düşünerek methoda çevirmek.
def mail_olustur1(personel_listesi:list):
    mailler=[]
    for personel in personel_listesi:
        mailler.append(mail_olustur(personel["ad"],personel["soyad"],"bilgeadam.com"))
        return mailler

print(mail_olustur1(personel_listesi))
print(mail_olustur("gonca","çomak","bilgeadam.com"))

# ['nur.ozturk@bilgeadam.com', 'damla.kahraman@bilgeadam.com', 'mert.boylu@bilgeadam.com', 'neslihan.kaptanyorubulut@bilgeadam.com']
# bu formatta gelen mail listesinin ad ve soyadı ayrıştırıp personel listesi şeklinde dönen bir metot yazınız.
# p_list=[{"ad":"nur","soyad":"öztürk"}]
# split kullanıcaz.

def mail_listesi_donusturme(liste:list):
    liste=[]





































