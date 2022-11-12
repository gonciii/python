#Collections
# # İçerisinde birden fazla veri barındırabilen yapılardır.
# # 1.) List
# # birden fazla veri bulundurabilir.
# # verilerin aynı veri tipinden olma zorunluluğu yoktur.
# # aynı veriden birden fazla bulunabilir.
# # [] arasında tanımlama yapılabilir.
#
# karisik_liste=["nur","öztürk",True,160]
# # dizinin elemanlarına erişme: Liste[index_no]
# ad=karisik_liste[0]
# soyad=karisik_liste[1]
# # *** index no ' 0 dan başlar .
#
# print(karisik_liste[0])
# karisik_liste[0]="ali"
# print(karisik_liste[0])
#
# print(karisik_liste)    #['ali', 'öztürk', True, 160]
# for i in karisik_liste:
#     print(i)
# '''
# ali
# öztürk
# True
# 160
# '''
# # karisik_liste[4]=77   #IndexError: list assignment index out of range
# # print(karisik_liste)
#
# # T veri tipinin farketmediğini belli ediyor.
# # ------append (value) ------>listede olmayan bir veriyi eklemek için kullanırız.tüm veri tiplerini ekleyebiliyoruz.
# # ....=append gibi bir kullanım yapamayız.

# karisik_liste.append(77)
# print(karisik_liste)
#
# # -----insert(index,value)
# # öteleme yapıp ,+1  gibi
#
# karisik_liste.insert(2,"mezun")
# print(karisik_liste)
#
# # -------extend: birden fazla veriyi aynı anda ekleyebilir.tuple gibi tipleride ekler ancak hepsini liste çevirerek yapar.
# iller=["ankara","izmir","adana"]
# print(iller)
# iller.extend(["istanbul","eskişehir","bursa"])
# print(iller)
#
# # -----reverse: Lİsteyi ters çevirir.
# # iller.reverse()
# # print(iller)
#
# # -----sort: listein sıralanmasını sağlar. default:küçükten büyüğe ---ascii table
# # iller.sort()
# iller.sort(reverse=True) #büyükten küçüğe sıralama yapar.
# print(iller)
#
# # -----clear: boş bir liste haline getirir.
# # # iller.clear()
# # print(iller)  # []
#
# # -----del:tamamen referansını siler.ram üzerindeki yer tutan şeyi siler.
# # del iller
# # print(del)
#
# # -------copy:
# # iller_kopya=iller.copy()
# # print(iller_kopya)
#
# # ------count: #veriyi aradığımızda sorgulatma yapabiliriz ? kaç tane olduğunu döndürür.
# # # iller.append("ankara")
# # print(iller)
# # s=iller.count("ankara123a") #bulamazsa eğer 0 döner.bulursa kaç tane olduğunu sayar.
# # print(s)
#
# # -------remove=index değil.value bekler.  ---bulamazsa eğer ValueError:list.remove(x): x not in list
# #direk siler,eğer bulamazsa error verir.
#
# # iller.remove("bursa")
# # print(iller)
#
#
# # ------pop:hem silip hem değeri döndrüebiliir.
# #geriye değer döndürebilir.
# # silinen_deger=iller.pop(3)
# # print(silinen_deger)
# # print(iller)
#
# # # len:collection içinde kaç tane eleman olduğunu bulur.
# # eleman_sayisi=len(iller)
# # print(eleman_sayisi)
# # # sum:
# # toplam=sum([1,2,3,4,5])
# # print(toplam)
# # # min,max:
# # print(mil(iller)) #stringlerle ve ya sayısal değerlerle çalışabilir.
# # print(max([192,13,41,523,44]))
# # # any
# # print(any(iller)) #true
# # print(any([])) # false

# # slicing:
# # index yapısından dolayı slicing: şeklinde kullanılır.
# isimler=["damla","aykut","umut","neslihan","tayfun","emre","gonca","elifsu","mert"]
# print(len(isimler))
# print(isimler[0])
# print(isimler[4])
# # en sonunca eleman
# en_son_index=len(isimler)-1
# print(isimler[en_son_index])
# s1=isimler[2:5] #2.ci indexten başlayarak 5.ci indexe kadar elemanları
# # kesip size geri verir.(5 dahil değil)
# print(s1)   #['umut', 'neslihan', 'tayfun']
#
# s2=isimler[3:] #3.cü indexten listenin sonuna kadarki  elemanları dahil eder.
# print(s2) #['neslihan', 'tayfun', 'emre', 'gonca', 'elifsu', 'mert']
#
# s3=isimler[:5]  #0.ci indexten başlar 5.ci indexe kadar.5 dahil değildir.
# print(s3)   #['damla', 'aykut', 'umut', 'neslihan', 'tayfun']
#
# s4=isimler[:] #tüm elemanları getirir.
# print(s4)   #['damla', 'aykut', 'umut', 'neslihan', 'tayfun', 'emre', 'gonca', 'elifsu', 'mert']
#
# s5=isimler[3:-3] #- listenin sondan index sayaacağını gösterir ancak 0 olamayacağı için
# # -1 den başlar.
# # 3.indexten başlar -3.cü indexe kadarki elemanları getirir.(-3. index dahil değilidir.)
# print(s5) #['neslihan', 'tayfun', 'emre']


#Örnek:1 den girilen sayıya kadar olan sayıları bir listeye ekleyen bir uygulama yazınız.
# benim yaptığım:
# sayi=int(input("Lütfen bir sayı giriniz:"))
# list=[]
# for list in range(1,(sayi)+1):
#     print(list)

# # hocanın yaptığı:
# sayi=int(input("Bir sayı giriniz:"))
# liste=[]
# for i in range(1,sayi+1):
#     liste.append(i)
#     liste.insert(i-1,i)
# print(liste) #[1, 2, 3, 4, 5]
#
# for i in liste:
#     print(i)
# # ---------------------------------------------------------
# # 2.yöntem
# sayi=int(input("Bir sayı giriniz:"))
# liste=[]
# liste.extend(range(1,sayi+1))
# print(liste)

# # Örnek:İnputtan 2 sayı alınız,ilk girilen sayı
# # küçük ise artan sırayla;büyük ise azalan sırayla bir liste oluşturunuz.
# sayi1=int(input("1.Sayıyı giriniz:"))
# sayi2=int(input("2.Sayıyı giriniz:"))
# artis_miktari=1
# if sayi1>sayi2:
#     artis_miktari=-1
# # alternatif kısa yöntemi artis_miktari=1 if sayi1>sayi2 else -1
# liste=[]
# for i in range(sayi1,sayi2+artis_miktari,artis_miktari):
#     liste.append(i)
# print(liste)

# # Diğer bir yol:
# sayi1 = int(input("bir sayı giriniz: "))
# sayi2 = int(input("ikinci bir sayı giriniz: "))
# liste= []
# if sayi1 < sayi2:
#     liste.extend(range(sayi1, sayi2+ 1))
# else:
#     liste.extend(range(sayi1, sayi2- 1, - 1))
# print(liste)

# Örnek: A'dan Z'ye kadar olan harfleri döngü ile listeye ekleyiniz.

# # ------NOTE:
# ord("a") #içine bir string alır.içindeki aparametre olarak bir sembol alır.
# ascii_karsiligi=ord("a")  #a->97 b>-98
# harf_karsiligi=chr((97))
# print(ascii_karsiligi,harf_karsiligi)

# ---------------------------------

# kucuk_harfler_listesi=[]
# for i in range(ord("a"),ord("z")+1):
#     kucuk_harfler_listesi.append(chr(i))
# print(kucuk_harfler_listesi)
#
# buyuk_harfler_listesi=[]
# for i in range(ord("A"),ord("Z")+1):
#     buyuk_harfler_listesi.append(chr(i))
# print(buyuk_harfler_listesi)
#
# rakam=[]
# for i in range(ord("0"),ord("9")+1):
#     rakam.append(chr(i))
# print(rakam)

# ÖRNEK:SAYILAR İSİMLİ BİR LİSTEYE 10 TANE RASTGELE SAYI ÜRETEREK EKLEYİNİZ.ÜRETİLECEK SAYILAR (1-100)
# ARASINDA OLSUN.

# sayilar=[]
# import random as rnd
# for i in range(0,10):
#     rsayi=rnd.randint(1,100)
#     sayilar.append(rnd.randint(1,100))
# print(sayilar)

# # başka bir metot:
# import random as rnd
# rastgele_sayilar= rnd.sample(range(1,101),10)
# print(rastgele_sayilar)

# geliştirme:eğer rastgele üretilen bir sayı daha önce varsa eklemeyelim
# sayilar=[]
# import random as rnd
# for i in range(10):
#      rsayi=rnd.randint(1,100)
#      if sayilar.count(rsayi)==0:
#          sayilar.append(rsayi)
#
# print(sayilar) -----------------bu for ile olamıyor .

# çözüm:
# index=0
# while index < 10:
#     rsayi = rnd.randint(1, 100)
#     if sayilar.count(rsayi) == 0:
#         sayilar.append(rsayi)
#         index+=1
#
# # ------------------------------------------
# dongu_kac_kez_dondu=0
# while len(sayilar)<10:
#     dongu_kac_kez_dondu+=1
#     rsayi = rnd.randint(1, 100)
#     if sayilar.count(rsayi) == 0:
#         sayilar.append(rsayi)
# print(sayilar)
# print(dongu_kac_kez_dondu)

# ----------------------------------------------

# Müşteriden kaç kolon oynamak istediğini alalım.Sonrasında
# 1 kolan için 1-49(49) dahil rastgele 6 tane sayı üretilsin ve bir listeye eklesin  ve kçükten büyüğe doğru sıralansın.
# Her kolan için aynı işlemler yapılsın.

# ÇÖZÜM:

# import random as rnd #sayfanın en üstüne eklenmesi önerilir.
# ana_liste=[]
# kolon_sayi=int(input("Kolon sayısı giriniz:"))
#
# for i in range(kolon_sayi):
#      liste = []
#      while len(liste) < 6:
#            uretilen = rnd.randint(1, 49)
#            if liste.count(uretilen)==0:
#              liste.append(uretilen)
#      liste.sort()      #sıralıyor.
#      ana_liste.append(liste)
#      #liste=[] #clear kullanamadık çünkü clear listede değişiklik yaptığı için
#
# print(ana_liste)

# -------------------------------------------
# ÖRNEK:
# kullanıcı hayır(h) diyene kadar veri almaya ve girilen değeri bir listeye eklyen uyg.yazınız.
# Listeye hem index no hemde veri ile birlikte alt alta yazdırınız.
# 1.ankara
# 2.izmir
# 3.izmir

# iller=[]
# while True:
#     il=input("İl giriniz:")
#     iller.append(il)
#     girilen=input("Devam etmek istiyor musunuz? E/H yazınız.")
#     if girilen.lower()=="h":
#         break

# for i in range(len(iller)):
#     print(f"{i+1}.{iller[i]}")
# -------------------------------------------------------------

# for il in iller:
#     print(f"{iller.index(il)+1}.{il}")
# --------------------------------------------------------------

# while True:
#     girilen=input("İL giriniz:")
#     if girilen.lower()=="h":
#         break
#     iller.append(girilen) --------->başka bir yöntem !!


# ÖDEV:
# password generator:
# kaç karakterli bir şifre istiyorsunuz ? 6
# büyük harf istiyor musunuz ? e  [A B C D E ...Z]
# küçük harf istiyor musunuz ? e  [a b c d ...z]
# rakam istiyor musunuz ? e [0 1,2....9]
# sembol istiyor musunuz ? h
# Ascii table
# t 3 _ _ _ _ _

#
# karakter_sayisi=int(input("Kaç karakterli şifre istiyorsunuz,lütfen giriniz :"))
# buyuk_harf_olacak_mi=input("Büyük  olacak mı ?: e/h")
# kucuk_harf_olacak_mi=input("Küçük olacak mı ?: e/h")
# rakam_harf_olacak_mi=input("Rakam  olacak mı ?: e/h")
# sembol_harf_olacak_mi=input("Sembol  olacak mı ?: e/h")
#
# buyuk_harfler=[]
# kucuk_harfler=[]
# rakamlar=list(range(0,10))
# semboller=[]
# # ord("a")->97  chr(97)-->"a"
# for i in range(ord("A"),ord("Z")+1):
#     buyuk_harfler.append(chr(i))
#
# for i in range(ord("a"),ord("z")+1):
#     kucuk_harfler.append(chr(i))
#
# for i in range(ord("!"),ord("/")+1):
#     semboller.append(chr(i))
#
# import random as rnd #döngü içinde kullanma !!
# #password =[]
# password=""
# while len(password) <karakter_sayisi:
#     uretilen=rnd.randint(0,3)
#     match uretilen:
#         case 0: #büyük harfler
#             if buyuk_harf_olacak_mi=="e":
#                 password += buyuk_harfler[rnd.randint(0,len(buyuk_harfler)-1)]
#         case 1: #küçük harfler
#             if  kucuk_harf_olacak_mi=="e":
#                 password += kucuk_harfler[rnd.randint(0,len(kucuk_harfler)-1)]
#         case 2: # rakamlar
#             if  rakam_harf_olacak_mi=="e":
#                 password += str(rakamlar[rnd.randint(0,len(rakamlar)-1)])
#         case 3: #semboller
#             if  sembol_harf_olacak_mi=="e":
#                 password += semboller[rnd.randint(0,len(semboller)-1)]
# print(password)

# 2-) TUPLE
# collectiondur.
# listten farklı olarak değeri sonradan değiştirilemez.
# () şeklinde tanımlanır.
# slicing yapılabilir.
# index mantığı vardır.
# t1=()  #boş tuple.
# print(type(t1))  #<class 'tuple'>
#
# t2=(1,1,1,2,3,4,5,6)
# print(t2)

# VERİ ALMAK İSTEDİĞİMİZ ZAMAN:
# print(t2[3])  #indexler 0 dan başlar.
#t2[3]=10  #TypeError: 'tuple' object does not support item assignment
# tuppların değerini sonradan değiştiremeyiz.
# TUPLE'IN 2 tane metodu vardır:
# count ve index
# print(t2.count(1))  #3
# print(t2.index(4))  #5
#
# del t2[2] #TypeError: 'tuple' object doesn't support item deletion
# # değeri silmek istediğimiz için ve tuple'lar değiştirilemeyeceği için hata verir.
# del t2   #tanımlanan bir değişkeni tamamen sildiğimiz için bu hata vermez.
# print(t2)  #yukarıdaki satırda bu değişkeni ramden kaldırdığı için bu değere erişilemez.
#
# # slicing kullanımı:
# sayilar=(11,12,13,14,15,16)
# print(sayilar[2:4]) #sondaki index dahil olmuyor. --> 13,14
# print(sayılar[2:-1]) #-1 dahil değil .---> 13,14,15
# # tuple kullanım amacı:
'''
Tuple vs list
-tuple kopya üretemiyor.ram üzerinden bakılıyor.daha az ram kullanır.
içinde dğişiklik olamayacağı için az veri ve ram kullanımından dolayı tuple kullanılır.,
-tuple nesnenin kopyasını üretmez direkt olarak nesnenin kendisini kullanır,list ise 
nesnenin kopyasını üreterek çalışır.
-boyutları sabit olduğundan ramde sıkıştırılmış olarak tutulurlar.
-list'lere append denildiğinde fazladan yer açarak boyutlanır.
-list() 0
-list().append(x) -->3
-kısaca daha hızlı ve daha az yer kaplarlar.
'''
# 3-)Set
'''
-matematikteki kümelere benzer.
-tanımlaması --- {} işaretleri arasında tanımlanır.
-ancak bu şekilde boş set tanımlanamaz.çünkü bu tanım dict'e aittir.
-eleman tekrarı yoktur.
-Değerleri değiştirilebilir ve ya silinebilir.
-Index yapısı yoktur.
-Slicing yoktur.
'''
# s1={}
# print(type(s1))  #class,dict
# s2=set()
# print(type(s2))  #class,set
# s3={1,1,1,1,2,3,4,5}
# print(len(s3))
#9 değeri vermez çünkü tekrar eden elemenları 1 olarak sayar.
# s3[2]=19

# ------SET METTOTLARI:
# ------add
# s3={1,1,1,1,2,3,4,5}
# print(len(s3))
# s3.add(6)
# s3.add(7)
# print(s3)
# # -----update:
# s3.update([7,8,9])
# s3.update([10,11,12])
# print(s3)
#
# # ----discard: bu silinmek istenen veriyi bulamazsa birşey yapmaz
# s3.discard(10)
# print(s3)
#
# # -----remove: bu silinmek istenen veriyi bulamazsa hata döner
# # s3.remove(20)
# # print(s3)
#
# # -----pop: set'in en baştaki elemanını siler.
# #  ve o elemanı size döner.
# print(s3.pop())
# print(s3)

# clear :siliyor
# copy: başka bir listeye atıyır.
# s3={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# ------difference: fark alma metotu.
# s3={1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
# s4={10,11,12,13,14,15}
# s4_un_farki=s4.difference(s3)
# print(s3.difference(s4))
# -----difference_update:farkını bulur ve ana set üzerinde o farklı olanları siler.
# s3.difference_update(s4)
# print(s3)
# print(s4)

# ------intersection:
# kesisim_kumesi=s3.intersection(s4)
# print("kesişim",kesisim_kumesi)
#
# # -------union:
# birlesim_kumesi=s3.union(s4)
# print("birleşim",birlesim_kumesi)

#
# s3.isdisjoint(s4):kümelerin ayrık olup olmadığını döner.
# True/False döner
# s3.issubset(s4):küme diğerinin alt kümesi mi?
# s3.issuperset(s4):kümenin diğer kümeyi kapsamadığını döner.
# ---CRUD :create read update delete..(list daha çok karşınıza çıkar)

# 4-) Dictionary
'''
-key-value şeklinde veri tutar.
-{} içinde tanımlanır. set gibi değil.{key:value} şeklinde tanımlanır.
-key:string,numeric ve ya tuple cinsinden tanımlanabiir.
birden fazla aynı isimden key kullanılırsa en son hangisi tanımlandıysa onun value'sunu verir.
-aynı keyden birden fazla tanımlama yapmayın demek isteniyor.
-value:tüm veri tiplerinden tanımlanabilir.
'''
# ogrenci={"nur","öztürk",True,1} #mesela bu bir set oldu.
ogrenci={
    "ad":"nur",
    "soyad":"öztürk",
    "mezun_mu":True,
    "il_plaka":6,
    "mezun_bolumleri":["istatistik","pc müh","psikoloji"],
    (6,):"yaşadığı il",
    99:"diğer"
}
# dictionary_degiskeni[key]
print(ogrenci["ad"])
print(ogrenci[(6,)])
print(ogrenci[99])   #index değil.key bu şekilde tanımlandığı için bu şekilde veriyi isteriz
ogrenci["ad"]="rabia nur"
print(ogrenci)  #veri güncellenebilir.

# del ogrenci["mezun_mu"]
# print(ogrenci)  #veriyi siliyor.


# Dictionary metotları:
# ----update:veri eklemek için kullanılır.
# update(*kwargs): (key=value)--string gibi yazılmıyor.(key değeri string vb yazmıyoruz)
# ogrenci.update(okul="Gazi")
# print(ogrenci)
#
# # ------pop:veri silmek için kullanılır.
# print(ogrenci.pop("ad"))
# print(ogrenci)
#
# # -----popitem:son veriyi siler.
# #ogrenci.popitem() #en son veriyi siliyor.
#
# #-----get
# print(ogrenci.get("soyad")) #değeri döndürür.
#
# # ----items: for ile kullanıcaz
# print(ogrenci.items()) #tuple listesi
#
# # print(ogrenci.keys())
# # print(ogrenci.values())

for (key,value) in ogrenci.items():
    print(f"key:{key}  value={value}")

for i in ogrenci.values():
    print(i)

for i in ogrenci.keys():
    print(ogrenci.get(i))

ogrenciler=[
    {
        "ad":"nur",
        "soyad":"öztürk",
        "il":"ankara"
    },
    {
        "ad":"damla",
        "soyad":"kahraman",
        "il":"izmir"
    },
    {
        "ad":"tayfun",
        "soyad":"karakavuz",
        "il":"izmir"
    }
]

# uzun versiyon:
ogrenci=ogrenciler[1]
print(ogrenci["ad"])
# kısa versiyon:
print(ogrenciler[1])
print(ogrenciler[1]["ad"])
# JSON (javascript object natation)tipine benzerler.


















