#ENUM:
# import enum yazılarak kullanılır.
# sabit değerler oluşucaksa enum kullanılabilir.mesela kargo oluşturma adımları,cinsiyet vb.
# standartı korumak için kullanılabilen bir modüldür.

import enum as e
class Cinsiyet(e.Enum):
    belirtilmemis=0
    kadin=1      # name=value bunlar sabit.
    erkek=2

print(Cinsiyet.erkek.name) #erkek
print(Cinsiyet.erkek.value) #2

class Ogrenci:
    def __init__(self,ad:str="",cinsiyet:Cinsiyet=Cinsiyet.belirtilmemis):
        self.ad=ad
        self.cinsiyet=cinsiyet

o1=Ogrenci()
o1.ad="nur"
o1.cinsiyet=Cinsiyet.kadin






