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

# cift_sayilar=0
# tek_sayilar=0
# for i in range(1,101):
#     if i%2==0:
#         cift_sayilar +=1
#     else:
#         tek_sayilar +=1
# print(f"çift sayıların toplamı:{cift_sayilar},tek sayıların toplamı:{tek_sayilar}")

#22-) çarpım tablosunu döngü kurarak nasıl yaparız.
#title_list=["1'ler","2'ler","3'ler","4'ler","5'ler","6'lar","7'ler","8'ler","9'lar","10'lar"]
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

# vize=-1 #random bir değer atıyoruz.
# while not 0<= vize <=100:
#     vize=float(input("lütfen vize notunuzu giriniz:"))
#
# final=-1
# while not 0<= final <=100:
#     final=float(input("Lütfen final notunuzu giriniz:"))
#
# average=vize*0.4+final*0.6  #ortalama değeri atanıyor.
# print(f"ortalama:{average}")

#31-)
# sayı tahmini uygulaması
# 1-10 arasında rastgele bir sayı üretilir ekranda gösterilmez.kullanıcıdan o sayıyı tahmin etmesi istenir
# .3 kez tahmin etme hakkı olur.Hakları bittiğinde game over!yanlış girdikçe yeni tahminler( kalan hakkı kadar) yapabilir.
# sayıyı bildiğinde ise tebrikler uyarası verilir.
#hocanın yaptığı:
# import random as rnd
# rastgele_uretilen_sayi=rnd.randint(1,10)
# print(rastgele_uretilen_sayi)
# for i in range (3):
#      kullanicinin_tahmini=int(input("Tahmini giriniz:"))
#      if kullanicinin_tahmini==rastgele_uretilen_sayi:
#         print("bildiniz")
#         break
#      else:
#         print("Yanlış tahmin ettiniz.")


#alternatif çözüm:
# import random as rnd
# rastgele_uretilen_sayi=rnd.randint(1,10)
# print(rastgele_uretilen_sayi)
# kalan_hak=3
# while kalan_hak >0 :
#     kalan_hak-=1
#     kullanicinin_tahmini=int(input("Tahmini giriniz:"))
#     if kullanicinin_tahmini==rastgele_uretilen_sayi:
#         print("bildiniz")
#         break
#     else:
#         print("Yanlış tahmin ettiniz.")
#     if kalan_hak==0:
#         print("game over")


#COLLECTİONS:
#1-) LİST
#2-)SET
#3-)TUPLE
#4-) DICTIONARY
#------------------------------------------------------------------------------
#1-)Örnek:1 den girilen sayıya kadar olan sayıları bir listeye ekleyen bir uygulama yazınız.
# kullanici_girisi=int(input("Lütfen bir sayı giriniz:"))
# sayi_listesi=list()
# for sayi in range(1,kullanici_girisi+1):
#     sayi_listesi.append(sayi)  #append:eklemek
# print(sayi_listesi)

# farklı yöntem:
# girilen_sayi=int(input("Sayı giriniz:"))
# liste=[]
# for i in range(1,girilen_sayi+1):
#     liste.insert(i-1,i)  #insert metodu:istediğimiz indekse ekleme yapabiliriz.
# print(liste)

#farklı yöntem:

# giris_sayi=int(input("sayı giriniz:"))
# liste=[]
# liste.extend(range(1,giris_sayi+1)) #extend:
# print(liste)


#2) Örnek:İnputtan 2 sayı alınız,ilk girilen sayı.
# küçük ise artan sırayla;büyük ise azalan sırayla bir liste oluşturunuz.

# sayi1=int(input("1.sayıyı giriniz:"))
# sayi2=int(input("2.sayıyı giriniz:"))
# artis_miktari=1
# if sayi1>sayi2:
#     artis_miktari-=1
#     liste = list()
# for i in range(sayi1,sayi2+artis_miktari,artis_miktari):
#     liste.append(i)
# print(liste)

#diğer bir yol:
# number1=int(input("1.sayıyı giriniz:"))  #1.sayı inputtan istendi.
# number2=int(input("2.sayıyı giriniz:"))  #2.sayı inputtan istendi.
# liste=[]     #liste tanımlandı.
# if number1<number2:    #1. sayısı 2. sayıdan küçük ise:
#     liste.extend(range(number1,number2 +1)) #listeye extend metodu ile ekle(önce 1.sayı sonra 1.sayı+1)
# else:                                       #ya da  2.sayı 1.sayıdan büyük ise:
#     liste.extend(range(number1,number2-1,-1))     #listeye extend metodu ile ekliyoruz.tersten sıralamak için -1 ile yapıyoruz.
# print(liste)                                      #print ile ekrana yazdırıyoruz.

#3-)Örnek: A'dan Z'ye kadar olan harfleri döngü ile listeye ekleyiniz.
#kucuk_harfler_listesi=[]
'''
for i in range(ord("a"),ord("z")+1):
    kucuk_harfler_listesi.append(chr(i))
print(kucuk_harfler_listesi)

buyuk_harfler_listesi=[]
for i in range(ord("A"),ord("Z")+1):
    buyuk_harfler_listesi.append(chr(i))
print(buyuk_harfler_listesi)

semboller_listesi=[]
for i in range(ord("!"),ord("?")+1):
    semboller_listesi.append(chr(i))
print(semboller_listesi)
'''

#4-)ÖRNEK:SAYILAR İSİMLİ BİR LİSTEYE 10 TANE RASTGELE
# SAYI ÜRETEREK EKLEYİNİZ.ÜRETİLECEK SAYILAR (1-100) ARASINDA OLSUN.
'''
import random as rnd    #random sayı üretilecek.
sayilar=[]              #sayi listesi atandı.
for i in range(1,11):     # 10 kere döngü olucak.
    uretilen_sayilar = rnd.randint(1, 100) #10 sayı 1-100 arasından seçiliyor.
    if sayilar.count(uretilen_sayilar)==0:     #aynı sayı listeye alınmıyor.
       sayilar.append(uretilen_sayilar)         #sayilar listesine ekleniyor.
print(sayilar)                               #yazdırılıyor.

'''

#diğer bir yöntem:
# while yöntemi:
'''
index=0      #döngünün durması için durdurma pointi.
sayilar=[]
while index <10:                # 10 kere dönücek
    uretilen_sayilar=rnd.randint(1,100)
    if sayilar.count(uretilen_sayilar)==0:
        sayilar.append(uretilen_sayilar)
        index+=1
print(sayilar)
'''

#5-)
# Müşteriden kaç kolon oynamak istediğini alalım.Sonrasında
# 1 kolan için 1-49(49) dahil rastgele 6 tane sayı üretilsin ve bir listeye eklesin  ve kçükten büyüğe doğru sıralansın.
# Her kolan için aynı işlemler yapılsın.

'''
import random as rnd  #rastgele sayı üretiliyor.
kolon=int(input("Kaç kolon oynamak istersiniz(4-6):"))  #dışarıdan bilgi alınıyor.
kolon_listesi=[]                                        #liste tanımlandı.
sayac=0                                                 #başlangıç değer tanımlandı.
while sayac<6:    #6 kere için döngü kuruldu.
    rastgele_sayi_üretilsin=rnd.randint(1,50)   #random sayı üretme
    if kolon_listesi.count(rastgele_sayi_üretilsin)==0:   #count ile aynı sayı çıkarma
        kolon_listesi.append(rastgele_sayi_üretilsin)     #append ile listeye ekleme.
        kolon_listesi.sort()                              #sort metodu ile sıralama.
    sayac+=1                                              #sayaç arttırılıyor.
print(kolon_listesi)                                      #print ile yazdırılıyor.

'''

#6-) password generator:
# password generator:
# kaç karakterli bir şifre istiyorsunuz ? 6
# büyük harf istiyor musunuz ? e  [A B C D E ...Z]
# küçük harf istiyor musunuz ? e  [a b c d ...z]
# rakam istiyor musunuz ? e [0 1,2....9]
# sembol istiyor musunuz ? h
# Ascii table
'''
sifre=int(input("kaç karakterli şifre istiyorsunuz:"))
buyuk_harf_olcak_mi=input("Buyuk harf ister misiniz: e/h")
kucuk_harf_olcak_mi=input("Kucuk harf ister misiniz : e/h")
rakam_olcak_mi=input("Rakam istiyor musunuz: e/h")
sembol_olcak_mi=input("Sembol istiyor musunuz: e/h")
buyuk_harfler=[]
kucuk_harfler=[]
rakam=list(range(0,10))
sembol=[]
for i in range(ord("A"),ord("Z")+1):
    buyuk_harfler.append(chr(i))
for i in range(ord("a"),ord("z")+1):
    kucuk_harfler.append(chr(i))
for i in range(ord("!"),ord("?")+1):
    sembol.append(chr(i))

import random as rnd
pasword=[]
while len(pasword)<sifre:
    uretilen=rnd.randint(0,3)
    match uretilen:
        case 0 :
            if buyuk_harf_olcak_mi=="e":
                pasword+= buyuk_harfler[rnd.randint(0,len(buyuk_harfler)-1)]
        case 1:
            if kucuk_harf_olcak_mi=="e":
                pasword+= kucuk_harfler[rnd.randint(0,len(kucuk_harfler)-1)]
        case 2:
            if rakam_olcak_mi=="e":
                pasword+=str(rakam[(rnd.randint(0,len(rakam)-1))])
        case 3:
            if sembol_olcak_mi=="e":
                pasword+= sembol[rnd.randint(0,len(sembol)-1)]
#print(pasword)
'''

#Diğer örnekler:
#mail ayrımı:
# mail_listesi=["nur.ozturk@bilgeadam.com","sema.yılmaz@bilgeadam.com"]
# print("/".join(mail_listesi)) #nur.ozturk@bilgeadam.com/sema.yılmaz@bilgeadam.com
#
# #matematik kütüphanesi için kullanılan:
# #import math
# import math as p1
# pi_sayisi=p1.pi
# print(f"Pi sayısı={pi_sayisi}") #Pi sayısı=3.141592653589793
# e_sayisi=p1.e
# print(f"E sayısı={e_sayisi}")  #E sayısı=2.718281828459045
# #1-) floor(): bir alt tam sayıya tamamlamak.
# print(p1.floor(pi_sayisi)) #3
# print(p1.floor(e_sayisi))  #2
# #2-) ceil():bir üst tamsayıya tamamlamak.
# print(p1.ceil(pi_sayisi)) #4
# print(p1.ceil(e_sayisi))  #3
# #3-) fabs(): mutlak değer alır.
# sayi1=-100
# print(p1.fabs(sayi1)) #100
# #4-) sqrt():karekök alma
# sayi2=81
# print(p1.sqrt(sayi2))  #9.0
# #5-) pow(): üs alma
# a=5
# b=3
# print(p1.pow(a,b)) #125.0
# #fsum():
# rakamlar=[0,1,2,3,4,5,6,7,8,9]
# print(p1.fsum(rakamlar))  #45.0
#
# #DATETİME METOTLARI
# #import datetime as dt
#
# #şimdiki zamanı nasıl hesaplayabiliriz?
# # import datetime as dt                #eğer böyle yazarsak dt.datetime diye çağırmamız gerekir.
# # simdiki_zaman=dt.datetime.now()
# # print(simdiki_zaman)    #2022-11-29 20:29:52.890975
#
# #bugünün zamanını nasıl hesaplarız?
# # from datetime import datetime as dt   #eğer from datetime diye yazarsak datetime'ı çağırmamıza gerek yoktur.
# # bugünün_tarihi=dt.today()
# # print(bugünün_tarihi)   #2022-11-29 20:31:14.958684
# # print(dt.date())        #2022-11-29 20:34:05.733673
#
# #TARİH NASIL OLUŞTURULUR ?
# import datetime as dtm
# bugünün_zamani=dtm.date.today()
# dogum_tarihi=dtm.date(1990,10,10)
# fark=bugünün_zamani-dogum_tarihi
# print(fark)  #11738 days, 0:00:00
# tam_yasi=fark.days/365
# print(round(tam_yasi)) #32  #round yuvarlıyor.

#bizim zaman dilimimiz yani tarih olarak-GÜN-AY-YIL----11-04-1997
#diğer ülkelerdeki zaman diliminde ise -AY-GÜN-YIL-----04-11-1997
'''
%Y:year
%d:day
%m:month
%H:hour
%M:minute
%S:second
'''
#  STRFTİME: f format (time string olarak formatlıyor) tarihten stringe
#yani srtftime aslında hesapladığımız şu anki güncel zamanı bize tgün tarih ve yıl cinsinden verir.
# import datetime as dt
# guncel_zaman=dt.datetime.now()
# print(guncel_zaman)  #2022-11-29 23:01:52.350312
# print(guncel_zaman.strftime("%m-%d-%Y")) #11-29-2022
# print(guncel_zaman.strftime("%d-%m-%Y")) #29-11-2022
#
# #STRPTİME: p parse,stringden tarih cinsine
# #strptime da verilen tarihi stringe çeviriyor.
# import datetime as dt
# tarih=dt.datetime.strptime("04.11.1997","%m.%d.%Y")
# print(tarih)  #1997-04-11 00:00:00
# print(tarih.timestamp())  #saniye cinsinden --860706000.0

#custom metotlar:
'''
-Custom metotların kullanılmasının sebebi aslında daha complex kodlar için fonskiyon tanımı içinde daha anlaşılır;
yazabilmek ve sonrada değiştirmek daha kolay olduğu için kullanılabilir.
-metot tanımlanması-----> def ile yapılır.
def def_adi():-----> paramaetre/parametresiz-Metot tanımlanması-
    islemler
def_adi()    ------> fonskiyon çağrılır.
# Metotlar çağırılarak çalıştırılırlar.
# Sıralama önemlidir
# Önce metot tanımlanacak !
# Parametreli veya parametresiz metotlar tanımlanabilir.
# Eğer parametre alıyorsa veri tipinin tanımlaması zorunlu değildir.

KULLANIM ŞEKLİ;
# metot adı: snake_case notasyonu ile tanımlanır.
def metot_adi():
    metodun yapacağı işlemler

-metot=fonksiyon
-fonksiyon kendi başına tanımlanan bir yapıdır.
-metot da bir fonksiyondur.
-Bir classın içinde tanımlanıyorsa metot oluyor.
-ikiside aynı şeyi yapıyor.

-ÖNCE ÇAĞIR SONRA TANIMLA
# NOT: ÇOĞU ZAMAN EMİR KİPLERİ ŞEKLİNDE KULLANILIR.
# bir kez tanım yapıyoruz çoğu kez kullanıyoruz.
# metot overload yoktur.overload:aynı metot adı ile parametreleri değişicek şekilde birden fazla metot yazılmasıdır.
# aşırı yükleme yapılmıyor.
-------------------------------------------------------------------------------------------------
                             CUSTOM METOTLAR 2'YE AYRILIR.
    1-)GERİ DEĞER DÖNMEYEN               2-)GERİ DEĞER DÖNEN
    1.A) PARAMETRESİZ                    2.A) PARAMETRESİZ
    1.B) PARAMETRELİ                     2.B) PARAMETRELİ   
---------------------------------------------------------------------------------------------------
'''
# 1-) GERİ DEĞER DÖNMEYEN
# 1.A) PARAMETRESİZ
# def selamla():      #fonskiyon tanımlandı
#     print("Hello World!")     #mesaj verildi.
# selamla()                     # ve fonskiyon çağrıldı.Hello World!

#1.B) PARAMETRELİ
#metot içine yazılan değerlere parametre konuluyor: bu integeer,string,datetime vb. olabilir.

# def selam_ver(mesaj:str):
#     print(mesaj)
# selam_ver("selam güzelim :) ")
# def toplam(a:int,b:int):
#     print(f"a+b={a+b}")
# toplam(3,4)  #a+b=7
#
# def ortalama_al(vize:int,final:int):
#     ortalama=(vize*0.4)+(final*0.6)
#     print(f"ortalama:{ortalama}")
# ortalama_al(40,60)  #ortalama:52.0
#
# def fark_al(a:int,b:int):
#     fark=a-b
#     print(f"a-b={fark}")
# fark_al(9,2)  #a-b=7

#2-) GERİ DEĞER DÖNEN METOTLAR
#2.A-) PARAMETRESİZ
# def topla1():
#     toplam=4+5
#     return toplam
# print(topla1())   #9
#
# def us_alma():
#     us=2*2
#     return us
# print(us_alma())  #4
#
# def us_alma1():
#     us1=pow(3,3)
#     return us1
# t=us_alma1()
# print(t)  #27

#2.B-) PARAMETRELİ
# import math as q
# def summary(a:int,b:int,c:int):
#     toplam=a+b+c
#     return toplam
# print(summary(7,3,4))   #14

#NOT:CUSTOM METOTLAR :SİSTEMDE OLMAYAN KODLARI DAHA MODÜLER KULLANABİLMEK İÇİN YAZIYORUZ
#ÖRNEK:
# float parametre alarak bu sayıların farkını alan ve,
# gösteren bir metot tanımlayınız.(geri değer dönmeyen)
# def fark_al(a:float,b:float):
#     fark=a-b
#     print(f"a-b={fark}")
# fark_al(2022,1997) #a-b=25
# a=float(input("bir sayı giriniz:"))
# b=float(input("ikinci bir sayı giriniz:"))
# fark_al(a,b)    #bir sayı giriniz:24
#                 #ikinci bir sayı giriniz:3
#                 #a-b=21.0

#programlama dilidinde uyulması gereken 5 psensip vardır.
#    SOLID: S,O,L,I,D 5 TANE PRENSİP VARDIR.
#S: SINGLE RESPONSIBILITY: tek sorumluluk prensibidir.yazılan bir kodun(class,method)tek bir amaca hizmet etmesidir

# örnek:
# def dort_islem_yap(a:int,b:int):
#     toplam=a+b
#     fark=a-b
#     bolum=a/b
#     carpım=a*b
#     sonuc={
#         "toplam":toplam,
#         "fark":fark,
#         "bolum":bolum,
#         "carpim":carpım
#     }
#     return sonuc
# print(dort_islem_yap(10,2))

#aslında yapılması gereken 4 işlem dışında tek tek işlem fonskiyonları oluşturmaktır:

# def topla(a:int,b:int):
#     toplam=a+b
#     return toplam
# print(topla(3,4))

# def fark_al(a:int,b:int):
#     fark=a-b
#     return fark
# print(fark_al(9,2))
# def bol(a:int,b:int):
#     bolme=a/b
#     if b==0:
#         print("lütfen b değerini değiştiriniz")
#     return bolme
# print(bol(10,5))
#
# def carp(a:int,b:int):
#     carpma=a*b
#     return carpma
# print(carp(2,3))

#bölme fonskiyonu için 0'a bölme konusunda ,exception fırlatılması gerekiyor,çünkü ikinci sayının 0 olması hata verir.
# def division(a:int,b:int):
#     try:
#         div=a/b
#         return div
#     except:
#         raise Exception("B SAYISI 0 OLAMAZ !")
#
# # sayı1=division(9,0) #Exception: B SAYISI 0 OLAMAZ !
# # print(sayı1)
# sayı2=division(30,10)
# print(sayı2) #3.0

# ÖRNEK:
## # 1-) 1'den dışarıdan parametre olarak alınan bir sayıya kadar olan çift sayıları ekrana gösteren bir metot yazınız.
# # 2-)update:Listeye atan ve o listeyi dönen metot yazınız.
# parametre alıyor ve geri değer döndürmüyor.
# def ciftleri_yazdir(bitis:int)->list:
#     liste=[]
#     for i in range(1,bitis+1):
#         if i%2==0:
#             liste.append(i)
#             return liste
# ciftler=ciftleri_yazdir(6)
# print(ciftler)

#ÖRNEK:
# # parametre olarak ad,soyad,uzanti alarak ad.soyad@uzanti şeklinde
# # mail oluşturan ve dönen bir metot tanımlayınız.
# # (türkçe karakterleri dönüştürünüz tümü küçük harf olmalı)

# def turkce_karakterleri_cevir(metin:str):
#     '''türkçe karakter:ı,ö,ü,ş,ç,ğ'''
#     metin=metin.replace("ı","i").replace("ö","o").replace("ü","u").replace("ş","s").replace("ç","c").replace("ğ","g")
#     return metin
# def mail_olusturma(ad:str,soyad:str,uzanti:str):
#     ad=turkce_karakterleri_cevir(ad)
#     soyad=turkce_karakterleri_cevir(soyad)
#     mail=turkce_karakterleri_cevir((f"{ad}.{soyad}@{uzanti}".lower().replace('',"")))
#     return mail
# mail1=mail_olusturma("goncagül","çomak","bilgeadam.com")
# print(mail1) #goncagul.comak@bilgeadam.com

#ÖRNEK:# Türkçe karakterleri eng.karaktere çeviren bir metot tanımlayabilirsiniz
# ve mail oluşturucunun içinde kullanabilrsiniz.
personel_listesi=[
    {
        "ad":"gonca",
        "soyad":"çomak"
    },
    {
        "ad":"gökhan",
        "soyad":"çomak"
    },
    {
        "ad":"emircan",
        "soyad":"kor"
    }
]
# # bilgeadam.com -> yukarıdaki listede yer alan tüm personellere mail oluşturucu metot yardımı ile
# # mailler oluşturunuz ve listeye ekleyiniz.
# def turkce_karakterleri_cevir(metin:str):
#     '''türkçe karakter:ı,ö,ü,ş,ç,ğ'''
#     metin=metin.replace("ı","i").replace("ö","o").replace("ü","u").replace("ş","s").replace("ç","c").replace("ğ","g")
#     return metin
# def mail_olusturma(ad:str,soyad:str,uzanti:str):
#     ad=turkce_karakterleri_cevir(ad)
#     soyad=turkce_karakterleri_cevir(soyad)
#     mail=turkce_karakterleri_cevir((f"{ad}.{soyad}@{uzanti}".lower().replace('',"")))
#     return mail
#
# mail_listesi=[]
# for personel in personel_listesi:
#     personel_adi=personel["ad"]
#     personel_soyadi=personel["soyad"]
#     mail=mail_olusturma(personel_adi,personel_soyadi,"bilgeadam.com")
#     mail_listesi.append(mail)
#
# print(mail_listesi)

#UPDATE:
# dışarıdan parametre olarak bir dict. listesi alan ve tüm listedeki
# çalışanlar için mail oluşturup liste olarak dönen method yazınız.
# sürekli liste geldiğini düşünerek methoda çevirmek.

# def mail_olustur1(personel_listesi:list):
#     mailler=[]
#     for personel in personel_listesi:
#         mailler.append(mail_olusturma(personel["ad"],personel["soyad"],"bilgeadam.com"))
#         return mailler
# print(mail_olustur1(personel_listesi))


#ÖRNEK:
# ['nur.ozturk@bilgeadam.com', 'damla.kahraman@bilgeadam.com', 'mert.boylu@bilgeadam.com', 'neslihan.kaptanyorubulut@bilgeadam.com']
# bu formatta gelen mail listesinin ad ve soyadı ayrıştırıp personel listesi şeklinde dönen bir metot yazınız.
# p_list=[{"ad":"nur","soyad":"öztürk"}]
# split kullanıcaz.
# def mail_ayristirma(mailler:list)->list:
#     personeller=[]
#     for mail in mailler:
#         ilk_eleman=str(mail).split("@")[0]
#         ayrismis_elemanlar=ilk_eleman.split(".")
#         personel={
#             "ad":ayrismis_elemanlar[0],
#             "soyad":ayrismis_elemanlar[1]
#         }
#         personeller.append(personel)
#         return personeller
#
# mailler=['nur.ozturk@bilgeadam.com', 'damla.kahraman@bilgeadam.com', 'mert.boylu@bilgeadam.com', 'neslihan.kaptanyorubulut@bilgeadam.com']
# print(mail_ayristirma(mailler))



#Örnek:
#Bir metot istiyoruz; parametre olarak bir metin(str) alan ve bu metin içindeki sesli ve sessiz harfleri ayırarak hem sayısını hem harfleri gösteren bir metor yazınız.
# merhaba dünya ! ->sesliler:e,a,a  sessizler :m,r,b
# a,e,ı,i,o,ö,u,ü
#kaç tane a vardr gibi bir şey de olucak,
# {
#     sesliler:....,
#     sessizler:...,
#     seslilerin_sayisi:x
#     sessizlerin_sayisi:y
# }

# def sesli_sessiz_harf_varmi(metin:str):
#     sesli_harfler=["a","e","ı","i","o","ö","u","ü"]
#     metindeki_sesli_harfler=set()
#     metindeki_sessiz_harfler=set()
#     sesli_sayisi=0
#     sessiz_sayisi=0
#     for harf in metin:
#         if harf.isalpha():
#             if sesli_harfler.count(harf) >0:
#                 metindeki_sesli_harfler.add(harf)
#                 sesli_sayisi+=1
#             else:
#                 metindeki_sessiz_harfler.add(harf)
#                 sessiz_sayisi+=1
#     return{
#             "sesliler":metindeki_sesli_harfler,
#             "sessizler":metindeki_sessiz_harfler,
#             "seslilerin sayisi":sesli_sayisi,
#             "sessizlerin sayisi":sessiz_sayisi
#         }



#mesaj=sesli_sessiz_harf_varmi("2023 senesinin ilk ayları yazılım alanı için kariyerimin başladğı ilk sene olucak !")
#print(mesaj) #{'sesliler': {'i', 'ı', 'e', 'o', 'u', 'a'}, 'sessizler': {'r', 'b', 'n', 'd', 'k', 'm', 'y', 'ğ', 's', 'c', 'ç', 'l', 'z', 'ş'}, 'seslilerin sayisi': 30, 'sessizlerin sayisi': 36}
# girilen=input("Bir metin giriniz:")
# print(sesli_sessiz_harf_varmi(girilen))
#
# #update :
# def metin_incele(metin:str)->dict:
#     sesli_harfler=["a","e","ı","i","o","ö","u","ü"]
#     metindeki_sesli_harfler=dict()
#     metindeki_sessiz_harfler=dict()
#     sesli_harf_sayac=0
#     sessiz_harf_sayac=0
#     for harf in metin:
#         if harf.isalpha():
#             if sesli_harfler.count(harf) > 0:
#                 metindeki_sesli_harfler.get(harf)
#                 sesli_harf_sayac+=1
#             else:
#                 metindeki_sessiz_harfler.get(harf)
#                 sessiz_harf_sayac+=1
#     return {
#         "sesli harfler":metindeki_sesli_harfler,
#         "sessiz harfler":metindeki_sessiz_harfler,
#         "sesli harf sayısı":sesli_harf_sayac,
#         "sessiz harf sayısı":sessiz_harf_sayac
#     }
#
# mesaj=metin_incele("ben nerdeyim ?")
# print(mesaj)


#ÖRNEK:
#parametre olarak '1980-10-12' gibi bir doğum tarihi olarak yaş hesaplayan ve bu değeri geri dönen bir metot yazınız:
#hataya düşmemek için: #def yas_hesapla(yil:int,ay:int,gun:int)-->int:

#fonskiyonu oluştururken içine parametre alan ve geri değer döndüren bir metot yazılcak.

def dogum_tarihi_hesapla(dogum_tarihi:str)->int:
    from datetime import datetime as dt
    simdiki_zaman=dt.now()
    dogum_tarihi=dt.strptime(dogum_tarihi,"%Y-%M-%d")
    yas=simdiki_zaman-dogum_tarihi
    return round(yas.days/365)

# benim_yasim=dogum_tarihi_hesapla("1997-04-11")
# print(benim_yasim) #26
# annemin_yasi=dogum_tarihi_hesapla("1974-05-18")
# print(annemin_yasi) #49
# babamin_yasi=dogum_tarihi_hesapla("1969-03-10")
# print(babamin_yasi) #54


#EMEKLİLİK YAŞ HESAPLAMA ÖRNEĞİ:
#emekliliğe kaç yıl kaldığını hesaplamaya kaç yıl kaldığını hesaplayan bir metot yazınız:
#kadın :58 erkek:65
#"sevgili Nur,2022 tarihi itibariyle emekliliğine 40 yıl kalmıştır."

def yas_hesapla(dogum_tarihi:str)->int:
    from datetime import datetime as dt   #datetime kütüphanesi yazıldı.
    simdiki_zaman=dt.now()                #şimdiki zamanı hesapladık.
    dogum_tarihi=dt.strptime(dogum_tarihi,"%Y-%M-%d")
    yas=simdiki_zaman-dogum_tarihi
    return round(yas.days/365)
def emeklilik_yasi(ad:str,soyad:str,cinsiyet:str,dogum_tarihi:str)->int:
    from datetime import datetime as dt
    emeklilik_yasi=65
    if cinsiyet=="k":
        emeklilik_yasi=58
    kisinin_yasi=yas_hesapla(dogum_tarihi)
    emeklilige_kalan_yil=emeklilik_yasi-kisinin_yasi
    sonuc=f"AD:{ad.capitalize()}\nSOYAD:{soyad.capitalize()}\nCİNSİYET:{cinsiyet.capitalize()}\nEmekliliğe Kalan Yıl:{emeklilige_kalan_yil}"
    return sonuc

me=emeklilik_yasi("gonca","çomak","k","1997-04-11")
print("---- KİŞİSEL BİLGİLER----")
print(me)  #---- KİŞİSEL BİLGİLER----
           #AD:Gonca
           #SOYAD:Çomak
           #CİNSİYET:K
           #Emekliliğe Kalan Yıl:32


#dairenin yarıçapını hesapla:
#örnek:
# def dairenin_alani_hesaplama(yaricap:float,pi_sayisi:float=None):
#     import math as m
#     if pi_sayisi is None:
#         pi_sayisi=m.pi
#     alan=pi_sayisi*m.pow(yaricap,2)
#     return alan
# daire_alan=dairenin_alani_hesaplama(10,3)
# print(daire_alan) #300.0

#ya da
# import math as a
# def daire_alani(yaricap:float,pi_sayisi=a.pi):
#     '''#daire alanı:pi.yarıçapın karesi--> 3*yarçap**2'''
#     d_alani=pi_sayisi*a.pow(yaricap,2)
#     return d_alani
# daire_alani1=daire_alani(10,3)
# print(daire_alani1)  #300.0

#note:
#normalde pythonda overlood yoktur.parametre tanımlarken fonskiyon içinde yapılabiliyor.
# def toplama_yap(sayi1:int,sayi2=12,sayi3=30):
#     topla=sayi1+sayi2+sayi3
#     return topla
# print(toplama_yap(15)) #57
# print(toplama_yap(10,sayi2=5,sayi3=4)) #19

#note2:
'''kaç tane parametre tanımlamayı bilmiyorsak *args olarak parametre girebiliriz.'''
def topla(*sayilar):
    toplam=0
    for i in sayilar:
        toplam += i
    return (toplam)

print(topla(1,23,4,)) #28



#PYTHONDA MODÜL :
# .py adında bir dosya açtığımızda içine tanımlanan fonskiyonu başka bir python file dosyasında import ederek çağırabilir ve çalıştırlabilir.
#örneğin destek.py adında bir dosya oluşturup içine :
'''
def yaz(para):
    print("Merhaba",para)
    return  
# gibi bir fonksiyonu dosyaya yazıp daha sonra:
# python klasörinde :
import destek 
destek.yaz("Python ! ")
#gibi bir örnek yazdığımızda ----> Merhaba Python ! kodunu yazdırmış oluruz.
'''

# from...import ifadesi:
# from..import yapısı sayesinde modülün sadece bir kısmını kullanabiliriz.
# örneğin: from fib import fibonacci

# SCOPE (KAPSAM)
'''FONSKİYONLAR tanımlandığında kendi içlerinde yeni bir tanımlama
alanı(scope) oluşturular dolayısıyla fonskiyon içinde ya da dışında tanımlanan
değişkenlerin nasıl ele alındığını öğrenmemiz gerekir.'''
#LOCAL VE GLOBAL SCOPE
'''Her fonskiyon tanımlandığında kendi tanımlama alanı oluşturular ve kendi içlerinde tanımlanan değişkenler
local yani yerel değişken olarak adlandırılır.'''
#global scope
x='global x'
def function():
    #local scope
    x='local x'
    print(x)
function() # local x
print(x)   # global x

'''Aynı isimde tanımlanan x değişkeni hem global hem de local olarak tanımlanmıştır. 
Dolayısıyla fonksiyon içerisinde x değişkenine yapılan atama global alanda tanımlanan değişkeni etkilemez 
çünkü fonksiyon kapsamında yeni bir scope tanımlanır.'''

#Peki fonksiyon kapsamın x değişkenini tanımlamazsak ne olur ?

#global scope
# y='global y'
# def function():
#     #local scope
#     print(y)
#
# function()  # global y
# print(y)    # global y



#local
name="gonca"
def changeName(new_name):
    #local
    name=new_name
    print(name)
changeName("zeynep")  # zeynep
print(name)           # gonca

'''changeName() fonksiyonuna gönderdiğimiz değer fonksiyon kapsamındaki name değişkenine atanacağından dolayı 
değişiklik global değil yerel name değişkeninde yapılmış olur. Dolayısıyla ekrana zeynep ve gonca bilgisi yazılır.'''

#   NESNED FUNCTİONS SCOPES:
# iç içe tanımlanan fonskiyonlar için nasıl olur ?
#örnek1:
# global scope
name="GONCA"
def selamla():
    #local scope
    name="GÜL"
    def selamla1():
        #local scope
        name="BEYZA"
        print("MERHABA",name)

    selamla1()

selamla()  #MERHABA BEYZA

# örnek2:
#global scope
nick_name="GONCİİ"
def slm():
    def slm1():
        # local scope
        name="AŞKO"
        print("Hello",name)
    slm1()
slm()  #Hello AŞKO

#örnek3 :
# global scope
name="global scope"
def selam():
    def selam1():
        print("SELAM",name)
    selam1()
selam()     #SELAM global scope



# # DOSYA İŞLEMLERİ
# dosya=open("bilgiler.txt","r",encoding="utf8")  #dosya seçildi.
# oku=dosya.read() #seçilen dosya ekrana okundu.
# print(oku)
# #It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,
# #as opposed to using 'Content here, content here', making it look like readable English.
# oku1=dosya.read(10)
# print(oku1)  #It is a lo

# dosya=open("bilgiler.txt","r",encoding="utf8")
# print(dosya.readline()) #It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.
#
# print(dosya.readline()) #The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,
#
# print(dosya.readline()) #as opposed to using 'Content here, content here', making it look like readable English.
#
# dosya=open("bilgiler.txt","r")
# for satir in dosya:
#     print(satir)   #bu şekilde dosyayı satır satır yazabiliriz.

# with open("bilgiler.txt","r") as dosya:
#     for satir in dosya:
#         print(satir)
#It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.

#The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,

#as opposed to using 'Content here, content here', making it look like readable English.


#readlines():
# dosyanın tüm satırlarını bir diziye ekler.
#böylece her satır dizinin bir elemanı olur.
# dosya=open("bilgiler.txt","r",encoding="utf8")
# dizi=dosya.readlines()
# print(dizi)
# #['It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.\n', 'The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,\n', "as opposed to using 'Content here, content here', making it look like readable English.\n"]


#dosyayı yazma işlemleri:
#------"w" modunda yazılır.
#dosyanın içinde bir şey var ise siler yenisini oluşturur.
dosya=open("bilgiler.txt","w",encoding="utf8")
dosya.write("write modunda bilgiler.txt dosyasının içeriğine yeni metin yazılır.\n")
dosya.write("bigiler.txt içeriğindeki metin dosyası değişti.\n")
dosya.write("txt dosyasında daha önce yazılan şeyler tek satırda yazıldı.\n")
# write modunda bilgiler.txt dosyasının içeriğine yeni metin yazılır.
# bigiler.txt içeriğindeki metin dosyası değişti.
# txt dosyasında daha önce yazılan şeyler tek satırda yazıldı.

#-----"a" modunda yazmak:
dosya=open("bigiler.txt","a",encoding="utf8")
print(dosya.write("a modunda yazdığımızda içerik silinmez ekleme yapılır."))
print(dosya.write("ekleme yapıldu."))  #ekleme yapmadı.

# dosyayı kapatmak için close() kullanılır.
dosya=open("bilgiler.txt","a",encoding="utf8")
dosya.close()

#-------ya da :
with open("bilgiler.txt","a",encoding="utf8") as dosya:
    dosya.close()
# bu yöntemde kapatma olarak kullanılabilir.


# örnek:
#öğrencinin adını,soyadını,dt ve cinsiyetini alarak dict.olarak hazırlayan
#ve geri dönen bir metot yazınız ve bu metottan yararlanarak 3 kişi
#oluşturarak listeye ekleyiniz.Oluşturulan listeyi ogrenciler.txt dosyası içine yazdırıınız.


def ogrenci_bilgileri(ad:int,soyad:int,dt:int,cinsiyet:int)->dict:
    return {
        "ad":ad,
        "soyad":soyad,
        "dogum_tarihi":dt,
        "cinsiyet":cinsiyet

    }
ogrenci_listesi=[]
ogrenci_listesi.append(ogrenci_bilgileri("gonca","çomak","1997","k"))
ogrenci_listesi.append(ogrenci_bilgileri("gokhan","çomak","1999","e"))
ogrenci_listesi.append(ogrenci_bilgileri("zeynep","öztürk","1996","k"))
import pprint
print(pprint.pformat(ogrenci_listesi))
dosya=open("ogrenciler.txt","w",encoding="utf8")
dosya.write(pprint.pformat(ogrenci_listesi))


# HTTP İSTEKLERİ:
'''
http: client----> internet <-----server 
http : hyper text transform protocol en .ok kullanılan protokoldür.
https: s ile kullanıcı bilgileri,şahıs bilgileri şifrelenir ve riske dönüşmez kilit şekilde sembol olması https olduğunu gösterir.
response code:
1xx:information
2xx:başarılı durumlar
3xx:yönlendirme durumları
4xx: client hatası.
5xx: server hatası ve ya developer .500:sunucu hatası.

200: istek başarılı.
301: yönlendirme yapılıyor.
400: istek hatalı
404:izin olmadığını gösterir.
'''
# requests modülünü kullanıyoruz.
# bu paketin içerisinde 4 tane istek atmamıza yardım edecek methodlar vardır.
# get,post,put,delete,patch gibi mothodlar ile adrese istekler atılabilir.
# istekleri json ile gönderiyoruz.
'''
get : get methodu ile istek atıp veri alabiliriz.
post : post methodu ile de istek atıp veri almış oluruz.yalnız yanında veri göndermemiz gerekiyor ki create edilebilsin.
put/ patch: örneğin soyadımı olarak tanımlanan değri değiştirmek için kullanabiliriz.
patch daha kapsamlı veri gönderir.
put daha sıklıkla kullanılır.
delete: delete methodu ile veri siler.
import request kullanılır.
'''

# örnek:
# import requests as req
# # get methodu ile istek atıyoruz
# '''tanımlanan sonuc değişkeni sayesinde bana bir sonuç dönücek.'''
# sonuc=req.get("https://reqres.in/api/users")
# print(sonuc.status_code)  # 200 döndü : yani istek başarılı.
# print(sonuc.json())       # json methodu ile json formatına çeviriyoruz.
#                           #{'page': 1, 'per_page': 6, 'total': 12, 'total_pages': 2, 'data': [{'id': 1, 'email': 'george.bluth@reqres.in', 'first_name': 'George', 'last_name': 'Bluth', 'avatar': 'https://reqres.in/img/faces/1-image.jpg'}, {'id': 2, 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver', 'avatar': 'https://reqres.in/img/faces/2-image.jpg'}, {'id': 3, 'email': 'emma.wong@reqres.in', 'first_name': 'Emma', 'last_name': 'Wong', 'avatar': 'https://reqres.in/img/faces/3-image.jpg'}, {'id': 4, 'email': 'eve.holt@reqres.in', 'first_name': 'Eve', 'last_name': 'Holt', 'avatar': 'https://reqres.in/img/faces/4-image.jpg'}, {'id': 5, 'email': 'charles.morris@reqres.in', 'first_name': 'Charles', 'last_name': 'Morris', 'avatar': 'https://reqres.in/img/faces/5-image.jpg'}, {'id': 6, 'email': 'tracey.ramos@reqres.in', 'first_name': 'Tracey', 'last_name': 'Ramos', 'avatar': 'https://reqres.in/img/faces/6-image.jpg'}], 'support': {'url': 'https://reqres.in/#support-heading', 'text': 'To keep ReqRes free, contributions towards server costs are appreciated!'}}
#
# # post methodu ile:
# sonuc1=req.post("https://reqres.in/api/users",data={"page":"10","name":"gonca","job":"teacher"})
# if sonuc1.status_code==201:
#     print(sonuc1.json())
# else:
#     print("istek başarısız oldu")


# örnek:
#import requests
# r = requests.get('https://api.genelpara.com/embed/doviz.json')
# print(" \n Status code for  specific search: ",r.status_code,"\n") #Status code for  specific search:  200

# istek gönderirken python üzerinden geldiğimizi değilde,tarayıcı gibi
#gözükmek istiyorsan,request ile "header"bilgilerimizi gönderebiliriz.
# r=requests.get('https://api.genelpara.com/embed/doviz.json',headers={'user-agent':'asimmisirliFirefox'})
# print(r.status_code) #200
#
# #bu istekleri post ve put metotları ile de atabiliriz.
# response=requests.post("https://api.genelpara.com/embed/doviz.json",headers={"user-agent":"asimmisirliFirefox"})
# print(response.status_code) #200


# # ÖRNEK: döviz kurlarını çekelim:
# import requests
# r = requests.post('https://api.genelpara.com/embed/doviz.json',headers={'user-agent': 'asimmisirliFirefox'}) #headers yani asim misır ...dan geliyor demek.
# print(" \n Status code: ",r.status_code,"\n")
# if r.status_code == 200:
#     #json verilerini alıyoruz.
#     data2 = r.json()
#     for i in data2:
#         print("1 Türk lirası Satis/Alış ", i, ":", data2[i]["satis"], data2[i]["alis"], data2[i]["degisim"])
#         print("-------------------------------------------------------")
#
#
# else:
#     print ("Something wrong went")


### ----> OOP:OBJECT ORIENTED PROGRAMMING <-------
'''
Yazılımcının kendi nesnelerini(object),bu nesnelerinin özelliklerini ve davranışlarını
tanımlamısına imkan veren programlama yaklaşımıdır.
-Birçok yüksek seviyeli programlama dili oop'dir.c#,java,python
-Nesne üretmeye yarayan şablonlara sınıf(class)denir.
-Sınıflardan üretilen kopyalara(instance) nesne(object) denir.
-OOP TEMELLERİ
-UYULMASI GEREKEN KURALLAR VE TEMELLER:
-Encapsulation(veri gizleme,kapsülleme):sınıfın içindeki bilgileri korumak ve kontrollü şekilde korumaya sağlamaktır.
-Inheritance(kalıtım):ortak özelliklere sahip sınıflar oluşurulduğunda biz buna kalıtımdan yararlanarak yapılır.cinsiyet,yaş,ad,soyad gibi ortak insanda olan verileri kopyala yapıştırmak gibi uzun kodla yazmaktansa kalıtım adı altında birleştirilir.
-Polymorphism(çok biçimlilik):Aynı davranışın farklı sınıflarda çalışması.Kalıtımdan yaralanılmak zorundadır.

'''

# PYTHON CLASS(SINIF)
# class oluşturup içerisinde özellik(attributes) ve davranışlar(behavior) ekyerek bir sınıf oluştururuz.
# nesne(object) üretmek için oluşturulan şablondur.
'''
kullanım şekli:
class SinifinAdi:          # sınıf oluşturduk.
     sınıfın özellikleri
     sınıfın davranışları

SinifinAdi()               # bu şekilde de nesne üretmiş oluyoruz.
'''
# örnek:
class Araba():
    marka=""
    renk=""

araba1=Araba()  # araba1 Araba() classında oluşmuş bir nesnedir.
araba1.marka="audi"
araba1.renk="beyaz"

araba2=Araba()  # araba2 Araba() classından oluşmuş bir nesnedir.
araba2.marka="ford"
araba2.renk="siyah"
print("-----ARABA 1-----")
print(f"Arabanın Markası:{araba1.marka}\nArabanın Rengi:{araba1.renk}")
print("-----ARABA 2-----")
print(f"Arabanın Markası:{araba2.marka}\nArabanın Rengi:{araba2.renk}")

# EKRAN ÇIKTISI:
# -----ARABA 1-----
# Arabanın Markası:audi
# Arabanın Rengi:beyaz
# -----ARABA 2-----
# Arabanın Markası:ford
# Arabanın Rengi:siyah

class Canta():
    renk=""
    model=""
    def __str__(self):
        return f"Çantanın Rengi:{self.renk} ve Çantanın Modeli:{self.model}"

# canta1=Canta()
# canta1.renk="pembe"
# canta1.model="baget"
# print(canta1) #Çantanın Rengi:pembe ve Çantanın Modeli:baget

#Örnek:
# #Bir öğrenci sınıfı oluşturarak,attribute:
# olarak ad,soyad,numarası,doğum tarihi:str şeklinde tanımlayınız.ve 2 nesne üreterek içini doldurunuz.
#__str__'yi override ederek ad soyad /numarası şekinde gösteriniz

class Ogrenci:
    def __init__(self,ad:str,soyad:str,numara:str,dogumTarihi:str):
        self.ad=ad
        self.soyad=soyad
        self.numara=numara
        self.dogumTarihi=dogumTarihi
    def __str__(self):
        return (f"AD:{self.ad},SOYAD:{self.soyad},Numara:{self.numara},Doğum Tarihi:{self.dogumTarihi}")
    def __repr__(self):
          return     (f"AD:{self.ad},SOYAD:{self.soyad},Numara:{self.numara}")
# nesne 1:
ogrenci1=Ogrenci("GONCA","ÇOMAK","404","")
#print(ogrenci1)      #AD:GONCA,SOYAD:ÇOMAK,Numara:404,Doğum Tarihi:1997
ogrenci1.ad="zeynep"
ogrenci1.soyad="çomak"
ogrenci1.numara="404"
ogrenci1.dogumTarihi=""
print(ogrenci1)       #AD:zeynep,SOYAD:çomak,Numara:404,Doğum Tarihi:

#nesne 2:
ogrenci2=Ogrenci("Ece","Demir","209","")
print(ogrenci2)  #AD:Ece,SOYAD:Demir,Numara:209,Doğum Tarihi:

ogrenciler=[]
ogrenciler.append(ogrenci1)
ogrenciler.append(ogrenci2)
print(ogrenciler)  #[AD:zeynep,SOYAD:çomak,Numara:404, AD:Ece,SOYAD:Demir,Numara:209]

for ogrenci in ogrenciler:
    print(ogrenci.__dict__)  #{'ad': 'zeynep', 'soyad': 'çomak', 'numara': '404', 'dogumTarihi': ''}
                             #{'ad': 'Ece', 'soyad': 'Demir', 'numara': '209', 'dogumTarihi': ''}
# CONSTRUCTOR METHOD: Yapıcı Metot
#CLass bünyesinde tanımlanan bir özellik(attribute) bilgisine değer ataması yapabilmek için yapıcı method tanımlaması yapmalıyız.
#İlk çalışan metottur.
# class'ı create edebilmek için constructor metodu kullanılır.

class Person:
    def __init__(self,name,year):
        self.name=name
        self.year=year
        print("init metodu çalıştı.")

person1=Person("gonca",2022)  #init metodu çalıştı.
person2=Person("gül",202)     #init metodu çalıştı.

# __init__(self,....): constructorun ilk metotudur.
# pythondaki constructor'ı tanımlamak için kullanılır.

class Araba:             # Araba adına bir class yarattık.
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model
    def info(self):
        print(f"{self.marka}--{self.model}")

# araba1=Araba("AUDI","E8")
# print(araba1.marka) #AUDI
# print(araba1.model) #E8
# araba1.info() #AUDI--E8


# ÖRNEK:
##çalışan sınıfı oluşturunuz,init'de ad,soyad,işe giriş tarihi(datetime)alınız.
# sonra calisma_süresini_hesapla metotdu oluşturarak kaç yıldır çalıştığını dönen bir metot yazınız.
import datetime
class Calisan():
    def __init(self,ad:str,soyad:str,ise_giris_tarihi:datetime):
        self.name=ad
        self.surname=soyad
        self.ise_giris_tarihi=ise_giris_tarihi
    def calisma_gunu_hesapla(self):
        simdiki_zaman=datetime.datetime.now()
        fark=simdiki_zaman-self.ise_giris_tarihi
        yil=fark.days/365
        return yil
# calisan1=Calisan()
# calisan1.ise_giris_tarihi=datetime.datetime(2000,10,11)
# print(calisan1.calisma_gunu_hesapla())  #22.194520547945206
#
# calisan2=Calisan()
# calisan1.ise_giris_tarihi=datetime.datetime(2001,8,9)
# print(calisan2.calisma_gunu_hesapla())


# örnek:
class Student:
    sertifikalar=[]
    def __init__(self):
        self.sertifikalar=[]
    def sertifika_ekle(self,sertifika_adi):
        self.sertifikalar.append(sertifika_adi)
    def sertifikalari_goster(self):
        print(self.sertifikalar)

sertifika1=Student()
sertifika1.sertifika_ekle("formasyon")
sertifika1.sertifika_ekle("python")
sertifika1.sertifika_ekle("big data")
sertifika1.sertifikalari_goster()         #['formasyon', 'python', 'big data']


sertifika2=Student()
sertifika2.sertifika_ekle("word")
sertifika2.sertifika_ekle("excel")
sertifika2.sertifika_ekle("point")
sertifika2.sertifikalari_goster()   #['word', 'excel', 'point']

# Attributes:özellik
# sınıflar içerisinde class attributes yani class seviyesinde ya da nesne seviyesinde tanımlayabiliriz.


# ENCAPSULATİON ( KAPSÜLLEME )
# bazı özellik ve metotların her kişi tarafından erişilmemesi için gerekebilir.
'''
Sınıf içinde kullanılacak,kullanıcının bilmesine gerek olmayan verileri
gizlemek istediğimizde veya kontrollü şekilde veri set etmemiz gerektiğinde kullandığımız temel OOP kavramıdır.
gizlemek istediğimiz değişkenlerin başına __ eklenerek private yapılır.
kontrollü bir şekilde veri set etmek için de get/set metotları veya property tanımlanır.
'''
import math
class Daire:
    __pi_sayisi=math.pi   # __ encapsulation yapıldı.
    def __init__(self,yaricap):
        self.yaricap=yaricap
    def alan_hesapla(self):
        return self.__pi_sayisi*math.pow(self.yaricap,2)
    '''getter yada get metodu ile pi sayısını açabiliriz.'''
    def get_pi(self):
        return self.__pi_sayisi
    '''setter yada set metodu ilede pi sayısının değerini değiştirebiliriz hata mesajı veirilir.'''
    def set_pi(self,value):
        if not  (value==3 or value==3,14):
            raise Exception("Pi sayısı 3 ve ya 3.14 olan bir değerdir.")
        self.__pi_sayisi=value


daire1=Daire(2)
print(daire1.alan_hesapla())  #12.566370614359172
daire2=Daire(2)
daire2.set_pi(3)
print(daire2.alan_hesapla())  #12.0

'''
#ilk private yapıldı---> __pi_sayisi sonra,get edildi,
#get:talep ederse isterse ayrı metot yazılır.
#sonra set edildi.içerideki değeri kontrollü değiştirmek istediğimizde dışarıdaki kullanıcı değişkenin değerini değiştirmek istediğin de set ya da setter kullanıcaz.

'''
# PROPERTY:
# GET VE SET METOTLARINI TANIMLARKEN @property decarator kullanarak daha kısa tanımlayabiliriz.
class Ogrenci:
    def __init(self):
        self.__numara=1
    @property
    def numara(self):          #getter
        return self.__numara
    @numara.setter
    def numara(self,value):   #setter
        if not 100 <= value <=300:
            raise Exception("NUMARA DEĞERİ 100-300 ARALIĞINDADIR.")
        self.__numara=value

#sadece get metodu olan bir property tanımlanabilir.
ogrenci1=Ogrenci()
ogrenci1.numara=200
print(ogrenci1.numara)  #200


# INHERITANCE:KALITIM
'''
#kalıtım,sınıflar arasında hiyerarşik bir ilişki kurmamızı sağlar ve kod tekrarlarını önler.
#birden fazla sınıftan kalıtım alınabilir.
#oop genellikle diğer programlam dilleri ile aynıdır tek bir farkı vardır.

kullanım şekli:
# base class: kalıtım veren sınıf
# derived class:kalıtım alan sınıf

class BaseClass1:
    pass
class BaseClass2:
    pass

class DerivedClass(BaseClass1,BaseClass2):
    pass

class DerivedClass2(DerivedClass):
    pass

'''
# class Kamera:
#     def __init__(self,cozunurluk):
#         self.cozunurluk=""
#
#     def fotograf_cek(self):
#         print("fotoğraf çekildi.")
# class Radyo:
#     def radyo_cal(self,kanal):
#         self.kanal=""
#         print("radyo çalınıyor.")
# class Telefon(Kamera,Radyo):   #kalıtım aldı.
#     def arama_yap(self):
#         print("arama yapılıyor.")
#     def radyo_cal(self,kanal):    #override yapıldı.
#         print("telefonda radyo çalınıyor..")

# t1=Telefon()
# print(t1.cozunurluk)
# t1.fotograf_cek()
# t1.radyo_cal()
# t1.arama_yap()

#örnek:

class Okul:
    def __init__(self,isim,soyisim,yas):
        self.isim=isim
        self.soyisim=soyisim
        self.yas=yas
        print("okul sınıfı çalıştı.")

class Ogretmen(Okul):
    def __init__(self,isim,soyisim,yas):
        super().__init__(isim,soyisim,yas)
        print("öğretmen sınıfı çalıştı.")
    def intro(self):
        print (f"{self.isim} {self.soyisim} {self.yas} yaşında bir öğretmendir.".capitalize())

bir=Ogretmen("gonca","çomak","25")
bir.intro()  #Gonca çomak 25 yaşında bir öğretmendir.
iki=Ogretmen("berk","demir",26)
iki.intro()  #Berk demir 26 yaşında bir öğretmendir.

# ABSTRACT CLASS: SOYUT SINIFLAR
'''
Bu soyut sınıflar alt sınıflar için bir şablon görevi görürler.
Soyut sınıfların 2 özelliği vardır
1-) soyut sınıftan nesne üretilemez !
2-) Alt sınıfta bu metotları kullanacaksanız orada yeniden tanımlanmalı.
'''
#1-) Soyut sınıftan bir nesne üretilemez .
# from abc import ABC,abstractmethod
# class Hayvan(ABC):
#     @abstractmethod
#     def yürü(self):
#         pass
#     @abstractmethod
#     def kos(self):
#         pass
#
# class Kedi(Hayvan):
#     pass

#kus=Hayvan()   #TypeError: Can't instantiate abstract class Hayvan with abstract methods kos, yürü

# 2-) Alt sınıflarda bu metotları kullanacaksanız orada yeniden tanımlanmalı.
from abc import ABC,abstractmethod
class Hayvan(ABC):
    @abstractmethod
    def yürü(self):
        pass
    @abstractmethod
    def kos(self):
        pass
class Kedi(Hayvan):
    def yürü(self):
        print("kedi yürüyor.")
    def kos(self):
        print("kedi koşuyor.")

bir=Kedi()
bir.yürü()  #kedi yürüyor.
bir.kos()   #kedi koşuyor.

# Overriding(üzerine yazma-öncekini iptal etme)
'''Eğer alt sınıfta,ana sınıftan metotları aynı isimde tanımlarssak alt sınıftaki üst sınıftakini iptal eder ve
alt sınıftaki aktif olur.'''
class Okul:
    def __init__(self,isim,soyisim,yas):
        self.isim=isim
        self.soyisim=soyisim
        self.yas=yas
        print("okul sınıfı çalıştı.")
    def info(self):
        print(f"{self.isim} {self.soyisim} {self.yas} yaşında bir okul üyesidir.")
class Ogretmen(Okul):
    def __init__(self,isim,soyisim,yas,maas,uzmanlık):
         super().__init__(isim,soyisim,yas)
         self.maas=maas
         self.uzmanlık=uzmanlık
         print("öğretmen sınıfı çalıştı.")
    def info(self):
        print(f"{self.isim} {self.soyisim} {self.yas} yaşında ve {self.maas} maaşı olan bir {self.uzmanlık} öğretmenidir.")

bir=Okul("gonca","çomak",25)
bir.info() #gonca çomak 25 yaşında bir okul üyesidir.
iki=Ogretmen("gonca","çomak","25","15000","matematik")
iki.info()  #gonca çomak 25 yaşında ve 15000 maaşı olan bir matematik öğretmenidir.


# 5-) Polymorphism ( çok şekilcilik)
'''
Base sınıflarda tanımlanan metotların alt sınıflarda adı aynı kalmak üzere farklı bir
şekilde çalışmasını sağlayan OOP temel kavramlarından biridir.
Daha önceki örneklerde (4_Inheritance) kalıtım yoluyla bu kavramı uygulamıştık.
aşağıdaki örnekte ise function yöntemiyle polym.
uygulamasını görelim.

'''

from abc import ABC,abstractmethod
class Silah(ABC):
    @abstractmethod
    def ates_et(self):
        print("ateş edildi.")
class RoketAtar(Silah):
    def ates_et(self):
        #roket atılma işlemleri.
        print("roket atıldı....")

class OkAtarSilah(Silah):
    def ates_et(self):
        # ok atma işlemleri
        print("ok atıldı...")
rpg7=RoketAtar()
rpg7.ates_et()       #roket atıldı...

cross_bow=OkAtarSilah()
cross_bow.ates_et()   #ok atıldı...

def atesle(silah:Silah):
    silah.ates_et()
atesle(rpg7)            #roket atıldı....
atesle(cross_bow)       #ok atıldı....


# Örnek:
class Okul:
    def __init__(self,isim,soyisim,yas,maas):
        self.isim=isim
        self.soyisim=soyisim
        self.yas=yas
        self.maas=maas
        print("okul sınıfı çalıştı.")
    def info(self):
        print(f"{self.isim} {self.soyisim} {self.yas} yaşında ve {self.maas} maaş almaktadır.")
    def zam(self):
        return f"Güncel Maaş: {self.maas*1.2}"
class Ogretmen(Okul):
    def __init__(self,isim,soyisim,yas,maas,uzmanlik):
        super().__init__(isim,soyisim,yas,maas)
        self.uzmanlik=uzmanlik
        print("öğretmen sınıfı çalıştı.")
    def info(self):
        print(f"{self.isim} {self.soyisim} {self.yas} yaşında ve {self.maas} maaş alan bir {self.uzmanlik} bir öğretmendir.")
    def zam(self):
        return f"Güncel Maaş:{self.maas*1.5}"

class Yonetim(Okul):
    def __init__(self,isim,soyisim,yas,maas):
        super().__init__(isim,soyisim,yas,maas)
        print("yönetici sınıfı çalıştı.")
    def info(self):
        print(f"{self.isim} {self.soyisim} {self.yas} yaşında ve {self.maas} maaş alan bir  bir yöneticidir.")
    def zam(self):
        return f"Güncel Maaş:{self.maas*2}"

bir=Okul("gonca","çomak",25,6000)
bir.info()
print(bir.zam())       #okul sınıfı çalıştı.
                       #gonca çomak 25 yaşında ve 6000 maaş almaktadır.
                       #Güncel Maaş: 7200.0


iki=Ogretmen("gonca","çomak",25,6000,"matematik")
iki.info()
print(iki.zam())        #okul sınıfı çalıştı.
                        #öğretmen sınıfı çalıştı.
                        #gonca çomak 25 yaşında ve 6000 maaş alan bir matematik bir öğretmendir.

                        #Güncel Maaş:9000.0

uc=Yonetim("gonca","çomak",25,6000)
uc.info()
print(uc.zam())          #okul sınıfı çalıştı.
                         #yönetici sınıfı çalıştı.
                         #gonca çomak 25 yaşında ve 6000 maaş alan bir  bir yöneticidir.
                         #Güncel Maaş:12000
# her sınıf için ayrı bir zam oranı yapabildik.

# ENUM:hata ayıklmayı önleyen bir yöntem,kütüphanedir.
'''
ne zaman kullanılır ?
-sınırlı bir olası değeri olan değişken grubunuz varsa kullanmak uygun olur.
-sınıf içerisindeki değişkenler daha sonradan değiştirilmesin istiyorsanız kullanabilirsiniz.
-değişkenlerin tuttuğu değerler benzersiz olsun yani 2 değişken aynı değere sahip olmasın istiyorsanız kullanabilirsiniz.
'''
#import enum
# class Status(enum.Enum):
#     active=1
#     inactive=0
# for s in Status:                                #iterasyana soktuk.
#     print(s.name,s.value)  #active 1
#                            #inactive 0
# IntEnum: sıralama-ayrıştırma
# import enum
# class Status(enum.IntEnum):
#     new=2
#     closed=3
#     invalid=1
# #print(list(s.name for s in sorted(Status))) #['invalid', 'new', 'closed']


# @enum.unique :decarator
# import enum
# @enum.unique
# class Status(enum.Enum):
#     new=2
#     closed=3
#     invalid=1
#     inactive=1

# DUNDER ÇEŞİTLERİ:
'''
Dunder double underscore:Çift alt çizgi
__init__: constructor metod tanımı yaparken ilk kullanılan init metodur.
__str__:
__len__:
__repr__:
'''


# Örnekler:
class Calisan:
    zam_orani=1.05
    per_say=0
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
        self.eposta=self.ad+self.soyad+"@sirket.com"
        Calisan.per_say +=1
    def tamad(self):
        return f"ad:{self.ad} soyad:{self.soyad}"
    def zam(self):
        return f"Güncel maaş :{self.maas*self.zam_orani}"   # Calisan.zam_orani da olabilir.

personel1=Calisan("ali","demir",2500)
personel2=Calisan("kerim","bakir",1950)
Calisan.zam_orani=1.2

#personel1.zam_orani=1.1        #sonradan değişim yapılabilir.
print(personel1.maas)  #2500
print(personel1.zam()) #Güncel maaş :2625.0
#personel2.zam_orani=1.15      #sonradan değişim yapılabilir.
print(personel2.maas) #1950
print(personel2.zam()) #Güncel maaş :2047.5

# EXAMPLES:
class Parrot:
    #class attribute(sınıf özelliği)
    name=""
    age=0

# create parrot1 object
parrot1=Parrot()
parrot1.name="Blu"
parrot1.age=10

#create another object parrot2
parrot2=Parrot()
parrot2.name="Woo"
parrot2.age=15

# access attributes
print(f"{parrot1.name} is {parrot1.age} years old !") #Blu is 10 years old !
print(f"{parrot2.name} is {parrot2.age} years old !") #Woo is 15 years old !


#EXAMPLE -INHERITANCE(kalıtım)

#base class(temel sınıf)
class Animal:
    def eat(self):
        print("I can eat !")
    def sleep(self):
        print("I can sleep ! ")

#derived class(türetilmiş sınıf)
class Dog(Animal):
    def bark(self):
        print("I can bark! Woof woof!!")

#Create object of the Dog class
dog1=Dog()

#Calling members of the base class
dog1.eat()         #I can eat !
dog1.sleep()       #I can sleep !

#Calling members of the derived class
dog1.bark()        #I can bark! Woof woof!!

# examples -inheritance

class Animal:
    #attribute and method of the parent class
    name=""
    def eat(self):
        print("I can eat")
# inheritance from Animal
class Dog(Animal):
    #new methof in subclass
    def display(self):
        #access name attribute of superclass using self
        print("My name is",self.name)
# create an object of the subclass
labrador=Dog()
#access superclass attribute and method
labrador.name="Rohu"
labrador.eat()          #I can eat
#call subclass method
labrador.display()      #My name is Rohu

# example -overriding
class Animal:
    name=""
    def eat(self):
        print("I can eat")
# inheritance from Animal
class Dog(Animal):
    #override eat() method
    def eat(self):
        print("I like to eat bones")

labrador=Dog()
labrador.eat()    #I like to eat bones

# example:
class Animal:
    name=""
    def eat(self):
        print("I can eat")
class Dog(Animal):
    def eat(self):
        super().eat()
        print("I like to eat bones")
labrador=Dog()
labrador.eat()  #I can eat
                #I like to eat bones

# example - encapsulation:kapsülleme
class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print(f"Selling Price:{self.__maxprice}")
    def setMaxPrice(self,price):
        self.__maxprice=price

c=Computer()
c.sell()      #Selling Price:900

#change the price
c.__maxprice=1000
c.sell()      #Selling Price:900

#using setter function
c.setMaxPrice(1000)
c.sell()     #Selling Price:1000



# example- polymorphism

class Polygon:
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")
class Square(Polygon):
    #renders Square
    def render(self):
        print("Rendering square...")
class Circle(Polygon):
    #renders Circle
    def render(self):
        print("Rendering circle..")

#create an object of square
s1=Square()
s1.render()    #Rendering square...

#create an object of circle
s2=Circle()
s2.render()  #Rendering circle..

# example:
class Animal(object):
    def __init__(self,animal_type):
        print("Animal Type:",animal_type)
class Mammal(Animal):
    def __init__(self):
        #call superclass
        super().__init__("Mammal")
        print("Mammals give birth directly ")

dog=Mammal()  #Animal Type: Mammal
              #Mammals give birth directly

class Mammal(object):
    def __init__(self,mamma1Name):
        print(mamma1Name,"is a warm-blooded animal.")
class Dog(Mammal):
    def __init__(self):
        print("Dog has four legs")
        super().__init__("Dog")

d1=Dog()   #Dog has four legs
           #Dog is a warm-blooded animal.

#örnek:
### QUESTİON SINIFI
class Questions:    #sorular sınıfı oluştu.
    def __init__(self,text,choices,answer):
        self.text=text         #soru özelliği
        self.choices=choices   # şıklar özelliği
        self.answer=answer     # doğru cevap özelliği
    def checkAnswer(self,answer):
        return self.answer==answer

q1 = Question('en iyi programlama dili hangisidir ?', ['C#','python','javascript','java'], 'python')
q2 = Question('en popüler programlama dili hangisidir ?', ['python','javascript','C#','java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q4 = Question('en çok sevilen programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q5 = Question('en kolay programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')

questions = [q1,q2,q3,q4,q5]















































































































































































































































