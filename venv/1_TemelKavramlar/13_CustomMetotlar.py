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
def selamla():
           print("Merhaba Dünya!")
selamla()    #Merhaba Dünya!

# 1.b-) PARAMETRELİ
# --------------Örnek:
def selamla1(mesaj:str):
    #mesaj değişkenini metot içinde istediğimiz gibi kullanabiliriz.
    print(mesaj)

selamla()  #statik olarak : #Merhaba Dünya!
selamla1("Hello World!")    #Hello World!
selamla1("Naber?")          #Naber?
# Örnek:Toplama işlemi metodu yazalım.
def topla():
    print(4+5)
def summary(a:int,b:int):
    try:
        a=int(a)
        b=int(b)
        toplam=a+b
        print(toplam)
    except:
        print("çevrilmeyen bir değer gönderildi")
topla()
summary("1a0","20")         #çevrilemeyen bir  değer göndrildi.
summary(10,20)             #30
#summary("10",20)          #error verir.



# 2-) GERİ DEĞER DÖNEN METOTLAR
# 2.a-) PARAMETRESİZ
# return:geriye değer döndürüyor.
def topla1()-> float:
    '''sabit olarak 4 ve 5 değerini toplayarak sonucu döner.'''
    toplam=4+5
    return float(toplam)  #float sayesinde 9.0 döndürürüz.

t=topla1()
print(t)    #9
print(topla1())   #9
#print(topla())    #None:değer dönmüyormuş demektir.ancak çağırım yapabilir.

# bir metottan bir değer döner.
# return toplam,fark,üs gibi birden fazla değer döndüremez.
# Dict kullanarak yapabiliriz.



# 2.b-) PARAMETRELİ

def summary1(a:int,b:int) -> float:
    toplam=a+b
    return float(toplam)
    print("bitti")
# returnden sonra kodalr çalışmaz.
# Tek bir değeri vardır.değer döndürmek !!
t2=summary1(10,20)
print(t2)     #30.0
print(t2**2)  #900.0

