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
    @abstractmethod
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

def atesle(silah:Silah):
    silah.ates_et()

atesle(rpg7)
atesle(cross_bow)



