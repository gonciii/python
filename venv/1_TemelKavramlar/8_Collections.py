#Collections
# İçerisinde birden fazla veri barındırabilen yapılardır.
# 1.) List
# birden fazla veri bulundurabilir.
# verilerin aynı veri tipinden olma zorunluluğu yoktur.
# aynı veriden birden fazla bulunabilir.
# [] arasında tanımlama yapılabilir.

karisik_liste=["nur","öztürk",True,160]
# dizinin elemanlarına erişme: Liste[index_no]
ad=karisik_liste[0]
soyad=karisik_liste[1]
# *** index no ' 0 dan başlar .

print(karisik_liste[0])
karisik_liste[0]="ali"
print(karisik_liste[0])

print(karisik_liste)    #['ali', 'öztürk', True, 160]
for i in karisik_liste:
    print(i)
'''
ali
öztürk
True
160
'''
# karisik_liste[4]=77   #IndexError: list assignment index out of range
# print(karisik_liste)

# T veri tipinin farketmediğini belli ediyor.
# ------append (value) ------>listede olmayan bir veriyi eklemek için kullanırız.tüm veri tiplerini ekleyebiliyoruz.
# ....=append gibi bir kullanım yapamayız.

karisik_liste.append(77)
print(karisik_liste)

# -----insert(index,value)
# öteleme yapıp ,+1  gibi

karisik_liste.insert(2,"mezun")
print(karisik_liste)

# -------extend: birden fazla veriyi aynı anda ekleyebilir.tuple gibi tipleride ekler ancak hepsini liste çevirerek yapar.
iller=["ankara","izmir","adana"]
print(iller)
iller.extend(["istanbul","eskişehir","bursa"])
print(iller)

# -----reverse: Lİsteyi ters çevirir.
# iller.reverse()
# print(iller)

# -----sort: listein sıralanmasını sağlar. default:küçükten büyüğe ---ascii table
# iller.sort()
iller.sort(reverse=True) #büyükten küçüğe sıralama yapar.
print(iller)

# -----clear: boş bir liste haline getirir.
# # iller.clear()
# print(iller)  # []

# -----del:tamamen referansını siler.ram üzerindeki yer tutan şeyi siler.
# del iller
# print(del)

# -------copy:
# iller_kopya=iller.copy()
# print(iller_kopya)

# ------count:
# # iller.append("ankara")
# print(iller)
# s=iller.count("ankara123a") #bulamazsa eğer 0 döner.bulursa kaç tane olduğunu sayar.
# print(s)

# -------remove=index değil.value bekler.  ---bulamazsa eğer ValueError:list.remove(x): x not in list
# iller.remove("bursa")
# print(iller)


# ------pop:hem silip hem değeri döndrüebiliir.
# silinen_deger=iller.pop(3)
# print(silinen_deger)
# print(iller)