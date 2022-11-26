# Http İstekleri(request)
#Https
#Http:veri iletişimi için kullanılan bir yapıdır.
#https://www.abckres.com şelinde bir site yaptığında ,s olamayn bir yerden ödenme yapılması tehliikeli olabilir.s daha güvenli bir iletişim için kullanılır.
#eri tipi ortamlarında genellikle http şeklinde oluyor.
#www.abckres.cım ->domain
#bu domain'in arkasında bir ip adresi var.
#IP adresi -> 192.168.1.1
#reqres.in örnek veri döndüren bir adrestir.

#request -> adrese atılan istektir.hhtp istek.
#response -> adresten gelen cevaptır.

#https://reqres.in/api/users?page=2
#protokol://domain?querystring1=val1&querystring2=val2

#https://reqres.in/api/users
#request package indirilir.
#pip install requests (şeklinde package elde edebiliriz ya da file->settingden yapabiliriz.)
#requests pckage eklendi.

import requests as req
#Bu paketin içerisinde 4 tane istek atmamıza yardım edicek methodlar vardır.
#get,post,put,delete,patch gibi metotlar ile adrese istekler atılabilir.
#Http Methods:
# Adres:https://reqres.in/api/users
#JSON ile gönderiyoruz.
# bu adrese :
# --Get methodu: ile istek atarsak veri(tüm kullanıcılar) almış oluruz.
# --Post methodu: ile istek atılırsa yanında bir veri(kullanıcı) göndermemiz gerekir ve bu veriyi create edebiliriz.
# --Put/Patch metodu: update için,örneğin onların veri tabanında soyadımı değiştirmöek istediğimde put ya da patch kullanırız.
#patch daha kapasamlı veri dönderir.çoğu zaman put kullanılır.
# --Delete metotu: silme için kullanılır.

#respons=req.get("https://reqres.in/api/users")  #respons=burdan bana bir sonuç döndürülüyor.
#print(respons.status_code) #200
#print(respons.json()) #json ile de json formatına çeviriyoruz.
#print(type(respons.json())) #<class 'dict'>
# gelen=respons.json()
# calisanlar_listesi=gelen["data"]
# print(calisanlar_listesi)   #birden fazla istek attığımızda engelleniriz.

#rate limit:belli bir süre içinde belli bir sayıda istek atabilmesine izin verir.
#fazla istek atılırsa belli bir süre engellenebilirsiniz.429,418 gibi sonuçlar alırsanız:birr süre bekleyip yeniden deneyiniz.
#rate limit neden konulur ? ->DDOS koruma amaçlıdır.
#http status code :
'''
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429  --status code'lar.
*:en sık dönen değerler.
1xx:information
2xx:başarılı durumlar *200,201,204 vb.
3xx:yönlendirme durumları www.google.com->www.goooogle.com adres taşınmıştır ve yönlendirme yapıp sonuç döndürür.
4xx:client hataları.(istemci hatası) *404,*429,*418->ı am a teapot.*401:yetkisiz giriş
5xx:server hataları *500 developer hatası da olabiir.
'''

#sürekli istek atmamak için gelen cevabı bir dosyada saklayıp o dosyadan okumak rate limit'e takılmamamızı sağlar.
#örnek: yukarıdaki adresten aldığınız sonuca göre çalışanların ad.soyad@bilgeadam.com şeklinde mail adreslerini oluşturunuz.daha önce yazdığımız mail oluşturma methodunu kullanarak yapınız.
#bu methodu önce bir package içine koyunuz ve oradan kullanınız.

# from mymailpackage.mail_methodlari import mail_olustur
# gelen=respons.json()
# calisanlar_listesi=gelen["data"]
# print(calisanlar_listesi)
#
# mailler=[]
# for calisan in calisanlar_listesi:
#     calisan_ad=calisan["first_name"]
#     calisan_soyad=calisan["last_name"]
#     calisan_mail=mail_olustur(calisan_ad,calisan_soyad,"bilgeadam.com")
#     mailler.append(calisan_mail)
# print(mailler)


#örnek:
#parametreli istek atma:
# calisan_id=4
# req.get(f"https://reqres.in/api/users/{calisan_id}")

#https://reqres.in/api/users?id=4
# res1=req.get("https://reqres.in/api/users",params={"id":4})  #({"page":2}) #page parametresi örnek olarak yazıldı.
# print(res1.json()["data"])

#post isteği gönderme
# res2=req.post("https://reqres.in/api/users",data={"name":"nur","job":"eğitmen"})
# if res2.status_code==201:
#     print(res2.json())
# else:
#     print("istek başarısız sonuçlandı.")

#https://dummy.restapiexample.com/
# bu adrese bir istek atıcaz.

import requests as req
# res=req.get("https://dummy.restapiexample.com/api/v1/employees"
#             ,headers={"user-agent":"pythondan"}) #headers gönderdiğinizde 200 döner.
# print(res.status_code) #406
# print(res.json())

#https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa--uzantı adresi

#attığınız istekten 200 geldiğinde gelen "data" kısmını employees.json adında bir dosya içine yazdırınız.sonraki işlemlerde bu json'dan veriyi okuyarak işemleri yapırız.
#ortalama çalışan maaşlarını hesaplayınız.
import json
import requests as req
def verileri_cek():
    res = req.get("https://dummy.restapiexample.com/api/v1/employees", headers={"user-agent": "pythondan"})
    if res.status_code == 200:
        # datayı okuyup json dosyasına yazdırıcaz.
        gelen = res.json()  # dict
        json.dump(gelen["data"], open("employees.json", encoding="utf8", mode="w"), ensure_ascii=False)
        print("dosya oluşturuldu")
    else:
        print("hata oldu!")

#verileri_cek()

#import istatistikselpackage.ortalamahesaplari as oh
calisanlar=json.load(open("employees.json",encoding="utf8"))
maaslar=[]
for calisan in calisanlar:
    maaslar.append(float(calisan["employee_salary"]))
print(maaslar)
import statistics as s
print(s.mean(maaslar)) #276865.4166666667

# import istatistikselpackage.ortalamahesaplari as oh
# ort_maas=oh.aritmetik_ortalama(maaslar)
# print(ort_maas)






















