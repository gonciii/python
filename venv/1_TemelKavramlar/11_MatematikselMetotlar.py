#Mateematiksel Metotlar:
#import math şeklinde tanımlıyoruz.
# import math
# pi_sayisi=math.pi
# print(pi_sayisi)    #3.141592653589793
# # farklı yazım şekli:
# import math as m
# pi_sayisi=m.pi      #(pi,e bunlar sabit değerler,parantez açılmıyor )
# print(pi_sayisi)    #3.141592653589793
#
# e_sayisi=m.e
# print(e_sayisi)  #2.718281828459045
# # --------------------------------------------------
# print(m.inf)
# print(m.nan)
# print(m.tau)     #6.283185307179586

# -------------------------------------------------
# 1-) floor():bir alt tamsayısına yuvarlanmasını sağlar.
# floor içine bir değer alıcak.
import math as m
pi_sayisi=m.pi
print(pi_sayisi)
print(m.floor(pi_sayisi))  #3

# 2-)ceil():bir üst tamsayısına yuvarlanmasını sağlar.
print(m.ceil(pi_sayisi))  #4

# 3-) round():ondalıklı kısmı 50 olan sayılarda çifte yuvarlanma eğilimi vardır.
# yüzden 2.5 ->2'e    3.5->4'e yuvarlanıyor.
print(round(2.51))  #3
print(round(3.49))  #3
print(round(2.5))   #2
print(round(3.5))   #4
print(round(pi_sayisi,3))   #3.142

# min,max,any,sum,len...diğer metotlar

# 4-) fabs():mutlak değer alır.
# negatifleri pozitife çeviriyor.float olarak verdi.
print(m.fabs(-10))   #10.0
print(m.fabs(-10.50)) #10.5

# 5-) pow():power,üs alma işlemi yapar.
# pow içine 2 değer istiyor.  #4**2
karesi=m.pow(4,2)
karesi_tam=int(m.pow(4,2))
print(karesi)     #16.0
print(karesi_tam)  #16
us=m.pow(16,0.5)
print(us)          #4.0 (karekökünü verir.)

# 6-)  sqrt(): karekökünü verir.
print(m.sqrt(16))   #4.0===us=m.pow(16,0.5)

# 7-) fsum(): içindeki değerleri toplar.
# başında f olan float döner.
print(m.fsum([10,12,14,16])) #52.0
print(sum([10,12,14,16]))    #52,içindeki değerlerin en az biri float ise float öner.

# 8-) radians(): radyan cinsine dönüşüm için
r_30=m.radians(30)
print(r_30)   #0.5235987755982988
# 9-) sin,cos,tan :parametre olarak radyan cinsinden değer alır
# print(m.sin(30)) #tam değer vermez
print(m.cos(m.radians(180)))  #-1.0

# 10-) degree(): derece cinsine çevirir.
print(m.degrees(r_30))    #29.999999999999996
# 11-) factorial(): faktöriyel döner.
print(m.factorial(6))  #720
# 12-) exp(): e sayısının üssünü alır.
print(m.exp(2))     #7.38905609893065
# 13-) isnan(): float ya da int değer alır. #NaN:not a number
print(m.isnan(10))  #false
print(m.isnan(m.nan)) #true





