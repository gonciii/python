#Polymorphism (çok biçimlilik)
'''
Base sınıflarda tanımlanan metotların alt sınıflarda adı aynı kalmak üzere farklı bir
şekilde çalışmasını sağlayan OOP temel kavramlarından biridir.
Daha önceki örneklerde (4_Inheritance) kalıtım yoluyla bu kavramı uygulamıştık.
aşağıdaki örnekte ise function yöntemiyle polym.
uygulamasını görelim.

'''
#ABC:ABSTRACT BASE CLASS
class Silah(ABC):
    @abstractmethod    #bütün silahların ateşleme özelliği var ve soyut bir sınıfmış gibi düşünebiliriz.
    def ates_et(self):
        pass
class RoketAtarSilah(Silah):
    def ates_et(self):
        #roket atılma işlemleri
    print("roket atıldı...")

class OkAtarSilah(Silah):
    def ates_et(self):
        #ok atma işlemleri
    print("ok atıldı....")
rpg7=RoketAtarSilah()
#rpg7.ates_et()

cross_bow=OkAtarSilah()
#cross_bow.ates_et()

def atesle(silah:Silah):          #polymorphism'den yararlanma.oyun içinde nesneyi üretirken silahın tipinden bağımsız olarak silah almıştır ve ateşle
                                  # metodu ile daha genel bir kod yazarak yapı oluşmuş olur.
    silah.ates_et()

atesle(rpg7)            #metod içinede istenilen silah yazılabilirek kopya üretir.
atesle(cross_bow)


# python da birden fazla kalıtım alıyor .
# java,c# bir tane kalıtım alabilir.




