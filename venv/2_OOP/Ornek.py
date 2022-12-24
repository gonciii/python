# Örnekler:
# 1-) diyetisyen örneği:
#**** property oluştururken get metodu tanımlamak zorunludur ancak set metodu opsiyoneldir.
'''
# • Beden kitle/kütle indeksi < 18,5 ise Zayıf
# •    18,5 < Beden kitle/kütle indeksi < 24,9 ise Normal
# •    25 < Beden kitle/kütle indeksi < 29,9 ise Fazla kilolu
# •    30 < Beden kitle/kütle indeksi < 34,9 ise I. derece obez
# •    35 < Beden kitle/kütle indeksi < 39,9 ise II. derece obez
# •    Beden kitle/kütle indeksi > 40 ise III. derece obez
endeks=(kilo/(boy **2),2)
'''
import datetime as dt
import enum as e

class Cinsiyet(e.Enum):
    kadin=1
    erkek=2

class Kisi:
    def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad

class Uye(Kisi):
    def __init__(self,ad:str,soyad:str,dogum_tarihi:dt.datetime,cinsiyet:Cinsiyet):
        super().__init__(ad,soyad)
        self.dogum_tarihi=dogum_tarihi
        self.cinsiyet=cinsiyet

    @property
    def boy(self):
        return    self.__boy / 100

    @boy.setter
    def boy(self,val):
        if not (80 < val <230):
            raise Exception("80-230 cm arasında değer girilebilir.")
            self.__boy=val

    @property
    def kilo(self):
        return self.__kilo
    @kilo.setter
    def kilo(self,val):
        if not(20<val<300):
            raise Exception("20-300 kg arasında bir değer girebilirsiniz.")
        self.__kilo=val
    @property
    def yas(self):
        self.__yas=round((dt.datetime.now()-self.dogum_tarihi).days/ 365)
        return self.__yas
    def kisi_bilgilerini_goster(self):
        return self.__dict__

    def bki_hesapla(self,kilo):
        if not(20< kilo <300):
            raise Exception("20-300 kg arasında değer girilebilir.")
        self.__bki=kilo / (self.boy**2)
        return self.__bki

    def ideal_kilo_hesaplama(self):
        alt_sinir=18.5*(self.boy**2)
        ust_sinir=24.9*(self.boy**2)
        print(f"Normal sınırlar içinde olmak için {alt_sinir} ile{ust_sinir} arasında olmalısınız.{self.__kilo-ust_sinir} kg fazlanız vardır.")



uye1=Uye("gonca","çomak",dt.datetime(1997,4,11),Cinsiyet.kadin)
uye1.ad="ali"
uye1.soyad="beyaz"
uye1.boy=164
uye1.kilo=66
#uye1.yas=10 böyle olmaz ! yaş property'sinin settter metodu olmadığından bunu yaparsak hata alırızz.
print(uye1.yas)   #26
print(uye1.kisi_bilgilerini_goster())  #{'ad': 'gonca', 'soyad': 'çomak', 'dogum_tarihi': datetime.datetime(1997, 4, 11, 0, 0), 'cinsiyet': <Cinsiyet.kadin: 1>, '_Uye__kilo': 66, '_Uye__yas': 26}
# print(uye1.bki_hesapla(100))
# print(uye1.bki_hesapla(66))
uye1.ideal_kilo_hesaplama()




# hocanın yazdığı :
#
# ** Property oluştururken get metodunu tanımlamak zorunludur ancak set metodu opsiyoneldir.
import datetime as dt
import enum as e


class Cinsiyet(e.Enum):
    kadin = 1
    erkek = 2


class Kisi:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad

    def kisi_bilgileri_goster(self):
        return f"{self.ad} {self.soyad}"


class Uye(Kisi):
    def __init__(self, ad: str, soyad: str, dogum_tarihi: dt.datetime, cinsiyet: Cinsiyet):
        super().__init__(ad, soyad)
        self.dogum_tarihi = dogum_tarihi
        self.cinsiyet = cinsiyet
        self.__bki = 0

    @property
    def boy(self):
        return self.__boy / 100  # istersek metre cinsinden dönebiliriz

    @boy.setter
    def boy(self, val):  # cm cinsinden alıp
        if not (80 < val < 230):
            raise Exception("80-230 cm arasında değer girilebilir.")
        self.__boy = val

    @property
    def kilo(self):
        return self.__kilo

    @kilo.setter
    def kilo(self, val):
        if not (20 < val < 300):
            raise Exception("20-300 kg arasında değer girilebilir.")
        self.__kilo = val

    @property
    def yas(self):
        self.__yas = round((dt.datetime.now() - self.dogum_tarihi).days / 365)
        return self.__yas

    def kisi_bilgileri_goster(self):
        return self.__dict__

    def bki_hesapla(self, kilo):  # kilo / boy(m) **2
        if not (20 < kilo < 300):
            raise Exception("20-300 kg arasında değer girilebilir.")
        bki = kilo / (self.boy ** 2)
        return bki

    def ideal_kilo_hesapla(self):
        alt_sinir = round(18.5 * ((self.__boy / 100) ** 2))  # __boy'daki değeri metreye çevirip işlem yaptık
        ust_sinir = round(24.9 * (self.boy ** 2))  # property'den boy'un metre halini istedik
        print(
            f"Normal sınırlar içinde olmak için {alt_sinir} ile {ust_sinir} arasında olmalısınız. {round(self.__kilo - ust_sinir)} kg fazlanız var.")

    @property
    def bki(self):
        self.__bki = self.__kilo / (self.boy ** 2)
        return self.__bki

    def durum_goster(self):
        durum = ""
        if 0 < self.bki < 18.5:
            durum = "zayıf"
        elif 18.5 <= self.bki < 24.9:
            durum = "normal"
        elif 25 <= self.bki < 29.9:
            durum = "fazla kilolu"
        elif 30 <= self.bki < 34.9:
            durum = "I.derece obez"
        elif 35 <= self.bki < 39.9:
            durum = "II.derece obez"
        elif self.bki >= 40:
            durum = "III.derece obez"
        else:
            durum = "hesaplanamadı"
        return durum


uye1 = Uye("ahmet", "yılmaz", dt.datetime(1982, 1, 3), Cinsiyet.erkek)
uye1.ad = "ali"
uye1.boy = 180
uye1.kilo = 100
# uye1.yas = 10  # yas property'sinin setter metodu olmadığından bunu yaparsak  AttributeError: can't set attribute 'yas' hatasını alırız.
# print(uye1.yas)
# print(uye1.kisi_bilgileri_goster())
print(uye1.bki_hesapla(uye1.kilo))
print(uye1.bki_hesapla(75))
# uye1.ideal_kilo_hesapla()
print(uye1.durum_goster())












