# # #Genel tekrar ve örnekler:
# # # 1-) List
# # # METOTLAR:
# # # 1-)index:
# # # index 0'dan başlar.
# # # örnek:
# # isimler=["gonca","ebru","ozan","çağla","nilsu"]
# # # print(isimler[0]) #gonca
# # # print(isimler[3]) #çağla
# # for i in isimler:
# #     print(i)
# # # 2-) append:
# # # listede olmayan bir veriyi ekleyebiliriz.
# # # tüm veri tiplerinden veri türü eklenebilir.
# # # örnek:
# # isimler=["gonca","ebru","ozan","çağla","nilsu"]
# # isimler.append("emine")
# # print(isimler)  #['gonca', 'ebru', 'ozan', 'çağla', 'nilsu', 'emine']
# # # 3-) insert:
# # # insert metotu listeye istediğin indexe sonradan bir veri eklemektedir.
# # # örnek:
# # isimler.insert(3,"duygu")
# # print(isimler) #['gonca', 'ebru', 'ozan', 'duygu', 'çağla', 'nilsu', 'emine']
# # # 4-) extend:
# # # Birden fazla veriyi aynı anda ekleyebilir.
# # # Tupple gibi collectionlarıda ekleyebilir,ve hepsini list'e çevirir.
# # # örnek:
# # isimler.extend(["mehmetcan","sevilay","kerem"])
# # print(isimler)
# # # 5-) reverse:
# # # Listeyi ters çevirir.
# # isimler.reverse()
# # print(isimler)
# # rakamlar=[1,2,3,4,5,6,7,8,9]
# # rakamlar.reverse()
# # print(rakamlar)
# # # 6-) sort:
# # # Listeyi büyükten küçüğe doğru sıralar.
# # # örnek:
# # rakamlar.sort()
# # print(rakamlar)
# # # 7-) clear:
# # # Listeyi boş bir listeye çevirir.
# # rakamlar.clear()
# # print(rakamlar)
# # # 8-) del :
# # # Listeyi tamamen ram üzerinden siler.Referansı siler.
# # # del rakamlar
# # # print(del)
# # # 9-) copy:
# # renkler=["mavi","yeşil","mor"]
# # renklerin_kopyasi=renkler.copy()
# # print(renklerin_kopyasi)
# # # 10-) count:
# # # Listede arattığımız veriden kaç tane olduğunu verir.
# # # Bulamazsa 0 döndürür.
# # meyve=["çilek","muz","elma"]
# # meyve_varmi=meyve.count("çilek")
# # print(meyve_varmi)
# # # 11-) remove:
# # # Listenin içindeki value yu siler.İndex ile değil.
# # meyve.remove("çilek")
# # print(meyve)
# # # 12-) pop:
# # # Listenin içindeki son veriyi siler,eğer index belirtilirse index değerini siler ve döndürür.
# # taki=["küpe","saat","kolye"]
# # taki.pop()
# # print(taki)
# # taki.pop(0)
# # print(taki)
# # # 13-) len :
# # # Collection içindeki eleman sayısını verir.
# # gol=["abant","yedigöl","gölcük","gölyazı"]
# # print(len(gol))
# # # 14-) sum:
# # digit=[1,2,3,4,5,6,]
# # print(sum(digit))
# # # 15-) min/max:
# # print(min(digit))
# # print(max(digit))
# # # 16-) any :
# # print(any("1")) #true
# # # Slicing nedir ?
# # # index yapısından dolayı kullanılır.
# # isimler=["damla","aykut","umut","neslihan","tayfun","emre","gonca","elifsu","mert"]
# # print(len(isimler)) #9
# # print(isimler[0]) #damla
# # print(isimler[2]) #umut
# # # en sonuncu elamanı nasıl bulunur ?
# # en_sonuncu_eleman=len(isimler)-1
# # print(isimler[en_sonuncu_eleman]) #mert
# # # ÖRNEK:
# # print(isimler[2:5]) #2.indexten 5.indexe kadar.(5.index dahil değildir.) --#['umut', 'neslihan', 'tayfun']
# # print(isimler[2:]) #2.indexten sonraki bütün indexler dahildir. -#['umut', 'neslihan', 'tayfun', 'emre', 'gonca', 'elifsu', 'mert']
# # print(isimler[:5]) #['damla', 'aykut', 'umut', 'neslihan', 'tayfun']
# # print(isimler[2:-2]) #['umut', 'neslihan', 'tayfun', 'emre', 'gonca']
# # print(isimler[:]) #tüm elemanları verir.
# #
# # # Örnek:
# # # 1 den girilen sayıya kadar olan sayıları bir listeye ekleyen bir uygulama yazınız.
# # girilen_sayi=int(input("Lütfen bir sayı giriniz:"))
# # liste=[]
# # for i in range(1,girilen_sayi+1):
# #     #liste.append(i) #append listeye ekleme
# #      liste.insert(i-1,i)
# # print(liste)
# # # Örnek:
# # rakam=int(input("Bir rakam giriniz:"))
# # liste=[]
# # for i in range(1,rakam+1):
# #     liste.insert(i-1,i)
# # print(liste)
# # # Örnek:
# # rakam1=int(input("Bir sayı giriniz:"))
# # liste=list()
# # liste.extend(range(1,rakam1+1))
# # print(liste)
# #
# # # Örnek:İnputtan 2 sayı alınız,ilk girilen sayı
# # # küçük ise artan sırayla;büyük ise azalan sırayla bir liste oluşturunuz.
# # sayi1=int(input("Birinci sayı giriniz:"))
# # sayi2=int(input("İkinci sayıyı giriniz:"))
# # liste=list()
# # if sayi1 < sayi2:
# #     liste.extend(range(sayi1,sayi2+1))
# # else:
# #     liste.extend(range(sayi1,sayi2-1,-1))
# # print(liste)
# #
# # print(ord("a")) #97
# # print(chr(98)) #b
#
# # Örnek: A'dan Z'ye kadar olan harfleri döngü ile listeye ekleyiniz.
# liste=list()
# for i in range(ord("A"),ord("Z")+1):
#     liste.append(chr(i))
# print(f"Büyük harf listesi:{liste}")
#
# liste=[]
# for i in range(ord("a"),ord("z")+1):
#     liste.append(chr(i))
# print(f"küçük harf listesi:{liste}")
#
# liste=list()
# for i in range(ord("!"),ord("?")+1):
#     liste.append(chr(i))
# print(f"Semboller listesi:{liste}")
#
# liste=[]
# for i in range(ord("0"),ord("9")+1):
#     liste.append(chr(i))
# print(f"Rakamlar listesi:{liste}")
#
#
# #ÖRNEK:SAYILAR İSİMLİ BİR LİSTEYE 10 TANE RASTGELE SAYI ÜRETEREK EKLEYİNİZ.ÜRETİLECEK SAYILAR (1-100)
# # ARASINDA OLSUN.
# # import random as rnd
# # sayilar=list()
# # for i in range(10):
# #     rastgele_sayilar=rnd.randint(1,100)
# #     sayilar.append(rastgele_sayilar)
# # print(sayilar)
#
# # geliştme versiyonu:eğer üretilen sayı bir daha varsa eklemeyecek !
# # import random as rnd
# # sayilar=[]
# # for i in range(10):
# #     rsayi=rnd.randint(1,100)
# #     if sayilar.count(rsayi)==0: #count:var mı ? varsa ekleme komutu.
# #         sayilar.append(rsayi)
# # print(sayilar)
#
# # # while ile yapılması:
# # import random as rnd
# # index=0
# # while index<10:   #while daime true değer döndürdüğünde çalışır ve sonsuz döngüye girmemesi için durdurucu etki
# # # konulması gerekir.
# #     rastgle_sayi = rnd.randint(1, 100)
# #     if sayilar.count(rastgle_sayi)==0:
# #         sayilar.append(rastgle_sayi)
# #         index +=1
#
# # bu döngünün kaç kez döndüğünü nasıl bulabilriz ?
# import random as rnd
# dongu_kac_kez_dondu=0
# sayilar=[]
# while len(sayilar)<10:
#
#     rastgle_sayi=rnd.randint(1,100)
#     if sayilar.count(rastgle_sayi)==0:
#         sayilar.append(rastgle_sayi)
#         dongu_kac_kez_dondu+=1
#
# print(sayilar)
# print(dongu_kac_kez_dondu)
#
#
# # sayısal loto oyunu:
# # Müşteriden kaç kolon oynamak istediğini alalım.Sonrasında
# # 1 kolan için 1-49(49) dahil rastgele 6 tane sayı üretilsin ve bir listeye eklesin
# # ve kçükten büyüğe doğru sıralansın.
# # Her kolan için aynı işlemler yapılsın.
#
#
# kullanici_girisi=int(input("Lütfen kaç kolon oynamak istediğinizi giriniz(4-6): "))
# import random as rnd #rastgele sayı üretildi.
# kolon=list()         #bir liste tanımı yapıldı.
# index=0              #index tanımı yapıldı başlangıç değer için.
# while index<6:# while ile 6 ya kadar bir liste oluştu.
#     rastgele_sayi=rnd.randint(1,49)      #1-50 arasında rastgele sayı üretildi.
#     kolon.append(rastgele_sayi)          #kolon listesine rastgele sayı eklendi
#     kolon.sort()                         #sort metodu ile sıralandı.
#     index +=1                            #sonsuz döngü için durdurma yapıldı.
# print(kolon)                             # ve kolon print edildi...
#
# # Örnek:# kullanıcı hayır(h) diyene kadar veri almaya ve girilen değeri bir listeye eklyen uyg.yazınız.
# # # Listeye hem index no hemde veri ile birlikte alt alta yazdırınız.
# # # 1.ankara
# # # 2.izmir
# # # 3.adana
#
# iller=[]
# while True:
#     il=input("Lütfen il giriniz:")
#     iller.append(il)
#     girilen=input("Devam etmek istiyor musunuz? e/h").lower()
#     if girilen=="h":
#         break
# for i in range(len(iller)):
#     print(f"{i+1}.{iller[i]}")
#
#
# # Örnek:
# # password generator:
# # kaç karakterli bir şifre istiyorsunuz ? 6
# # büyük harf istiyor musunuz ? e  [A B C D E ...Z]
# # küçük harf istiyor musunuz ? e  [a b c d ...z]
# # rakam istiyor musunuz ? e [0 1,2....9]
# # sembol istiyor musunuz ? h
# # Ascii table
# # t 3 _ _ _ _ _
# import random as rnd
# karakter_sayisi=int(input("Lütfen kaç karakterli şifre istediğinizi giriniz:"))
# buyuk_harf=input("Büyük harf istiyor musunuz ? e/h")
# kucuk_harf=input("Küçük harf istiyor musunuz ? e/h")
# rakam=input("Rakam istiyor musunuz ? e/h")
# sembol=input("Sembol istiyor musunuz ? e/h")
# buyuk_harfler=[]
# kucuk_harfler=[]
# rakamlar=list(range(0,10))
# semboller=[]
# for i in range(ord("A"),ord("Z")+1):
#     buyuk_harfler.append(chr(i))
# for i in range(ord("a"),ord("z")+1):
#     kucuk_harfler.append(chr(i))
#
# for i in range(ord("!"),ord("/")+1):
#     semboller.append(chr(i))
#
# password=""
# while len(password)<karakter_sayisi:
#     uretilen=rnd.randint(0,3)
#     match uretilen:
#         case 0 : #büyük harfler için
#             if buyuk_harf=="e":
#                 password +=buyuk_harfler[rnd.randint(0,len(buyuk_harfler)-1)]
#
#         case 1: # küçük harfler için
#             if kucuk_harf=="e":
#                 password += kucuk_harfler[rnd.randint(0,len(kucuk_harfler)-1)]
#         case 2 :#rakamlar için
#             if rakam=="e":
#                 password += str(rakamlar[rnd.randint(0,len(rakamlar)-1)])
#         case 3 :#semboller için
#             if sembol=="e":
#                 password += semboller[rnd.randint(0,len(semboller)-1)]
# print(password)


# 2-)Tuple
# tuple collection çeşitidir.
# listten farkı değeri sonradan değişitirilemez.
# () tanımlaması bu şekilde yapılır.
# slicing yapılır.
# index mantığı vardır.
# t1=() boş bir tuple örneğidir.
# t2=(1,1,1,2,3,4,5,6)
# print(t2)
# print(type(t2))  #<class 'tuple'>
# print(t2[0])   #0.indexi 1
# print(t2[1])   #1.indexi 1
# print(t2[2])   #2.indexi 1
# print(t2[3])   #3.indexi 2
# # VERİ ALMAK İSTEDİĞİMİZ ZAMAN:
# #tuple'ların değerini sonradan değiştirilemez
# # COUNT METOTU:
# print(t2.count(1))   #1 den kaç tane var ? #3 tane var.
# print(t2.count(2))   #4 den kaç tane var ? #1 tane var.
# # index metotu:
# print(t2.index(4))  #4.veri kaçıncı indexte ? #5
# print(t2.index(5))  #5.veri kaçıncı indexte ? #6
# # del metotu:
# # tuple değer değiştirmediği için;
# # del t2[3]  #TypeError: 'tuple' object doesn't support item deletion
# # direk değer silmek gibi bir şey yaparsak error verir tanımlanan tuple'ı direk silmek gerekiyor
# # del t2
# # print(t2)  #ramdan tamamen silindi.
#
# # Slicing :
# sayilar1=[11,12,13,14,15,16]
# print(sayilar1[2:4])          #[13, 14]  (list örneği)
# sayilar=(11,12,13,14,15,16)
# print(sayilar[2:4])           #(13, 14)  (tuple örneği)
# print(sayilar[:])             #(11, 12, 13, 14, 15, 16)
# print(sayilar[2:])            #(13, 14, 15, 16)
# print(sayilar[:-3])           #(11, 12, 13)
# '''
# Tuple vs list
# -tuple kopya üretemiyor.ram üzerinden bakılıyor.daha az ram kullanır.
# içinde dğişiklik olamayacağı için az veri ve ram kullanımından dolayı tuple kullanılır.,
# -tuple nesnenin kopyasını üretmez direkt olarak nesnenin kendisini kullanır,list ise
# nesnenin kopyasını üreterek çalışır.
# -boyutları sabit olduğundan ramde sıkıştırılmış olarak tutulurlar.
# -list'lere append denildiğinde fazladan yer açarak boyutlanır.
# '''
# # 3-) SET
# '''
# Diğer bir collection şeklidir.
# matematikteki küme mantığına benzer.
# tanımlaması : {} şeklindedir.
# ancak bu şekilde boş bir tanımlama set için geçerli değildir çüünkü
# bu tanımlama dictionarye aittir.
# index yapısı yoktur.
# slicing yoktur.
# eleman tekrarı yok.
# içerisinde ki tanımlanan elemanlar değiştirilebilir ve ya silinebilir.
# '''
# s1={}
# print(type(s1))   #<class 'dict'>
# s3=set()
# print(type(s3))   #<class 'set'>
# s2={1,2,3}
# print(type(s2))   #<class 'set'>
#
# s4={1,1,1,1,2,4,6,8}
# print(len(s4))  # eleman tektarı yoktur. len --5
#
# # SET METOTLARI:
# # add
# digit={1,2,3,4,5}
# print(digit)
# digit.add(6)
# print(digit)
#
# s3={1,1,1,1,2,3,4,5}
# print(len(s3))    #5
# s3.add(6)
# s3.add(7)
# s3.add(8)
# print(len(s3))   #8
#
# # update:
# s3={1,1,1,1,2,3,4,5}
# s3.update((7,8,9))
# s3.update((10,11,12))
# print(s3)
#
# # discard:istenilen elamanı siler. bulamazsa hata döndürmez.
# a1={1,2,3,4,5,6,7,8,9}
# a1.update((10,11))
# print(a1)            #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
# a1.discard((9))
# print(a1)            #{1, 2, 3, 4, 5, 6, 7, 8, 10, 11}
# a1.discard(23)
# print(a1)           #hata döndürmedi.
#
# # remove: istenilen elemanı siler fakat o elemanı bulamazsa hata verir.
# #a1.remove(23)
# #print(a1)          #KeyError: 23
#
# # pop: set'in baştaki elemanını siler ve elemanı size verir.
# odd={1,3,5,7}
# print(odd.pop())
#
# # clear: siler.
# print(odd.clear())
# # copy: başka bir listeye atıyor.
#
# # difference: fark bulma.
# a_kumesi={1,2,3,4,5,6,7,8,9,10,11}
# b_kumesi={10,11,12,13,14,15,16,17}
# print(a_kumesi)
# # a_kumesi_farki=a_kumesi.difference(b_kumesi)
# # print(a_kumesi_farki)  #{1, 2, 3, 4, 5, 6, 7, 8, 9}
# # b_kumesi_farki=b_kumesi.difference(a_kumesi)
# # print(b_kumesi_farki)  #{12, 13, 14, 15, 16, 17}
#
# # difference update: farkını bulur ve ana set üzerinde farkı siler.
# a_kumesi.difference_update(b_kumesi)
# print(a_kumesi) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

# intersection:  kesişimlerini bulur.
# q={"a","b","c","d","e","f","g"}
# w={"a","b","c","t","y","n","m"}
# kesisim=q.intersection(w)
# print(f"kümelerin kesişimi:{kesisim}")
# # union: birleşimlerini bulur.
# birlesim=q.union(w)
# print(f"kümelerin birleşimi:{birlesim}")

# s3.isdisjoint(s4):kümelerin ayrık olup olmadığını döner.
# True/False döner
# s3.issubset(s4):küme diğerinin alt kümesi mi?
# s3.issuperset(s4):kümenin diğer kümeyi kapsamadığını döner.
# ---CRUD :create read update delete..(list daha çok karşınıza çıkar)

#4-) Dictionary
'''
-key-value şeklinde veri tutar.
-{} içinde tanımlanır. set gibi değil.{key:value} şeklinde tanımlanır.
-key:string,numeric ve ya tuple cinsinden tanımlanabiir.
birden fazla aynı isimden key kullanılırsa en son hangisi tanımlandıysa onun value'sunu verir.
-aynı keyden birden fazla tanımlama yapmayın demek isteniyor.
-value:tüm veri tiplerinden tanımlanabilir.
'''

# ogrenci={"gonca","çomak",25} #bu bir set örneği
# ogrenci1={
#     "ad":"gonca",
#     "soyad":"çomak",
#     "yaş":25
# }
# print(ogrenci1)
# print(ogrenci1["ad"]) #bu şekilde veri istenebilir.
# ogrenci1["ad"]="goncagül"
# print(ogrenci1["ad"]) #veri güncellenebilir.

#del ogrenci1
#print(ogrenci1)  #veri silindi.

# Dictionary metotları:
# erkek1={
#     "isim":"Mert",
#     "soyisim":"YAMAN",
#     "yaş":26,
#     "boyu":1.90,
#     "kilo":80,
#     "okul":"Abant İzzet Baysal Üniversitesi"
# }
# print(erkek1)
# # update:veri eklemek için kullanılır.
# erkek1.update(isim="MertCan")
# print(erkek1)
# # pop:veri silmek için kullanılır
# erkek1.pop("yaş")
# print(erkek1)
# # popitem:son veriyi siler.
# erkek1.popitem()
# print(erkek1)
# # get:değeri döndürür.
# print(erkek1.get("isim")) #Mert


#   ıtems: for ile kullanacağız.
#print(erkek1.items())  #tuple listesi
#print(erkek1.keys()) #dict_keys(['isim', 'soyisim', 'yaş', 'boyu', 'kilo', 'okul'])
#print(erkek1.values())  #dict_values(['Mert', 'YAMAN', 26, 1.9, 80, 'Abant İzzet Baysal Üniversitesi'])

# for (key,value) in erkek1.items():
#     print(f"Key:{key},Value:{value}")
# for i in erkek1.values():
#     print(i)
# for i in erkek1.keys():
#     print(i)
#
# ogrenciler=[
#     {
#         "ad":"nur",
#         "soyad":"öztürk",
#         "il":"ankara"
#     },
#     {
#         "ad":"damla",
#         "soyad":"kahraman",
#         "il":"izmir"
#     },
#     {
#         "ad":"tayfun",
#         "soyad":"karakavuz",
#         "il":"izmir"
#     }
# ]
# print(ogrenciler[1]) #{'ad': 'damla', 'soyad': 'kahraman', 'il': 'izmir'}
# print(ogrenciler[1]["ad"])   #damla
# print(ogrenciler[2]["il"])   #izmir
# # -----------------------------------------------------------------------------
# #METOTLAR:
# #bir kez tanımlayıp birden fazla kez kullandığımız yapılardır.
# #1-)Hazır sistemdeki metotlar
# #string metotlar
# #matematiksel metotlar
# #datetime metotlar
# #2-)Custom yazılan metotlar
# #2 ye ayrılır:
# # 2.a-)Geri değer dönen metotlar
# # 2.b-)Geri değer dönmeyen metotlar
#
# # ---------------------------------------------------------------------------------
# # String metotlar:
# '''
# stringler karakterler dizisidir.
# örneğin harf="g" bir stringdir.
# yazı="merhaba dünya"
# isim="gonca"
# bunlar bir stringdir.
# '''
#
# metin="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tristique justo ante, at fringilla libero imperdiet non."
# print(len(metin))
# print(metin.lower())
# print(metin.upper())
# print(metin.count("a")) #6
# print(metin.capitalize()) #metnin ilk harfini büyütür.
# print(metin.startswith("Lorem")) #true #büyük küçük harf duyarlılığı vardır.
# print(metin.endswith("."))    #true
# print(metin.find("sit")) #18 indexi boşluk ve sembollerde sayılır.
# print(metin.index("sit")) #18
# #print(metin.index("abc")) #değer dönmez yoksa.
# print(metin.replace("Lorem","totem"))
#
# ayrilmis_liste=metin.split('.')
# print(ayrilmis_liste)
# print(len(ayrilmis_liste))
#
# mailler="nur.ozturk@bilgeadam.com;ahmet.ata@bilgeadam.com;sema.yilmaz@bilgeadam.com"
# mail_liste=mailler.split(";")
# # print(mail_liste)
# print(mailler.replace(";","---").split("@bilgeadama.com"))
# print(metin.title()) #ilk harf büyür.

# # Örnek:
# girilen=input("Bir sayı giriniz:")
# if girilen.isdigit():
#     print("sayısal hale dönüştürülebilir.")
#     sayi=int(girilen)
# else:
#     print("metin içinde harf ve ya sembol var.")
#
# print(girilen.isalnum())
# print("merhaba dünya".center(20,"*")) #***merhaba dünya****
# print("hello".center(9,"+"))          #++hello++

# ÖRNEK:
# kullanici_girisi=float(input("Sayi giriniz:"))
# islem=kullanici_girisi**2
# print(f"Sayının karesi:{islem}")
#
# fonksiyon olarak nasıl yazılır ?
# def kare_fonksiyon(a:int,b:int):
#     kare_islemi=pow(a,b)
#     print(f"Sayının karesi:{kare_islemi}")
#
# kare_fonksiyon(3,2)
#
# def kare_al(a):
#     us_alma=a**2
#     print(f"Sayının karesi :{us_alma}")
# kare_al(9)
#
# def karekok_al(a:float)->int:
#     import math
#     kok_alma_islemi=math.sqrt(a)
#     print(f"Sayının karekökü:{kok_alma_islemi}")
# karekok_al(81)


#BÜTÜK ÖRNEK ÇÖZÜMLERİ:
#1-)Kullanıcıdan alınan bir sayının karesini bulan ve ekranda gösteren uygulamayı yazınız.
#kullanici_girisi=int(input("Lütfen bir sayı giriniz:"))
#kare_bulma=pow(kullanici_girisi,2)
#print(f"Girdiğiniz sayının karesi:{kare_bulma}")

# 2-) Kullanıcıdan vize ve final notunuzun ortalamasını istediği programı yazınız.

# vize=float(input("Lütfen vize notunuzu giriniz:"))
# final=float(input("Lütfen final notunuzu giriniz:"))
# average=(vize*0.4)+(final*0.6)
# print(f"Vize ve final notunuzun ortalaması:{average}")

#3-) kullanıcının adını ve soyadını alarak ad.soyad@bilgeadamakademi.com şeklinde
# bir mail adresi oluşturan ve gösteren uygulamayı yazınız.

# ad=input("Lütfen isminizi giriniz:")
# soyad=input("Lütfen soyisiminizi giriniz:")
# mail_adresi=f"{ad}.{soyad}@bilgeadamakademi.com"
# print(f"mail adresi:{mail_adresi}".lower().replace("ç","c"))

# #4-) kullanıcıdan isim isteyip doğru olup olmadığını kontrol ediniz.
# kullanici_adi=input("Kullanıcı adınızı giriniz:")
# if kullanici_adi=="Bilgeadamakademi":
#     print("Doğru cevap")
# else:
#     print("yanlış cevap")
#
# #5-)Girilen bir sayının negatif/pozitif olması durumunu kontrol ediniz.ve ekranda durumunu gösteriniz.
# sayi=int(input("bir sayı giriniz:"))
# if sayi==0:
#     print("sayı 0 dır.")
# elif sayi>0:
#     print("sayı pozitiftir.")
# else:
#     print("sayı negatiftir.")
#
# #6-) Girilen bir sayının çift/tek olmasını bulunuz ve ekrana yazdrınız.
#
# sayi1=int(input("Lütfen bir sayı giriniz:"))
# if sayi1%2==0:
#     print("sayi çift.")
# else:
#     print("sayı tektir.")
#
# #7-) Girilen bir x sayısının,yine kullaıcıdan istenen bir
# # y sayısına tam bölünüp bölünmediğini kontrol ediniz ve ekranda göteriniz.
#
# sayi_1=int(input("birinci sayıyı giriniz:"))
# sayi_2=int(input("ikinci sayıyı giriniz:"))
# islem=sayi_1%sayi_2
# if  sayi_2==0:
#     print("Lütfen sıfır dışında bir sayı giriniz.")
# elif islem!=0:
#     print(f"tam bölünemez.")
# else:
#     print("tam bölünür.")
#
# #8-) Girilen iki sayıdan hangisinin büyük olduğunu bulan uygulamayı yazınız.
# a=int(input("1.sayıyı giriniz:"))
# b=int(input("2.sayıyı giriniz:"))
# if a>b:
#     print(f"1.sayı 2.sayıdan daha büyüktür:{a},{b}")
# elif a==b:
#     print(f"Girilen sayılar birbirine eşittir:{a},{b}")
# else:
#     print(f"2.sayı 1.sayıdan büyüktür:{a},{b}")
#
# #9-) Girilen vize notunun 0-100 arasında olmasını kontrol ediniz.
# # eğer doğru giriş yapıldıysa giriş başarılı uyarsını gösterelim.
# # eğer ortalama 50 ve üzerinde ise geçti değilse kaldı yazdıralım.
#
# vize_notu=float(input("Lütfen vize notunuzu giriniz:"))
# final_notu=float(input("Lütfen final notunuz giriniz:"))
# ortalama=(vize_notu*0.4)+(final_notu*0.6)
# if vize_notu>0 and vize_notu<100:
#     print("Giriş başarılıdır.")
#     if ortalama>=50:
#         print("geçtiniz.")
#     elif ortalama<50:
#         print("Sınıfta kaldınız. !")
#
# else:
#      print("Lütfen notlarınızı tekrar giriniz.")

#10-)
'''
Eğer ortalama:
  0-30 aralığında ff
  31-50 DD
  51-70 CC
  71-90 BB
  91-100 AA
harf notunu belirleyen ve ortalama ile birlikte ekranda gösteren uyglamayı yazınız.
'''
# vize=float(input("vize notu :"))
# final=float(input("final notu:"))
# ortalama=(vize*0.3)+(final*0.7)
# harf_notu=""
# if 91< ortalama <100:
#     harf_notu="AA"
# elif 71 < ortalama <90:
#     harf_notu="BB"
# elif 51 < ortalama < 70:
#     harf_notu="CC"
# elif 31< ortalama < 50:
#     harf_notu="DD"
# else:
#     harf_notu="FF"
# print(f"Harf notunuz:{harf_notu},vize :{vize},final:{final}")

#11-) kullanıcıdan kullanıcı adı ve şifre istedikten sonra
# ka:admin ve şifre:1234 ise giriş başarılı değilse,
# hangi bilgi hatalıysa onun uyarısını veren bir uygulama yazınız.

# kullanici_adi=input("Lütfen kullanıcı adınızı giriniz:")
# sifre=int(input("Lütfen şifrenizi giriniz:"))
# if kullanici_adi=="admin" and sifre==1234:
#      print("Kullanıcı adı ve şifre doğru,GİRİŞ BAŞARILIDIR.")
# elif kullanici_adi=="admin" and sifre!=1234:
#      print("Şifre yanlış,tekrar deneyiniz.")
# elif kullanici_adi!="admin" and sifre==1234:
#      print("Kullanıcı ismi yanlış,tekrar deneyeniz.")
# elif kullanici_adi!="admin" and sifre!=1234:
#      print("Kullanıcı adı ve şifre yanlış.")
# else:
#      print("Lütfen bilgileri kontrol ediniz.")

#12-)
# Kullanıcıdan sipariş etmek istediğin kitap sayısını alarak indirim uygulayan
# ve müşteriye ödemesi gereken tutarı,indirim oranını ve indirimsiz fiyatı gösteren
# uygulamayı yazınız.İndirim oranları aşağıdadır:
'''
birim fiyatı:10 tl
kitap sayısı;
20'den az ise %5 indirim 
20-50 ise %10
50-100 ise %15
100'den fazla ise %24 indirim
'''
# kitap_adeti=int(input("Lütfen sipraiş etmek istediğiniz kitap sayısını giriniz:"))
# birim_fiyati=10
# indirimsiz_fiyat=kitap_adeti*birim_fiyati
# indirim_orani=0
# if kitap_adeti<20:
#     indirim_orani=0.5
# elif 20 < kitap_adeti <50 :
#     indirim_orani=0.10
# elif 50 < kitap_adeti <100:
#     indirim_orani=0.15
# elif kitap_adeti>100:
#     indirim_orani=0.24
# indirimli_fiyat=indirimsiz_fiyat-(indirimsiz_fiyat*indirim_orani)/100
# print(f"kitap sayısı:{kitap_adeti},indirimsiz fiyat:{indirimsiz_fiyat},indirim oranı:{indirim_orani*100},"
#       f"indirimli fiyatı :{indirimli_fiyat}")

#13-)
# Kullanıcıdan almak istediği ürünü isteyerek ürünün hangi reyonda olduğunu gösteren bir uygulama yapınız.
'''
Domates,biber,patlıcan ->Sebze reyonu
Parfüm,diş macunu,şampuan ->Kozmetik
Cep Telefonu,bilgisayar,ses sistemleri ->Teknoloji reyonu
bunlar dışında bir giriş yapılırsa "ürün bulunmamaktadır" uyarısı vericektir.
'''

# urun_cesiti=input("Lütfen istediğiniz ürünü giriniz:").lower()
# mesaj=" "
# if urun_cesiti=="domates" or urun_cesiti=="biber" or urun_cesiti=="patlıcan":
#     mesaj ="Sebze reyonu"
# elif urun_cesiti=="parfüm" or urun_cesiti=="diş macunu" or urun_cesiti=="şampuan":
#     mesaj="Kozmetik reyonu"
# elif urun_cesiti=="cep telefonu" or urun_cesiti=="bilgisayar" or urun_cesiti=="ses sistemleri":
#     mesaj="Teknoloji reyonu"
# else:
#     mesaj="böyle bir ürün bulunmamaktadır."
# print(f"Almak istediğiniz ürün çeşiti:{urun_cesiti},Bulunduğu reyon:{mesaj}")

#14-) # 1-10 arasında rastgele üretilen 3 adet sayının hangisinin
# büyük olduğuna bulan ve ekranda hem sayıları hem en büyük sayı:{x} gibi yazdıran uygulamayı yazınız.

# import random
# s1=random.randint(1,10)
# s2=random.randint(1,10)
# s3=random.randint(1,10)
#
# if s1>s2 and s1>s3:
#     print(f"En büyük sayı s1'dir:{s1},s2:{s2},s3:{s3}")
# elif s2>s1 and s2>s3:
#     print(f"En büyük sayı s2'dir:{s2},s1:{s1},s3:{s3}")
# elif s3>s1 and s3>s2:
#     print(f"En büyük sayı s3'dür:{s3},s1:{s1},s2:{s2}")
# else:
#     print("sayı bulunamamıştır.")


#15-)
# girilen boy ve kilo bilgileri ile beden kitle indekxi hesaplayan bir uygulama yazınız:
# BKI=Kilo/(boy**2)  kilo(kg) boy(m)
'''
# • Beden kitle/kütle indeksi < 18,5 ise Zayıf
# •    18,5 < Beden kitle/kütle indeksi < 24,9 ise Normal
# •    25 < Beden kitle/kütle indeksi < 29,9 ise Fazla kilolu
# •    30 < Beden kitle/kütle indeksi < 34,9 ise I. derece obez
# •    35 < Beden kitle/kütle indeksi < 39,9 ise II. derece obez
# •    Beden kitle/kütle indeksi > 40 ise III. derece obez

'''
# boy=float(input("Lütfen boyunuzu giriniz(m):"))
# kilo=float(input("Lütfen kilonuzu giriniz[kg):"))
# index=kilo/(boy**2)
# bki=""
# if index<18.5:
#     bki="ZAYIF"
# elif 18.5 < index < 24.9:
#     bki="NORMAL"
# elif 25 < index <29.9:
#     bki="FAZLA KİLOLU"
# elif 30 < index < 34.9:
#     bki="I.DERECE OBEZ"
# elif 35 < index < 39.9:
#     bki="II.DERECE OBEZ"
# else:
#     bki="III.DERECE OBEZ"
#
# print(f"BOY:{boy},KİLO:{kilo},Beden kitle indexi:{bki}")

#16-) match-case ile gün yazmak:

# haftanin_gunleri=input("Lütfen gün giriniz:")
# match haftanin_gunleri:
#     case "pazartesi":
#         print("haftanın 1.günü")
#     case "salı":
#         print("haftanın 2.günü")
#     case "çarşamba":
#         print("haftanın 3.günü")
#     case "perşembe":
#         print("haftanın 4.günü")
#     case "cuma":
#         print("haftanın 5.günü")

#17-)# and ile match örneği:
# kullanıcıdan kullanıcı ve şifre istedikten
# sonra ka:admin ve şifre:1234 ise giriş başarılı değilse,
# hangi bilgi hatalıysa onun uyarısını veren bir uygulama yazınız.

# kullanici_adi=input("Lütfen kullanıcı adınızı giriniz:")
# sifre=int(input("Şifre giriniz:"))
# match kullanici_adi:
#     case "admin":
#          match sifre:
#             case 1234 :
#                 print("giriş başarılır.")
#
#             case _:
#                 print("şifre yanlıştır.")
#     case _:
#         print("kullanıcı adı yanlıştır.")

#18-)
# kullanici_secimi=input("Lütfen indirimden almak istediğiniz ürünü giriniz:")
# match kullanici_secimi:
#     case "ayakkabı":
#         print("NİKE")
#     case "kaban":
#         print("ZARA")
#     case "aksesuar":
#         print("Atasay jewellery")
#     case "sweatshirt":
#         print("BERSHKA")
#     case _:
#         print("aradığınız ürün için marka bulunamadı.")

#19-) # for örnekleri:
# 10-20 arasındaki sayıları geriden yazdırınız.20-19-18-...11

# for i in range(20,10,-1):
#     print(i)

#20-) 0-20 arasındaki tek sayıların toplamını döngü ile bulunuz.

# toplam=0
# for i in range(1,20,2):
#     toplam +=i
#
# print(toplam)

#21-) 1-100 arasındaki teklerin  ve çiftlerin ayrı ayrı toplamını aynı döngüde hesaplayınız.

cift_sayilar=0
tek_sayilar=0
# for i in range(1,101):
#     if i%2==0:
#         cift_sayilar +=1
#     else:
#         tek_sayilar +=1
# print(f"çift sayıların toplamı:{cift_sayilar},tek sayıların toplamı:{tek_sayilar}")

#22-) çarpım tablosunu döngü kurarak nasıl yaparız.
title_list=["1'ler","2'ler","3'ler","4'ler","5'ler","6'lar","7'ler","8'ler","9'lar","10'lar"]
# for i in range(1,11):
#     print(title_list[i-1])
#     print("------")
#     for j in range(1,11):
#         print(f"{i}x{j}={i*j}")
#     print("------")

#23-) while örneği:
# while ile 1'den 10' a kadar sayıları yazdırın.
# sayac=0
# while sayac<10:
#     sayac +=1
#     print(sayac)

#24-)
#Kullanıcı hayır yazana kadar merhaba dünya yazan uygulamayı yazınız.

# devam_etsin_mi="evet"
# while devam_etsin_mi=="evet":
#     print("merhaba dünya")
#     devam_etsin_mi=input("devam etmek istiyor musunuz? : evet/hayır:")

#25-) # kullanıcı hayır diyene kadar rastgele sayı üreterek (1-100) ekranda gösteren uygulamayı yazınız.

# import random as rnd
# while True:
#     print(f"Üretilen sayı:{rnd.randint(1,100)}")
#     girilen=input("çıkmak için hayır yazınız.")
#     if girilen=="hayır":
#         print("çıkış yapıldı")
#         break
#26-)
# kullanıcıdan bir sayı alınız,girilen değer 0-10 aralığında
# ise doğru giriş değilse doğru giriş yapana kadar karşı taraftan bilgi istemeye devam
# eden programı ekrana yazdırınız.

# while True:
#     kullanici_girisi = int(input("Lütfen bir sayı giriniz:"))
#     if 0<= kullanici_girisi <=10:
#         print("doğru giriş yapıldı.")
#         break
#     else:
#         print("tekrar deneyiniz.")

#27-) # rastgele 4 haneli bir doğrulama kodu belirleyiniz.
# ve ekranda bu değer gösteriniz.Kullanıcıdan bu kodu doğru bir şekilde girmesini isteyiniz
# ve doğru giriş yapılana kadar uyarı veriniz.
# 1000-999
# import random as rnd
# rastgele_kod=rnd.randint(1000,9999)
# print(rastgele_kod)
# giris_dogru_mu=False
# while not giris_dogru_mu:
#     girilen = int(input("4 haneli bir kod giriniz:"))
#     if girilen != rastgele_kod:
#         print("yanlış giriş yaptınız.,tekrar deneyiniz.")
#     else:
#         print("giriş  başarılı yapıldı")
#     break


#28-)
# rastgele 4 haneli bir doğrulama kodu belirleyiniz.
# ve ekranda bu değer gösteriniz.Kullanıcıdan bu kodu doğru bir şekilde girmesini isteyiniz
# ve doğru giriş yapılana kadar uyarı veriniz.
# 1000-999
# geliştirme: her yanlış girildiğinde yeniden kod üretilerek gösterilsin.
# import random as rnd
# sayi=rnd.randint(1000,9999)
# print(f"Üretilen sayı:{sayi}")
# kullanici_girisi=int(input("Lütfen 4 haneli bir kod giriniz:"))
# while kullanici_girisi!=sayi:
#     sayi = rnd.randint(1000, 9999)
#     print(f"Tekrar üretilen kod:{sayi}")
#     kullanici_girisi = int(input("Lütfen 4 haneli bir kod giriniz:"))
# print("giriş başarılı.")

#29-)# rastgele 4 haneli bir doğrulama kodu belirleyiniz.
# ve ekranda bu değer gösteriniz.Kullanıcıdan bu kodu doğru bir şekilde girmesini isteyiniz
# ve 3 kez yanlış giriş yapılırsa hakkınız tükendi uyarısını veriniz

# import random as rnd
# rastgele_kod=rnd.randint(1000,9999)
# print(f"Üretilen rastgele kod:{rastgele_kod}")
# sayac=0
# kod=int(input("Lütfen 4 haneli kod giriniz:"))
# while rastgele_kod != kod:
#     sayac +=1
#     if sayac==3:
#         print("3 giriş hakkınız bitmiştir.")
#         break
#     else:
#         kod = int(input("Lütfen 4 haneli kod giriniz:"))
#
# if rastgele_kod==kod:
#     print("giriş başarılıdır.")

#30-)# vize final notları girilirken 0-100 aralığında girilmesini isteyiniz.
# eğer vize doğru girildiyse final notunu isteyiniz.her bir notu girerken 0-100 aralığında
# alana kadar notları yeniden isteyiniz.
# her ikisi de doğru girildiyse ortalama hesaplayıp gösteiniz.

vize=int(input("Lütfen vize notunuzu giriniz:"))
final=int(input("Lütfen final notunuzu giriniz:"))
ortalama=vize*0.3+final*0.7
sayac=0
while vize<100:
    print("vie")














































































































