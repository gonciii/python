#String Metorları:
# String karakterler dizisidir.
# harf="g" #string
# yazi="merhaba dünya" #string

# not="lorem ipsum"
metin="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tristique justo ante, at fringilla libero imperdiet non. Curabitur porta magna quis facilisis facilisis. Nunc suscipit nisi tristique leo malesuada sodales. Sed in facilisis nibh, vitae porttitor enim. Sed eget justo hendrerit, cursus magna ultrices, vestibulum urna. Sed nec sem nibh. Fusce urna sapien, congue at rutrum ut, fringilla finibus libero. Praesent ut ex ut velit pellentesque vestibulum eget non quam. Phasellus at lacinia felis. Sed euismod arcu vitae congue mattis. Duis eget interdum sem."
print(len(metin)) #571
print(metin.lower())
print(metin.upper())
print(metin.count("a")) #34
print(metin.capitalize()) #metnin ilk harfini büyütür.
print(metin.startswith("lorem")) #arama yaparken büyük küçük harf duyarlılığı vardır.
print(metin.endswith(".")) #metnin sonundakini arıyor.
print(metin.find("abc")) #-1:metin içinde aranılan değer bulunamazsa döner,bulunursa bulunduğu index döner
print(metin.find("sit")) #18.index boşluklar ve semboller de sayılır.
# stringlerde de index 0'dan başlar.

#print(metin.index("abc")) #ValueError: substring not found

print(metin.replace("a","e"))
print(metin.replace("lorem","totem"))

ayrilmis_liste=metin.split('.')
print(ayrilmis_liste)
print(len(ayrilmis_liste))

mailler="nur.ozturk@bilgeadam.com;ahmet.ata@bilgeadam.com;sema.yilmaz@bilgeadam.com"
mail_liste=mailler.split(";")
print(mail_liste)
print(mailler.replace(";","").split("@bilgeadam.com"))

print(metin.title()) #her kelimenin ilk harfini büyütür.
# Örnek:
# girilen=input("Bir sayı giriniz:")
# if girilen.isdigit():
#     print("sayısal hale dönüştürülebilir.")
#     sayi=int(girilen)
# else:
#     print("metin içinde harf ve ya sembol var.")
#
# print(girilen.isalnum()) #alpha:sadece harfler #numeric:sadece rakamlar #semboller gelirse false döner.
# #abc veya 123 veya abc123 ise True
# print(girilen.isalpha())
# print(girilen.isascii()) #metnin tümü ascii tablosunda ise True,değilse false ; ö,ç,ü,ğ,ş,ı,

mail_listesi=["nur.ozturk@bilgeadam.com","sema.yılmaz@bilgeadam.com"]
print(';'.join(mail_listesi)) #nur.ozturk@bilgeadam.com;sema.yılmaz@bilgeadam.com

print("merhaba dünya".center(30,"*")) #********merhaba dünya*********
print("merhaba dünya".center(20,"-")) #---merhaba dünya----
""