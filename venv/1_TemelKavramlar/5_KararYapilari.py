# # Karar Yapıları
# # if-else
# # if :verilen koşul True ise ise çalışıcak blok,else: False ise çalışıcak blok
# '''
# if kosul:
#     True iken yapılacak işlemler
#
#
#
# if kosul:
#     True iken yapılacak işlemler
# else :
#     False iken yapılacak işlemler
# 1 girinti =1 tab
# '''
#
# kullanici_adi = input("Kullanıcı adınızı giriniz:").lower()
# if kullanici_adi == "bilgeadam":
#     print("Hoşgeldiniz!")
# else:
#     print("lütfen kullanıcı adını kontrol ediniz.")
#
# '''
# if kosul1:
#    kosul1 True ise yapılacaklar
# elif kosul2:
#    kosul2 True ise yapılacaklar
# elif kosul3:
#    kosul3 True ise yapılacaklar
# else:
#     hiç bir koşul True değilse
# '''
#region Girilen bir sayının negatif/pozitif olması durumunu kontrol ediniz.ve ekranda durumunu gösteriniz.
# cast=convert
# sayi1 = int(input("Bir sayı giriniz:"))
# if (sayi1 < 0):
#     print("Girdiğiniz sayı negatiftir.")
# elif (sayi1 > 0):
#     print("Girdiğiniz sayı pozitiftir.")
# elif (sayi1 == 0):
#     print("Girdiğiniz sayı 0 eşittir.")
# else:
#     print("başka bir sayı giriniz")
#endregion

# girilen_sayi = int(input("Bir sayı giriniz"))
# if girilen_sayi > 0:
#     print(f"{girilen_sayi} sayısı pozitiftir.")
# elif girilen_sayi == 0:
#     print(f"{girilen_sayi} sayısı sıfırdır.")
# else:
#     print(f"{girilen_sayi} sayısı negatiftir.")

#region Girilen bir sayının çift/tek olmasını bulunuz ve ekrana yazdrınız.

# sayi1 = int(input("Bir sayı giriniz:"))
# if sayi1%2==0:
#     print(f"{sayi1} sayısı çifttir.")
# else:
#     print(f"{sayi1} sayısı tektir.")
# #endregion

#region Girilen bir x sayısının,yine kullaıcıdan istenen bir y sayısına tam bölünüp bölünmediğini kontrol ediniz ve ekranda göteriniz.

# sayi1 = int((input("Bir sayı giriniz:")))
# sayi2 = int((input("İkinci sayıyı giriniz:")))
# if sayi2 == 0:
#     print("Lütfen 0 dışında bir sayı giriniz.")
# else:
#     islem = sayi1 % sayi2
#     if islem == 0:
#         print(f"{sayi1},{sayi2}'in tam katıdır.")
#     else:
#         print(f"{sayi1}'in,{sayi2}'e bölümünden kalan {islem}'dir.")
#endregion

# Girilen iki sayıdan hangisinin büyük olduğunu bulan uygulamayı yazınız.
# sayi1 = int(input("Birinci sayıyı giriniz:"))
# sayi2 = int(input("İkinci sayıyı giriniz:"))
# if (sayi1 > sayi2):
#     print(f"{sayi1} büyüktür.")
# elif (sayi1 < sayi2):
#     print(f"{sayi1},küçüktür.")
# else:
#     print("sayılar biribine eşittir")

# Girilen vize notunun 0-100 arasında olmasını kontrol ediniz.eğer doğru giriş yapıldıysa giriş başarılı uyarsını gösterelim.eğer ortalama 50 ve üzerinde ise geçti değilse kaldı yazdıralım.
# veya kısaca
# if 0 <= vize <=100 and 0<= final <=100)

vize_notu = float(input("Vize notunuzu giriniz:"))
final_notu=float(input("Final notunu giriniz:"))
if (vize_notu >=0 and vize_notu <= 100) and (final_notu >=0 and final_notu <=100 ) :
    print("giriş başarılıdır.")
    ortalama=(vize_notu * 0.4)+(final_notu * 0.6 )
    print(f"ortalamanız:{ortalama}")
    if (ortalama > 50):
        print("not geçerlidir.")
    else:
        print("not geçersizdir.")

else:
    print("lütfen 0-100 aralığında bir sayı giriniz")

