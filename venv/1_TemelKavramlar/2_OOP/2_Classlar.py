#Python Class
#Nesne üretmek için tanımlanan şablonlardır.
#İiçinde özellikler(attributes) ve davranışlar(behavior) tanımlanır.
'''
Gösterim şekli ve kullanımı:
class ClassAdi:
     sınıfın özellikleri
     sınıfın davranışları vb.

*sınıf adı tanımlarken PascalCase notasyonu kullanılmalıdır.
*Tekil olarak tanımlanır.
camelCase
snake_case-->değişken ve metot tanımlanılması.
kebap-case--daha çok css de kullanılır.
PascalCase--->class adı için kullanılır.
typeHungarianCase:neyi tanımlıyorsak değişkenin baş harfi gibi bir şey yazıyoruz,tip olarak.

'''
import datetime


# class Araba:
#     pass

#Nesne üretme (instance)
#nesne nasıl üretilir? instance yani kopya nasıl yapılır?
# a1=Araba() #araba şablonu içinde a1 de olucak şekilde yapmış oluyoruz.
# a2=Araba()
#a3=a1--->bu yapılmaz.Bu şekilde dolaylı yoldan nesne üretilemez.

# class Araba():
#     marka=""
#     model:str=""
#
# araba1=Araba() #araba1 ram üzerinde yer kaplayan bir nesne almış olur.
# #sınıf içinde olan değişkenlere field denir.
# araba1.marka="seat"
# araba1.model="leon"
#
# araba2=Araba()
# araba2.marka="audi"
# araba2.model="Q2"
# print(f"{araba1.marka}-{araba1.model}")
# print(f"{araba2.marka}-{araba2.model}")
#
# print(araba1) #<__main__.Araba object at 0x0000027277FEBEE0>
# print(araba2) #<__main__.Araba object at 0x0000027277FEBE80>
#
# araba3=araba1
# print(araba3) #direk bunda referans olucak araba1 in referansını alır.
#
# #__str__:metodu nesneyi yazdırmak istediğinizde çalışan metottur.default olarak.
# # <__main__.Araba object at 0x000001C41B3EEDA0 > böyle bir değer döner.ancak kendiniz bunu override(ezmek) edebilirsiniz.
#
# class Araba:
#     marka=""
#     model=""
#     def __str__(self): #override --str ile kısıtlanılmış olur,yukarıdaki gibi yazdırılabilir.
#         return f"{self.marka}--{self.model}"
#
# a1=Araba()
# a1.marka="audi"
# a1.model="Q2"
# print(a1)     #audi--Q2

#Bir öğrenci sınıfı oluşturarak attr.
# olarak ad,soyad,numarası,doğum tarihi:str şeklinde tanımlayınız.ve 2 nesne üreterek içini doldurunuz.
#__str__'yi override ederek ad soyad /numarası şekinde gösteriniz
#örnek:
#ilk sınıf oluşturuldu:
# class Ogrenci:
#     ad:str=""
#     soyad:str=""
#     numarasi:int=""
#     dogumTarihi:str=""
#     def __str__(self):   #formatiprint
#         return f"{self.ad} {self.soyad}/{self.numarasi}{self.dogumTarihi}"
#     def __repr__(self):
#         f"{self.ad} {self.soyad}/{self.numarasi}
#
# ogrenci1=Ogrenci()
# ogrenci1.ad="gonca"
# ogrenci1.soyad="çomak"
# ogrenci1.numarasi=404
# ogrenci1.dogumTarihi=""
# # print(ogrenci1)
# # print(ogrenci1.ad)
#
# ogrenci2=Ogrenci()
# ogrenci2.ad="ozan"
# ogrenci2.soyad="içcan"
# ogrenci2.numarasi=13
# ogrenci2.dogumTarihi=""
#
# ogrenciler=[]
# ogrenciler.append(ogrenci1)
# ogrenciler.append(ogrenci2)
# #print(ogrenciler)
#__repr__ metodu override ettiğimizde [gonca çomak/404,,,,,]
#list[] vb içinde class instance kullanıldığında bu metotu override ederek kullanabiliriz.
#
# for ogrenci in ogrenciler:
#     print(ogrenci)
# print(ogrenci1.__dict__) #nesnenin içindekileri dictionary olarak verir.
# #{'ad': 'gonca', 'soyad': 'çomak', 'numarasi': 404, 'dogumTarihi': ''}

#Constructor/ yapıcı metot:
#sınıfın create edilmesinden sorumludur.İlk çalışan metotdur.
#tüm sınıflarda tanımlıdır.İsterseniz override edip farklı şekillerde kullanabilirsiniz.
#nesne üretirken SinifAi() kullanılan yapıda () constructor'ı çağırmaktadır.

#__init__ pythondaki constructor'ı tanımlamak için kullanılır.
#class Araba:
    #pass
#a2=Araba()

class Araba:   #araba diye bir sınıf tanımlanıyor.
    def __init__(self,marka:str="",model=""):    #init'i kullanmak aslında boş create etmek gibi bir şey anlamına gelir.
        self.brand=marka
        self.model=model
    def bilgileri_getir(self):      #parametresiz metot.              #otomatik self tanımlanıyor.self:sınıfın kendisini temsil eder.
        print(f"{self.brand}-{self.model}")

a1=Araba("audi","Q2")
#print(a1.model)

a3=Araba() #şeklinde tanımlama yapmak istersek
# constructor'daki parametreleri nullable yapmamız yeterlidir.
a3.brand="seat"
a3.model="leon"
#print(a3.brand)

#self:sınıfın kendisini temsil eder.
# function: def global kapsamda tanımlananlar.
# metot: def sınıf içinde tanımlanan fonskiyonalara metot denir.
#sınıf instance'ı olmadığı sürece metotlara erişemiyoruz.

a3.bilgileri_getir()  #seat-leon
a1.bilgileri_getir()  #audi-Q2

#örnek:
#çalışan sınıfı oluşturunuz,init'de ad,soyad,işe giriş tarihi(datetime)alınız.
#sonra calisma_süresini_hesapla metotdu oluşturarak kaç yıldır çalıştığını dönen bir metot yazınız.

#benim yaptığım :
#işegiriştarihi=igt
# class Calisan1:    #çalışanlar sınıfı oluşturuldu.
#     def __init__(self,ad:str="",soyad:str="",igt:datetime=""):
#         self.ad=ad
#         self.soyad=soyad
#         self.igt=igt
#     def calisma_suresi_hesaplama(self,guncel_tarih:datetime="",igt:datetime=""):
#         import date as dt
#         igt=input("Lütfen hangi yılında işe girdiğinizi giriniz:")
#         guncel_tarih=datetime.date.today()
#         calisma_yili=guncel_tarih-igt
#         return



import datetime
class Calisan:
    def __init__(self,ad:str="",soyad:str="",ise_giris_tarihi:datetime=datetime.datetime.now()):
        self.name=ad
        self.surname=soyad
        self.hiring_date=ise_giris_tarihi
    def calisma_suresi_hesapla(self):
        simdiki_zaman=datetime.datetime.now()
        fark=simdiki_zaman-self.hiring_date
        yil=fark.days/365
        return yil

# c1=Calisan("ali","yılmaz",datetime.datetime(2000,10,12))
# print(c1.calisma_suresi_hesapla()) #22.13972602739726
#
# c2=Calisan()
# c2.hiring_date=datetime.datetime(2005,1,1)
# print(c2.calisma_suresi_hesapla())   #17.915068493150685

c3=Calisan()
c3.name=input("çalışan adı giriniz:")
c3.surname=input("çalışan soyadı giriniz:")
c3.hiring_date=datetime.datetime.strptime(input("işe giriş tarihini giriniz(g/a/y):"),"%d/%M/%Y")
print(c3.calisma_suresi_hesapla())
