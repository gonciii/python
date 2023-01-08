# #PyMongo -> python ve mongodb arasında bağlatı kurmayı sağlayan bir
# #package pip install pymnongo ile yüklenebilir.
# import json
#
# import pymongo
#
# client=pymongo.MongoClient("mongodb://localhost:27017")
# #print(client.list_database_names()) # show dbs
#
#
# ## Bir database'e bağlanmak:
# # 2 yöntemi vardır :
#
# db=client.get_database("kitabevi") # use kitabevi 1
# #db=client.["kitabevi"] # use kitabevi 2
#
# # show tables'a karşılık gelen yapıdır.
# # 2 yapı olarak gösterilebilir :
# for i in db.list_collections():
#     print(i["name"])     #kitap
#
# print(db.list_collection_names()) #['kitap']
#
# kitaplar=db.get_collection("kitap") #db.kitap
# # kitaplar=db["kitap"]
#
# # print(kitaplar.find_one()) #kriteri sağlayan ilk veriyi döner.
# # print(type(kitaplar.find_one()))  #<class 'dict'>
# #
# # print(kitaplar.find())  #<pymongo.cursor.Cursor object at 0x00000284C3BC9E10> bunu for la döndürmek gerekiyor.cursor gördüğümüzde :
# # for i in kitaplar.find():
# #     print(i)
# #     #print(type(i))      #<class 'dict'> içindeki bütün elemanlar dict.
# #     print(i.get("kitap_adi"))
#
#
# # db'den veri çekerken performans için query'i en iyi şekilde yazmak tercih edilir.
# for i in kitaplar.find({},{"kitap_adi":1,"_id":0}):
#     print(i)
#
# #select kitap_adi from kitap where kitap_adi="Suç ve Ceza"
#
# eklenecek_kitap={
#     "kitap_adi":"Hayvan Çiftliği",
#     "yazar_adi":"George Orwell",
#     "yayin_tarihi":1877
# }
# #sonuc=kitaplar.insert_one(eklenecek_kitap)
# #print(sonuc.acknowledged,sonuc.inserted_id)
#
# print(kitaplar.find_one({"yazar_adi":"George Orwell"})) #tabloya eklenme sırasıyla kriteri sağlayan ilk veri gelir.
# #{'_id': ObjectId('63ba73ad1279c5683da22a1d'), 'kitap_adi': 'Hayvan Çiftliği', 'yazar_adi': 'George Orwell', 'yazar_tarihi': 1877}
#
#
# ### önemli ###
# # object id ile sorgu yazılacağı zaman ObjectId(id_no) şeklinde yazılması gerekiyor.
# print(kitaplar.find_one({"_id":"63ba73ad1279c5683da22a1d"})) # bu sağlamaz.
#
# # Bu şekilde sorgu yazılır :
# from bson import ObjectId
# print(kitaplar.find_one({"_id":ObjectId("63ba73ad1279c5683da22a1d")}))
# #{'_id': ObjectId('63ba73ad1279c5683da22a1d'), 'kitap_adi': 'Hayvan Çiftliği', 'yazar_adi': 'George Orwell', 'yazar_tarihi': 1877}
#
# ### regex ###
# '''
# . herhangi bir karakteri temsil eder
# ^ (shift+3+spacebar) stars with
# $ ends with
# .*karakter.* içinde karakter geçenleri SQL'deki -> where kitap_adi like '%karakter%' yapısına denk gelir.
# [] aralık temsil eder. [A-K]:A'dan K'ye kadar olanlar.
#                        [A,K]:A ve K demek
#
# '''
#
# # kitap adı S'ile başlayan kitapları getir.
# #query:sorgu
# q1={
#     "kitap_adi":{"$regex":"^S"}
# }
# for i in kitaplar.find(q1):
#     print(i)
#
# # sıralama sort("field",1 or -1) # tek kolona göre sıralama için
# # sort([("field",1),("field2",-1)]) birden fazla kalana gröe sıralama yapmak için.
#
# #ASCENDING :1' in
# #DESCENDING:-1'in karşılığı
# for i in kitaplar.find(q1).sort("kitap_adi",pymongo.ASCENDING):
#     print(i)
#
# for i in kitaplar.find(q1).sort([("yazar_adi",1),("kitap_adi",-1)]):
#     print(i)






