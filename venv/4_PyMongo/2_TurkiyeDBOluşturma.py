'''
iller.json dosyası içindeki illerin ve ilçelerin belli alanlarını adı turkiyedb olan bir veritabanına eklenmesi gerekmektedir.
eklenecek olanlar:
iller tablosuna >
il_adi
nüfus(int olarak kaydedilmesi gerekiyor bu yüzden .'ları kaldırmanız lazım)
plaka_kodu


ilçeler tablosuna >
il_kodu(illerdeki plka kodunundan alınız.)
ilce_adi
nufus(int olarak kaydedilmesi gerekiyor bu yüzden .'ları kaldırmanız lazım)


'''
# 1.dosyanın json.load ile açılması
# 2.dosya içindeki bilgilerin yeni bir dict.olarak ayrıştırılması
# 3.eklenecek_iller ve eklenecek_ilceler listelerinin doldurulması
# 4.veritabanıyla bağlantı kurulması
# 5.tabloların oluşturulması
# 6.tablolara eklenecek verilerin insert edilmesi.

# çözüm:
# 1.dosyanın json.load ile açılması :
import json

dict_iller = json.load(open("iller.json", encoding="UTF8"))
# print(dict_iller)
eklenecek_iller = []
eklenecek_ilceler = []
for il in dict_iller:
    il_adi = il["il_adi"]
    plaka_kodu = il["plaka_kodu"]
    nufus = il["nufus"]
    il_dict = {
        "il_adi": il_adi,
        "plaka_kodu": plaka_kodu,
        "nufus": int(str(nufus).replace(".", ""))  # noktalardan kurdardık,integer yaptık.
    }
    eklenecek_iller.append(il_dict)
    for ilce in il["ilceler"]:
        ilce_adi = ilce["ilce_adi"]
        ilce_nufus = ilce["nufus"]
        il_kodu = plaka_kodu
        dict_ilceler = {
            "ilce_adi": ilce_adi,
            "ilce_nufus": int(str(ilce_nufus).replace(".", "")),
            "il_kodu": il_kodu
        }
        eklenecek_ilceler.append(dict_ilceler)

print(eklenecek_iller)
print(eklenecek_ilceler)

# veri tabanı ile bağlantı kuruldu:
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
# veritabanı oluşturur:
db = client.get_database("turkiyedb")
# tabloların oluşturulması:
#
# db.create_collection("iller")    # create edildikten sonra kapatılması gerekiyor.
# db.create_collection("ilceler")
#
#print(db.list_collection_names())

# #tablolara ekelencek verilerin insert edilmesi:

iller_collection=db.get_collection("iller")
ilceler_collection=db["ilceler"]


# s1=iller_collection.insert_many(eklenecek_iller)
# s2=ilceler_collection.insert_many(eklenecek_ilceler)
# print(s1.acknowledged,s2.acknowledged)



