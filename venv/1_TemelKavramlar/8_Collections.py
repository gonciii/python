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

# hocanın yaptığı:
sayi=int(input("Bir sayı giriniz:"))
liste=[]
for i in range(1,sayi+1):
    liste.append(i)
    liste.insert(i-1,i)
print(liste) #[1, 2, 3, 4, 5]

for i in liste:
    print(i)
# ---------------------------------------------------------
# 2.yöntem
sayi=int(input("Bir sayı giriniz:"))
liste=[]
liste.extend(range(1,sayi+1))
print(liste)

# Örnek:İnputtan 2 sayı alınız,ilk girilen sayı
# küçük ise artan sırayla;büyük ise azalan sırayla bir liste oluşturunuz.





