#Datetime Metotları:
# c:class
# v:variable
# f:function
# import datetime as dt
# dt.date.fromtimestamp()
# dt.date.strftime()
# dt.date.replace()
# dt.time.strftime()
#  gibi sürekli date yazmak yerine ;
# from datetime : date ulaşmak için

# from datetime import date as dt
# #dt.fromtimestamp()
# #dt.strftime()
#
# from datetime import time as tm

# --------------------------------
# from datetime import datetime as dt
# # şimdiki zaman:
# print(dt.now())   #2022-11-12 11:31:31.351365
#
# # bugünün tarihi:
# print(dt.today())  #2022-11-12 11:32:06.780526
#
# from datetime import date as d
# print(d.today())   #2022-11-12
#
# # tarih oluşturma:  "2022-11-12"
# import datetime as dtm
# # print(dtm.date(2022,11,12))
# # print(type(dtm.date(2022,11,12)))   #<class 'datetime.date'>

# Örnek:
from datetime import datetime as dt  #from dosyaAdi.py ,import class
from datetime import date as d
import datetime as dtm               #import dosyaAdi.py

simdik_zaman=dtm.date.today()
dogum_tarihi=dtm.date(1900,11,12)
# zamanlar arasında fark alma
fark=simdik_zaman-dogum_tarihi
print(fark)    #44560 days, 0:00:00
print(type(fark)) #<class 'datetime.timedelta'>
yas=fark.days/365
print(round(yas))    #122 yaşındaymış
tam_zaman=dt.now()
print(tam_zaman)     #2022-11-12 12:04:36.809493
# bizim zaman tipimiz: gün-ay-yıl TR
# DİĞER ÜLKELERDE:     ay-gün-yıl EN
# uzun hali:
gun=tam_zaman.day
yil=tam_zaman.year
ay=tam_zaman.month
# kısa hali:
'''
format için kullanılan semboller:
%Y :yıl(year)
%m: ay(month)
%d :gün(day)
%H: saat(hour)
%M: dakika(minute)
%S: saniye (second)
'''
# strftime: f format (time string olarak formatlıyor) tarihten stringe
print(tam_zaman.strftime("%d.%m.%Y"))  #12.11.2022
print(tam_zaman.strftime("%H:%M"))     #12:10
print(tam_zaman.strftime(("%d.%m.%Y      %H:%M"))) #12.11.2022      12:11

# strptime: p parse,stringden tarih cinsine
# 11.12.2022
tarih=dt.strptime("11.12.2022","%d.%m.%Y")
print(tarih)
print(type(tarih))       #<class 'datetime.datetime'>
print(tarih.timestamp()) #1670706000.0  #saniye cinsinden tarihin karşılığıdır.





