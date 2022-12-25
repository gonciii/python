# Mongo shell açıldığında enter'a basarak ve ya bir connection string girdikten sonra
# enter'ladığımızda o server'a bağlanabiliriz.
# Default olarak localhost:27017 ' e bağlanır.
# Tüm dbleri görmek için : show dbs veya show.datbases kodunu çalıştırız.
# Mevcut bir db üzerinde çalışmak için : use veritabanıAdi
# Veri tabanına yeni bir collection eklemek için: db.createCollection("tabloAdi")
# Veri tabanındaki tüm collectionları görmek için : show tables veya show collections
# Veri tabanındaki collection'ı silmek için : db.collectionAdi.drop()
# northwind> db.customers.drop()
# true
# northwind>  # örnek

#cls : ekrandakileri temizler.
# veritabanı create etmek için use veritabaniAdi sonrasında
#db.createCollection("collectionAdi") sırasıyla çalıştırmamız gerekir.
# veritabanı ilk tablo oluşturulana kadar db'ler arasında görünmez.
# veritabanı silmek için : db.dropDatebase()

#----------------
# ---Queries
# CRUD queries :
# create için :
# insertOne ve insertMany komutları var.
# db.kitap.insertOne({"kitap_adi":"Suç ve Ceza","yayin_tarihi":1866,"yazar_adi":"Dostoyevski"})

#
db.kitap.insertMany([
{"kitap_adi":"Suç ve Ceza","yazar_adi":"Dostoyevski","yayin_tarihi":1866},
{"kitap_adi":"Sefiller","yazar_adi":"Victor Hugo","yayin_tarihi":1862},
{"kitap_adi":"Anna Karenina","yazar_adi":"Lev Tolstoy","yayin_tarihi":1877},
{"kitap_adi":"Vadideki Zambak","yazar_adi":"Balzac","yayin_tarihi":1832},
{"kitap_adi":"Notre Dame'ın Kamburu","yazar_adi":"Victor Hugo","yayin_tarihi":1831},
{"kitap_adi":"Savaş ve Barış","yazar_adi":"Lev Tolstoy","yayin_tarihi":1867}
])

# Read queries:
# MongoDB
#collectiondaki tüm verileri görmek için : db.collectionAdi.find() örnek: db.kitap.find()
# ve ya db.kitap.find({})
# yazarı Victor Hugo olan kitapları listele :db.kitap.find("yazar_adi":"Victor Hugo"})
# DİĞER VERİ TABANI :
# SQL : w3schools.com test etmek için kullanılabilir.
# SQL: select*from kitap where yazar_adi="Victor Hugo"
# mongodb:
#collectionda kaç adet veri olduğunu bulmak için : db.collectionAdi.countDocuments()  ---örnek: db.kitap.countDocuments()
# SQL :
# select count(*) from kitap



