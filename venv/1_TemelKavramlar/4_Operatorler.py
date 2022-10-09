#Operatörler
#1.Aritmetik operatorler
#+ - * /
#**:üs almak için kullanılır.
#//:bölümdeki tam kısmı verir.
#%:mod işlemi (bölümden kalanı verir)

sayi1=10
sayi2=2
us=sayi1**sayi2
print(us)

tam_kisim=sayi1//sayi2
print(tam_kisim)

mod=sayi1%sayi2
print(mod)

# 2.Atama Operatorleri
# = :sağdaki değeri soldaki değişkene atar.
# bileşik atama operatörleri
# +=:
# -=:
# *=:
# /=:
# %=:
sayi1=sayi1+10
sayi1 +=10

# 3.Mantıksal Operatörler
# 3.1.Karşılaştırma Operatörleri
# iki ve ya daha fazla değeri birbiri ile karşılaştırmak için kullanılır.
# == :eşit mi? demek anlamına gelir
s1=(sayi1==sayi2)
print(s1)  #False
# != :eşit değil mi?
s2=(sayi1!=sayi2)
print(s2) #True
# >: büyük mü ?
# <: küçük mü?
s3=(sayi1>sayi2)
print(s3) #True
s4=(sayi1<sayi2)
print(s4) #False

#  >= :büyük  ve ya eşit mi?
# <=  :küçük ve ya eşit mi?

# 3.2 Mantıksal Operatörler
# and: her bir karşılaştırma sonucunun true olması durumunda true döner aksi olduğundan false döner.
# or:  herhangi bir karşılaştırma sonucunun true olması durumunda true ,tüm önermeler false ise false döner.
# vize ve final notları için :vize 40'ın üzerindeyse ve final 50 veya üzerinde olmalı.
vize=10
final=50
sonuc=(vize>40) and (final>=50)
print(sonuc) #False

# title='mrs'(kadın),'ms'(kadın),'mr'(erkek)
# title bilgisi kullanıcıdan alınacak yukarıdaki değerlerden biri gelecek ve title'ın kadın olması durumu kontrol edilmeli.
title=input("Title giriniz")
sonuc1=(title=='mrs') or (title=='ms')
print(sonuc1)

# not : mevcut sonucunun değilini alır.
sonuc2=not(vize> 40 and  final>=50)
print(sonuc2) #True



