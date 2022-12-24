#Inheritance (kalıtım)
'''
#kalıtım,sınıflar arasında hiyerarşik bir ilişki kurmamızı sağlar ve kod tekrarlarını önler.
#birden fazla sınıftan kalıtım alınabilir.
#oop genellikle diğer programlam dilleri ile aynıdır tek bir farkı vardır.

# base class: kalıtım veren sınıf
# derived class:kalıtım alan sınıf

class BaseClass1:
    pass
class BaseClass2:
    pass

class DerivedClass(BaseClass1,BaseClass2):
    pass

class DerivedClass2(DerivedClass):
    pass

'''
class Kamera:
    def __init__(self):
        self.cozunurluk=""
    def fotograf_cek(self):
        print("fotoğraf çekildi!")
class Radyo:
    def radyo_cal(self):
        #radyo çalacak işlemleri tanımla
        print("radyo çalınıyor!")

class Telefon(Kamera,Radyo):             #telefonu kameradan miras alıyorum
    def arama_yap(self):
        print("arama yapılıyor !")
    #override:base sınıf içinde tanımlanmış olan metot ,derived sınıf içinde
    #farklı bir şekilde kullanılmak istenirse base'deki ismiyle ezilerek yeni versiyonu yazılabilir.
    def radyo_cal(self):
        print("telefonda radyo çalınıyor...")
t1=Telefon() #telefon classında kamera ve radyo valularını miras olarak aldığımızda kopyala yapıştır yapmak yerine daha kısa yaptık.
print(t1.cozunurluk)
t1.fotograf_cek()
t1.arama_yap()
t1.radyo_cal() #telefonda radyo çalınıyor...

#Örnekler:

class SamsungTelefon(Telefon):   #telefon sınıfından miras alıyor.
    pass
class AppleTelefon(Telefon):
    pass
iphone14=AppleTelefon

#Örnekler:

# İnsan:ad,soyad,doğum yılı
# Ogrenci : ad,soyad,doğum yılı,okul adı,öğrenci no
# Ogretmen: ad,soyad,doğum yılı ,okul adı ,branşı vb.

class Kisi:
    def __init__(self,ad="",soyad="",dogum_yili=""):
        self.ad=ad
        self.soyad=soyad
        self.dogum_yili=dogum_yili
    def kisi_bilgileri_getir(self):
        print(f"{self.ad}{self.soyad}")

class Ogrenci(Kisi):
    def __init__(self,ad="",soyad="",dogum_yili="",okul_adi="",ogrenci_no=0):
        super().__init__(ad,soyad,dogum_yili)
        self.okul_adi=okul_adi
        self.ogrenci_no=ogrenci_no

#super(): base sınıfı temsil eder.(diğer programlama dillerinde this)
# o1=Ogrenci("nur","öztürk","1980","Gazi",200)
# print(o1.__dict__)
# o2=Ogrenci()
# o2.ad="gonca"  #kişi den geliyor.
# o2.soyad="çomak"
# o2.dogum_yili=1997
# o2.okul_adi="abant izzet baysal"  #ogenciden geliyor.
# o2.ogrenci_no=160204041
# print(o2.__dict__)

# Base sınıf içinde tanımlanan metodun içinin derived sınıfta doldurulmak zorunda olması
# için abstract method olarak işaretlenemesi gerekir.
# decarator örnekleri : @property ve ya @abstract
from abc import ABC ,abstractmethod
class GeometrikSekil(ABC): #sınıfı abstract yapmış oluruz.
    @abstractmethod
    def alan(self):
        pass

class Kare(GeometrikSekil):
    def __init__(self,kenar_uzunlugu):
        self.kenar_uzunlugu=kenar_uzunlugu

    def alan(self):
        return self.kenar_uzunlugu**2
k1=Kare(10)
print(k1.__dict__)
print(k1.alan())

# gs1=GeometrikSekil()
# print(gs1.__dict__)  ----->bu problem çıkardı.

#daire sınıfı oluşturup geometrik şekil sınıfından kalıtım alarak sınıfın içini doldurunuz.
class Daire(GeometrikSekil):
    def __init__(self,yaricap):
        self.yaricap=yaricap
        self.pi=3
    def alan(self):
        return self.pi*(self.yaricap**2)
d1=Daire(2)
print(d1.alan()) #12
