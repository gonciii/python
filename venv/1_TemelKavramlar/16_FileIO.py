#FILE IO(input-output)
#dosya okuma:
# f1=open("olmayanbirdosya.txt")
# print(f1.read()) #FileNotFoundError: [Errno 2] No such file or directory: 'olmayanbirdosya.txt'


# f2=open("ogrenciler.txt",encoding="utf8") #txt.uzantılı dosyayı okuyor
# print(f2.read()) #merhaba dÃ¼nya ! #merhaba dünya !
# f2.close()  # tanımladığımız dosyayı kapatıyoruz. #merhaba dünya1

#dosya içine yazdırma
# f3=open("ogrenciler.txt",mode="w",encoding="utf8")
# f3.write("Hello World!")
# #print(f3.read()) #hata verir.read etme modunda açmadığı için hata verir,oku modunda açtık çünkü.
# f3.close() #Hello World!
#
# #mevcut dosyanın içine ekleme yapmak için a modunda alır.
# #eğer bu dosya adında bir dosya yoksa önce create eder sonra içine yazar.
# f4=open("ogrenciler.txt",mode="a",encoding="utf8")  #ekleme yapıyor.
# f4.write("Merhaba Dünya!")
# f4.close()    #Hello World!Merhaba Dünya!

# ÖRNEK:
#öğrencinin adını,soyadını,dt ve cinsiyetini alarak dict.olarak hazırlayan
#ve geri dönen bir metot yazınız ve bu metottan yararlanarak 3 kişi
#oluşturarak listeye ekleyiniz.Oluşturulan listeyi ogrenciler.txt dosyası içine yazdırıınız.

def ogrenci_ekle(ad,soyad,dt,cinsiyet)-> dict:
    return {
        "ad":ad.capitalize(),
        "soyad":soyad.capitalize(),
        "dogumTarihi":dt,
        "cinsiyet":cinsiyet.upper()
    }

ogrenciler_listesi=[]
ogrenciler_listesi.append(ogrenci_ekle("nur","öztürk","1980","k"))
ogrenciler_listesi.append(ogrenci_ekle("gonca","çomak","1997","k"))
ogrenciler_listesi.append(ogrenci_ekle("ozan",",içcan","1990","e"))
import pprint

print(pprint.pformat(ogrenciler_listesi))
f5=open("ogrenciler.txt","w",encoding="utf8")
f5.write(pprint.pformat(ogrenciler_listesi))
f5.close() #JSON













