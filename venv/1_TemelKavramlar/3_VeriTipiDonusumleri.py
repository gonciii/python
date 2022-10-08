# # Veri Tipi Dönüşümleri
# print("19"+"21")#1921  str+str
# print(19.0+21)#int+int,int+float
# #str+int hata verir.
# # print("19"+21)
#
# m1=str(19)
# s1=int("10") #10
# print(s1)
# print("10")
# type() :parametre olarak içerisindeki değerin veri tipini döner.
# print(type(m1))#str
# print(type(s1)) #int
# print(type("10")) #str
# input():dışarıdan bilgi almak için kullanılan metottur.
# sayi=input("Bir sayı giriniz:")
# print(sayi)

# dışarıdan gelen bilgiler string olarak gelir.
# kullanıcıdan alınan bir sayının karesini bulan ve ekranda gösteren uygulamayı yazınız.

# str_girilen_sayi=input("bir sayı giriniz:")
# sayi=int(str_girilen_sayi)
# karesi=sayi*sayi
# print(f"Girilen sayının karesi:{karesi}")

# sayi=int(input("Bir sayı giriniz:")
# print(f"Girilen sayının karesi:{sayi*sayi}")

# vize1_puanı=input("vize notunuzu giriniz")
# final_puanı=input("final notunuzu giriniz")
# vize=float(vize1_puanı)
# final=float(final_puanı)
# vize=(vize*40)/100
# final=(final*60)/100
# print(f"vize ve finalin ortalamasını gösteriniz:{vize+final}")

# kullanıcının adını ve soyadını alarak ad.soyad@bilgeadamakademi.com şeklinde bir mail adresi oluşturan ve gösteren uygulamayı yazınız.

ad=str(input("Adınızı giriniz:"))
soyadı=str(input("Soyadınızı giriniz:"))
mail_adresi=f"{ad}.{soyadı}@bilgeadamakademicom".lower().replace('ç',"c")
print(mail_adresi)


