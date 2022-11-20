#SCOPE : (KAPSAM)
'''
#kavramlar:

#Global:pythonda oluşturulan bir değişkenin her alandan erişebilir olduğunu anlatır.
ad="nur" #global değişkenn

#Local: fonksiyonların içinde tanımlanan değişkenler
def  fun():
     sayi=10  #local
print(sayi) #NameError:name 'sayi' is not defined

#Enclosing:
def func1():
    a=10 #enclosing

    def func2():
       b=20  #local

#Built-in: print(),len(),sum(),True-False,None,int(),str()
import etmeye gerek kalmıyor. print()
'''
#Değer değiştirme:
#global ve nonlocal keywords:
#global anahtar kelimesi:globalde tanımlanan bir değişkenin değeri bir
#fonksiyon içinde değiştirmek için kullanılır.
#değişken içinde değişken tanımlanıyorsa aslında local oluyor.
#değiştirmek istediğimizde globalde tanımlanmış olan fonskiyonu local anahtar kelimesi ile değiştirebiliriz.


sayi1=10    #global değişken
def func():
    global sayi1
    sayi1=100
    sayi2=20       #local değişken
    print(sayi1)   #100
    print(sayi2)   #20

# func()
# print(sayi1)  #10 globalden sonra #100 oluyor.

#Nonlocal: global keyword gibidir.
#İç içe fonksiyonlarda içteki func. içinden bir dıştaki func.değişkeni değiştirmek için kullanılır.


def func1():
    s1=10
    print(s1)     #10
    def func2():
        nonlocal s1
        s1=100
        s2=50
        print(s1)   #100
        print(s2)   #50

    func2()
    print(s1)    #100

func1()