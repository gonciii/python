import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017")

db=client["turkiyedb"]

iller=db["iller"]
ilceler=db["ilceler"]

#1-) Tüm illeri listeleyiniz.
# query={}
# for i in iller.find(query):
#     print(i)

#2-) İlçelerin id dışındaki bilgilerini listeleyiniz.
# query={}
# for i in ilceler.find({},{"_id":0}):    id istemediğimiz için _id:0 olucak.
#     print(i)

#3-) kaç il-ilçe vardır ?
# print(iller.count_documents({}))  #81
# print(ilceler.count_documents({}))  #971

#4-) il adı Eskişehir olan ilin nüfusu kaçtır ?
#print(iller.find_one({"il_adi":"Eskişehir"},{"_id":0,"nufus":1}))  #{'nufus': 871187}

#5-) en kalabalık 3 şehri adını ve nufusunu listeleyiniz
# for i in iller.find({},{"_id":0,"il_adi":1,"nufus":1}).sort("nufus",-1).limit(3):
    #print(i)
#{'il_adi': 'İstanbul', 'nufus': 15067724}
#{'il_adi': 'Ankara', 'nufus': 5503985}
#{'il_adi': 'İzmir', 'nufus': 4320519}

#6-) il adında Ankara,İstanbul,Antalya olanları getiriniz.
# aynı field içinde arama yapıldığı için in kullanılması en kısa yoludur,ancak or ile de yazılabilir.

#1.çözüm :

# for i in iller.find({"il_adi":{"$in":["Ankara","İstanbul","Antalya"]}}):
#     print(i)
'''
{'_id': ObjectId('63ba9a5dc40a729a158e701f'), 'il_adi': 'Ankara', 'plaka_kodu': '06', 'nufus': 5503985}
{'_id': ObjectId('63ba9a5dc40a729a158e7020'), 'il_adi': 'Antalya', 'plaka_kodu': '07', 'nufus': 2426356}
{'_id': ObjectId('63ba9a5dc40a729a158e703b'), 'il_adi': 'İstanbul', 'plaka_kodu': '34', 'nufus': 15067724}

'''
# 2.çözüm:

query={
    "il_adi":
        {
            "$in":["Ankara","İstanbul","Antalya"]
        }
}

# for i in iller.find(query):
#     print(i)

#7-) nüfusu 100'bin altında olan illeri getiriniz.(nufusa göre en kalabalık şehir üstte gelsin.

query={
    "nufus":{
        "$lte":100000
    }
}
#sorgu1=iller.find(query).sort("nufus",-1)
# for i in sorgu1:
#     print(i)
'''
{'_id': ObjectId('63ba9a5dc40a729a158e7064'), 'il_adi': 'Ardahan', 'plaka_kodu': '75', 'nufus': 98907}
{'_id': ObjectId('63ba9a5dc40a729a158e7057'), 'il_adi': 'Tunceli', 'plaka_kodu': '62', 'nufus': 88198}
{'_id': ObjectId('63ba9a5dc40a729a158e705e'), 'il_adi': 'Bayburt', 'plaka_kodu': '69', 'nufus': 82274}

'''
#8-) illeri önce adını tersten sonra nufusa göre artan sıralama yapınız.
# collation : türkçe karakterden dolayı kullanıldı.
# sorgu=iller.find().collation({"locale":"tr"}).sort([("il_adi",-1),("nufus",1)])
# for i in sorgu:
#     print(i)
#
#9-) A harfi ile başlayan illeri listeleyiniz.
# ve nufusa göre sıralama yapınız.
query={
    "il_adi":{"$regex":"^A"}
}
sorgu=iller.find(query,{"_id":0}).sort("nufus",1)
# for i in sorgu:
#     print(i)
# 10-)  içinde an geçen illerden ilk 3 tanesini atlyaıp sonraki 2 tanesini listeleyiniz.(regex)

# query={
#     "il_adi":{"$regex":".*an.*"}
# }
# sorgu=iller.find(query).sort("nufus",1).skip(3).limit(2)
# for i in sorgu:
#     print(i)

# pagination formül : skip kısmında kullanılan : count*(page-1) limit kısmının içinede count geliyor.

#11-) ankaranın ilçelerini listeleyiniz.
# query={"il_kodu":"06"}
# sorgu=ilceler.find(query).sort("ilce_adi",1)
# for i in sorgu:
#     print(i)

#12-) ilçe adı A ile başlayan ankaranın ilçelerini listeleyiniz ve nufusa görede tersten sıralama yapınız.
# #query={
#     "$and":[
#         {
#             "il_kodu":"06"
#
#         },
#         {
#             "ilce_adi":{"$regex":"^A"}
#
#         },
#         {
#             "ilce_nufus":{"$gte":20000}
#
#         }
#     ]
# }
# sorgu=ilceler.find(query).sort("ilce_nufus",-1)
# for i in sorgu:
#     print(i)

#13-) illeri ve o illerin ilçelerini aynı sorgu sonucunda gösteriniz :(join) iki tabloyu
# birleştirip ortak sonuc getirmeniz isteniyor.: aggregate() $lookup

#localField ve foreignField kısmında değerler aynı olmalı key-value şeklindeki value değerleri aynı olmalı ki sonrasında karışık değerler veirlir.
# query=[
#     {
#         "$lookup":{
#             "from":"ilceler",           #iller tablosu hangi tabloyla bağlanılacak
#             "localField":"plaka_kodu" , #iller tablosundaki hangi lan iller tablosuyla bağlı olacak kısmına denk gelir.
#             "foreignField":"il_kodu",   #ilçeler tablosundaki hangi alan il tablosuyla bağlı
#             "as":"ilceler"
#         }
#     }
# ]
# sorgu=iller.aggregate(query)
# import pprint as pp
# for i in sorgu:
#     pp.pprint(i)

# diğer bi kullanımı :
query=[
    {
        "$lookup":{
            "from":"ilceler",           #iller tablosu hangi tabloyla bağlanılacak
            "localField":"plaka_kodu" , #iller tablosundaki hangi lan iller tablosuyla bağlı olacak kısmına denk gelir.
            "foreignField":"il_kodu",   #ilçeler tablosundaki hangi alan il tablosuyla bağlı
            "as":"ilceler"
        }
    },
    {
        "$project":{
            "_id":0,
            "il_adi":1,
            "ilceler":{
                "ilce_adi":1
            }
        }
    },
    {
        "$limit":2
    },
    {
        "$sort":{"il_adi":-1}
    }
]
sorgu=iller.aggregate(query)
import pprint as pp
for i in sorgu:
    pp.pprint(i)

# bu ksımda limt,sort sorgusu aggregateden dolayı query içine yazılır.

#14-) illeri ilçe sayılarıyla birlikte listeleyiniz.
# ankara : ilce sayısı :25... gibi

query=[
    {
        "$group":{
            "_id":"$il_kodu",
            "ilce_sayisi":{"$count":{}}
        }
    },
    {
        "$sort":{"_id":1}
    },
    {
        "$lookup":{
            "from":"iller",
            "localField":"_id",
            "foreignField":"plaka_kodu",
            "as":"il"
        }
    },
    {
        "$project":{"il.il_adi":1,"ilce_sayisi":1}
    }
]
sorgu=ilceler.aggregate(query)
import pprint
for i in sorgu:
    pp.pprint(i)               #{'_id': '81', 'il': [{'il_adi': 'Düzce'}], 'ilce_sayisi': 8}




# EKSTRA NOT :
# python mongodb yazı kısmı çok değişmediği için bu yönden avantajlıdır.
# diğer programlama dilleri için :
# C# EntityFramework,Dopper vb Kitap.Where(x=>x.KitapAdi="Suç ve Ceza") -> select * from kitap where
# KitapAdi ="Suç ve Ceza"

# reqres le veri çekip
# db create edip
# sorgu atabilir miyiz buna bakabilirsiniz gibi bir fikir geldi.
