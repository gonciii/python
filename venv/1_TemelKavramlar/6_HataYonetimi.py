#Hata yönetimi (exception handling)
'''
HATA TİPLERİ:
1.Syntax (sözdizimi) Hataları:
Python'da kod yazarrken uyulması gereken syntax'da uyulmadığında oluşan hatalardır.
Programı çalıştırdığınızda console'da satır numarası ve hata mesajıyla birlikte hata görünür ancak program çalışmaz.
'''
# var sayi=10  ->syntax hatası  ->>var_sayi=10
#   sayi=10  ---> boşluk hatası

'''
2.Çalışma zamanı hataları (runtime expection)
syntax hatası yoktur,ancak uygulama çalışırken yönetilmemiş ve beklenmeyen hatalar oluşabilir.
'''
# sayi1=10
# sayi2=input("sayi2 girin")
# toplam=sayi1+sayi2  ##### (stringler string dışındaki veri tipi ile + işaretiyle toplanamaz.)

'''
try:
    #hata almasını beklediğiniz kodlar bu blokta yazılır.
except:(required)zorunlu
    #yukarıdaki kodda bir hata oluşursa bu bloğa düşer.
finally: (optional) opsiyonal
    #hata oluşsa da oluşmasa da bu blok çalışır.

'''
# try:
#     sayi1=10
#     # sayi2==int(input("sayi2 giriniz")) bu düzgün çalışır.
#     sayi2=input("sayi2 giriniz") #excepte düşer
#     toplam=sayi1+sayi2
#     print(toplam)
# except:
#     print("beklenmeyen bir hata oluştu.")
# finally:
#     print("yeniden deneyebilirsiniz")

# typo:yazım denetimi hata değildir.

# sınıflar ilki büyük harfle yazılır Exception bir sınıf örneğidir.Exception genel olarak bütün hataları kapsıyor:syntax olabilir,file hatası olabilir.
try:
    file=open("böylebirdosyayok.txt")
except FileNotFoundError as fnex:
    print(f"Bir hata oluştu.hata mesajı:{fnex.strerror}, hatalı dosya adı:{fnex.filename}")
except FileExistsError as fex:
    print(f"Bu dosyadan bir tane daha var.Mesaj:{fex.strerror} Hatalı dosya adı:  {fex.filename}")
except Exception as ex :
    print(f"Beklenmedik bir hata:{ex.args[1]}")

'''
3.MANTIKSAL HATALAR(LOGİCAL EXCEPTİONS)
Developer hatasıdır,bulunması zordur.
bki=kilo/(boy*2) --->burada karesi alınmak istenirken 2 ile çarpılmış bir mantıksal hata elde edilir.
DEBUG yaparak adım adım kod incelenir ve hata bulunmaya çalışılır.
DEBUG: program çalışırken adım adım kodu ilerletmek demektir.
Debug yaparken:
1.break point eklenir.(kodun sol tarafına line number'ın hemen sağına tıklayınız.)
2.projeyi debug modda çalıştırın.(alt +f5)
3.kod break pointe düştükten sonra f10 ile adım adım ilerleyebiliriz
'''
# boy=1.6
# kilo=78
# bki=kilo/(boy*2) #burada karesi alınmak istenirken 2 ile çarpılmış bir mantıksal hata elde edilir.
# print(bki)


##Hata fırlatma:  raise exception ("mesaj")
# try:
#     vize = float(input("vize notunu giriniz:"))
#     if not (vize >=0 or vize <=100):
#         raise Exception("0 ile 100 aralığında değer girilebilir.")
#     vize_agırlık=vize*0.4
#     print(vize_agırlık)
# except ValueError as ve:
#     print("Lütfen sayısal bir değer giriniz.")
# except Exception as ex:
#     print(ex)

