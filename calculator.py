# kutuphane dahil edildi
import os

#toplama fonksiyonu
def toplama(x,y):
    return x + y
#cıkarma fonksiyonu
def cikarma(x,y):
    return x - y
#bolme fonksiyonu
def bolme(x,y):
    return x / y
#carpma fonksiyonu
def carpma(x,y):
    return x * y

#cmd renk secme adam ister
renk = str(input("Komudunuzu Yazınız: "))
os.system(renk)

#selamla
print ("Selamlar Yapmak İstediğiniz İşlemi Seçiniz")
print("""

1) Toplama
2) Cıkarma
3) Bolme
4) Carpma

""")

#sayıları alma
sayi1 = int(input("Ilk Sayıyı Girin: "))
sayi2 = int(input("Ikinci Sayıyı Girin: "))
#kişi işlem seçer
islem = int(input("Yapmak İsteginiz İşlemi Seçin: "))

#kullanıcı hangi islemi secti sorgula
    # toplama
if islem == 1:
    deger = toplama(sayi1,sayi2)
    print (deger)
    # cikarmasi
elif islem == 2:
    deger = cikarma(sayi1,sayi2)
    print(deger)
    # bolmesi
elif islem == 3:
    deger = bolme(sayi1,sayi2)
    print(deger)
    # carpması
else:
    deger = carpma(sayi1,sayi2)
    print(deger)






