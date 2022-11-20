#----Modules: .py uzantılı dosyaları birbiri içinde import ederek
#kullanabilirsiniz.

#import PythonKonular.yasmetotlari as ym

yas=ym.dogum_tarihi_hesapla('1923-10-29')
print(yas)  #99

#from PythonKonular.yasmetotlari import emeklilik_yasi_hesapla as emh

print(emh('Nur','k','1980-10-22'))

#package: __init__.py dosyası bulunan klasörler package olarak görünür.

from istatistikselpackage import ortalamahesaplari as oh
#oh.aritmetik_ortalama()
#oh.agirlikli_ortalama()
import istatistikselpackage.ortalamahesaplari as oh
#oh.aritmetik_ortalama()
#oh.aritmetik_ortalama()
from istatistikselpackage.ortalamahesaplari import aritmetik_ortalama
#aritmetik_ortalama(1,2,3,4)
from istatistikselpackage.ortalamahesaplari import aritmetik_ortalama as ao
#ao(1,2,3,4)

#dışarıdan package yüklemek için pyPI'dan aradığımızı bulabiliriz.
#pypi.org
#terminalden yüklemek için >pip install numpy (pycharma gerek olmadığında)
# file >settings > project : <projectname> python interpreter > +iconu


#UYARI :# Eğer pycharm package için öneri sonmuyorsa:
# file >settings > project : <projectname> python structre >exclude görünen dosyaları
#source iconuna basaral include ediniz.

# import numpy as np
# print(np.zeros((3,3))) #başka cloudlardan package eklemeyebilriz.örneğin :numpy





