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
'''
#RDBMS      #NoSQL
table        collections
row          document
column       field
'''

#büyük datalarda-NoSQL(performans bakımından daha iyi)
#banka,asker..  -RDBMS


# Lev Tolstoy'un yazdığı kitapları listeleyinniz
#db.kitap.find({yazar_adi:"Lev Tolstoy"})

# ctrl+c -> o anki sorguyu iptal eder,yeni bir query açılır.

# yayın tarihi 1865'den sonra yazılmış olan kitapları
# listeleyiniz:
# kitabevi> db.kitap.find({yayin_tarihi:{$gte:1865}})
'''
> :gt
< :lt
>= : gte
<= :lte
!= : ne
'''

# Lev Tolstoy dışındaki yazarların yazdığı kitapları listeleyiniz:
# kitabevi> db.kitap.find({yazar_adi:{$ne:"Lev Tolstoy"}})

# and and or
# iki veya daha fazla  sorgu cümlesini birleştirir.
#  db.kitap.find({$and:[{query1},{quer2}]})
#  db.kitap.find({$and:[{query1},{query2}]})

# Victor Hugo'nun 1862'de yazdığı kitapları getiriniz.
#  db.kitap.find({$and:[{yazar_adi:"Victor Hugo"},{yayin_tarihi:1862}]})


#Victor Hugo'nun 1862'den önce yazdığı kitapları getiriniz.
#db.kitap.find({$and:[{yazar_adi:"Victor Hugo"},{yayin_tarihi:{$lte:1865}}]})

# Victor Hugo tarafından yazılan kitapları veya 1866'da yazılan kitapları listeleyiniz
#db.kitap.find({$or:[{yazar_adi:"Victor Hugo"},{yayin_tarihi:1866}]})

# $in: içinde geçenleri getir(eşitlik)
# yazarları  Victor Hugo veya Lev Tolstoy geçenleri getir.
 # db.kitap.find({yazar_adi:{$in:["Victor Hugo","Lev Tolstoy"]}})
 # db.kitap.find({$or:[yazar_adi:"Victor Hugo"},{yayin_tarihi:1866}]})

# belli kolon(field)'ları seçip getirmek istediğimizde find'ın ikinci parametresini kullanabiliriz.
# db.collectionName.find({query},{field(s)})
# 1:getirsin 0:getirsin
# not : _id alanı yazılmadığı sürece listelenir.
#db.kitap.find({},{kitap_adi:1,_id:0})
#db.kitap.find({},{kitap_adi:1,_id:0,yazar_adi:1})


# distinct : tabloda tekrarlayan bir alan varsa bir tanesini getir.
#db.kitap.distinct("yazar_adi")  # [ 'Balzac', 'Dostoyevski', 'Lev Tolstoy', 'Victor Hugo' ]
#db.kitap.distinct("kitap_adi")

# update :bir koşulu sağlayan veriyi güncellemek için kullanılır.
#updateOne/updateMany
db.collectionName.updateOne({query},{$set:{yeni veriler}})

##### !! update ve delete yaparken koşulu doğru vermeyi unutmayınız.
##### yedekleri almayı unutmayınız.
# bu kriterleri sağlayan birden fazla veri de olsa ilk sıradakini değiştirir,kriteri sağlayan tüm verilerde değişiklik isteniyorsa updataMany() kullanılır.
db.kitap.updateOne({kitap_adi:"Suç ve Ceza"},{$set:{kitap_adi:"Suç ve Ceza 1",yayin_tarihi:1890}})

# Delete : deleteOne()deleteMany()
# db.kitap.deleteOne({kitap_adi:"Suç ve Ceza"})
# db.kitap.deleteMany({yazar_adi:"Lev Tolstoy"})


# limit(n) : n sayıda veri getirmek için kullanılır.
# db.kitap.find().limit(3)
#skip(n) : n sayıda veriyi atla demektir.
# db.kitap.find().skip(2)

# sort() :sıralama yapar. 1:asc(küçükten büyüğe)
#                        -1:desc(büyükten küçüğe)
# db.kitap.find().sort({kitap_adi:-1})
# db.kitap.find().sort({kitap_adi:1,yayin_tarihi:-1})

# pretty(): sonucu düzgün göstermek için kullanılabilir.
# sonuna .pretty() yazılmalı.


# aggregate() : join,group by,match vb kodlarla sorgu çekmek için kullanılır.
use northwind
#db.createCollection("categories")
#db.createCollection("products")

'''
db.categories.insertMany(
 [
  {category_code:"TT",category_name:"tatlılar","description:"tatlılar_kategorisi"},
  {category_code:"AY",category_name:"ana yemekler","ana yemekler kategorisi"}
 ])
 
db.products.insertMany(
     [
        {product_name:"Cheesecake",price:80.99,category_code:"TT"},
        {product_name:"Baklava",price:300.99,category_code:"TT"},
        {product_name:"Pilav",price:20.99,category_code:"AY"},
        {product_name:"Hünkar Beğendi",price:120.99,category_code:"AY"},
        {product_name:"Adana Kebap",price:140.99,category_code:"AY"},
     ]
)
'''
#KATEGORİLERE GÖRE ÜRÜN SAYILARINI GETİRİNİZ.
'''
$sum,$avg,$max,min,count...
db.products.aggregate(
[
   { 
      $group:
      {
         _id:"$category_code",
         urun_sayisi:{$count:{} }
      }
   }

])
'''
db.products.aggregate(
[
   {
      $group:
      {
         _id:"$category_code",
         ortalama_fiyati:{$avg:"$price" }
      }
   }

])

# Join : lookup komutuyla kullanılır.
# from : foreign table
# localField : ana tablodaki bağlantılı olan
# foreignField :bağlantılı tablodaki alan
# as: görünmesini istediğiniz ismi
'''
db.products.aggregate(
   [
      {
         $lookup:
         { 
           from:"categories",
           localField:"category_code",
           foreignField:"category_code",
           as:"category"
         
         }
        
      }
   
   ]

)
'''
# category'leri ürünleriyle birlikte listeleyiniz.

'''
db.products.aggregate(
[
        {
            $lookup:
            {
                from:"products",
                localField:"category_code",
                foreignField:"category_code",
                as:"products"
            }
        },
        {
            $project:{category_name:1,"products.product_name":1,_id:0}
        },
        {
            $match:{category_name:"tatlılar"}
        }

]
)

$match : aggregate içinde kriter koymak için kullanılır.

'''

# backup/ restore için mongoDB tools indirmemiz gerekiyor.

# mongodbdump -> backup almak için
# mongodbrestore -> backup'daki verileri db'e aktarmak için
# sorun olursa yönetici modunda çalıştırılır.
# bson : binary json

# pymongo :aracı kütüphanedir.
# sürücü yada aracı bir kütüphanedir.shell de ki kodları burda metot olarak getirlmiştir.
# ikisi arasında bağlantıyı kurmak için kullanacağız.