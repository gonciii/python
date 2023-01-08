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
print(iller.find_one({"il_adi":"Eskişehir"},{"_id":0,"nufus":1}))  #{'nufus': 871187}

#5-) en kalabalık 3 şehri adını ve nufusunu listeleyiniz
for i in iller.find({},{"_id":0,"il_adi":1,"nufus":1}).sort("nufus",-1).limit(3):
    print(i)
#{'il_adi': 'İstanbul', 'nufus': 15067724}
#{'il_adi': 'Ankara', 'nufus': 5503985}
#{'il_adi': 'İzmir', 'nufus': 4320519}


