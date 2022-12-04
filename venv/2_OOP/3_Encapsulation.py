#Encapsulation (kapsülleme)
# Sınıf içinde kullanılacak,kullanıcının bilmesine gerek olmayan verileri
# gizlemek istediğimizde veya kontrollü şekilde veri set etmemiz gerektiğinde kullandığımız temel OOP kavramıdır.
# gizlemek istediğimiz değişkenlerin başına __ eklenerek private yapılır.
# kontrollü bir şekilde veri set etmek için de get/set metotları veya property
# tanımlanır.
import math
class Daire:
    __pi_sayisi=math.pi         #kimsenin değerini değiştirmesini istemedğimiz için dışarıya kapattık.__
    '''Bu değişkenin değerini sınıf içinde herhangi bir yerde kullanabiliriz ancak instance'lar bunu göremez.'''
    def __init__(self,yaricap):
        self.yaricap=yaricap
    def alan_hesapla(self):
        return self.__pi_sayisi*math.pow(self.yaricap,2)
    #pi sayısı için getter or get:pi sayısını açıyor.
    def get_pi(self):
        return self.__pi_sayisi
    #pi sayısını setter metotu ilede değiştiriyoruz, hata mesajı veriyoruz.
    def set_pi(self,value):
        if not  (value==3 or value==3.14):
            raise Exception("Pi sayısı 3 veya 3.14 değerini alabilir.")
        self.__pi_sayisi=value


d1=Daire(2)
d1.set_pi(3)
print(d1.alan_hesapla()) #---->#12.566370614359172---->sonradan 12 olucak.

#print(d1.__pi_sayisi) #------->#eğer __pi_sayisi şeklinde dışarıdan kullanıma kapatıldıysa
#önerilerde görünmez,yine de zorla kullanılmaya çalışılırsa hata  verir.
#AttribureErorr:"Daire" object has no attribute "__pi;_sayisi"
#get metotudundan sonra geçerli olan:
print(d1.get_pi()) #3.141592653589793 --->sonradan 3 olucak.
d2=Daire(3)
print(d2.alan_hesapla()) #28.274333882308138
#print(d2.pi_sayisi)      #3.141592653589793
print(d2.get_pi())       #3.141592653589793
#ilk private yapıldı---> __pi_sayisi sonra,get edildi,
#get:talep ederse isterse ayrı metot yazılır.
#sonra set edildi.içerideki değeri kontrollü değiştirmek istediğimizde dışarıdaki kullanıcı değişkenin değerini değiştirmek istediğin de set ya da setter kullanıcaz.



#---> PROPERTY:
#get ve set metotlarını tanımlarken @property decarator kullanarak daha kısa tanımlayabiliriz.
class Ogrenci:
    def __init(self):
        self.__numara=1

    @property
    def numara(self):        #getter
        return self.__numara
    @numara.setter
    def numara(self,val):        #setter
        if not 100<= val <=300:
            raise Exception ("Numara değeri 100-300 aralığında olabilir.")
        self.__numara=val

#sadece get metodu olan bir property tanımlanabilir.
o1=Ogrenci()
#print(o1.numara)
#o1.numara=10
o1.numara=200   #o1.set_numara(200) gibi kullanmak yerinde daha kısa ve okunur yaptık:
                #o1.get_numara()
print(o1.numara)
