#import basitOyun
#import calisan
#from calisan2 import *
#import gizliUyeler
#import harfSay
#from kitapListe import *
#import oyuncular
#import program
#import sınıflar
#import siparis
#import statikmetodlar
#import tarih



"""
gofret=siparis.Siparis()
gofret.firma='Eti'
gofret.miktar=1000


ahmet=calisan.Calisan('Ahmet')
mehmet=calisan.Calisan('Mehmet')
ayse=calisan.Calisan('Ayse')
calisan.Calisan.personel_sayisini_görüntüle()
ahmet.personel_sayisini_görüntüle()
"""


"""#sınıf niteligi icin sınıfın kendisi cagrilir
print(calisan.Calisan.kabiliyetleri)

#sınıfın bir ÖRNEĞİNİN niteligini kullanabilmek icin __init__ metodu gerekir cünkü  init'te kullanılan self Calisan sinifina degil Calisan clasindan türetilen örnege isaret eder
#yani degiskenin bicimini Calisan belirler ama icindekini özel kullanim icin türetilen örnek belirler yani kabiliyetin bir liste oldugunu Calisan söyler ama icindeki bilgiyi
#almak zorunda degildir o yüzden self ile cagrilirsa ahmet'in kendi atadigi kabiliyet bilgisi gösterilir
print(ahmet.kabiliyetleri)
"""


"""
kitapListe.sorgula('isbn','79456412321')
kitapListe.sorgula('isbn','3214556489')
kitapListe.sorgula('isbn','456138721')
kitapListe.sorgula('yayinevi','Cem')
kitapListesi.sorgula('yayinevi','Cem')
kitapListesi.sorgula('yazar','Evren')
"""

"""
Sorgu.isbnden("79456412321")
Sorgu.eserden('Böyle Buyurdu Zerdüşt')
Sorgu.yazardan('Nietzsche')
hepsi=Sorgu()
"""

"""
sınıflar.Siniförnekler.tcknden()
deger=sınıflar.Siniförnekler()


print(tarih.bugün)
"""

"""
m=statikmetodlar.Mat()
print(m.pi())
print(m.karekök(25))
print(statikmetodlar.Mat.pi())
print(statikmetodlar.Mat.karekök(25))

statikmetodlar.Mat.pi2()


snf=sınıflar.Siniförnekler()
print(dir(snf))
"""


"""
#Oyuncular
siz=basitOyun.Oyuncu('Ahmet')
rakip=basitOyun.Oyuncu('Mehmet')

#Oyun Baslangici
while True:
    print('Su anda rakibinizle karsi karsiyasiniz.',
          'Yapmak istediginiz hamle: ',
          'Saldir: s',
          'Kac:    k',
          'Cik:    q',sep='\n',
          )
    hamle=input('\n> ')
    if hamle=='s':
        siz.saldir(rakip)
        print('Rakibinizin durumu')
        rakip.mevcut_durumu_görüntüle()
        print('Sizin durumunuz')
        siz.mevcut_durumu_görüntüle()

    if hamle=='k':
        siz.kac()

    if hamle=='q':
        siz.oyundan_cik()
"""



"""
c1=Calisan2('Ahmet')
c2=Calisan2('Mehmet')
c3=Calisan2('Selim')
Calisan2.personeli_görüntüle()
c1.isim='Kaan'
Calisan2.personeli_görüntüle()


program1=program.Program()
program1.sayi=5
print(program1.sayi)



asker1=oyuncular.Asker('Ahmet','Er')
isci1=oyuncular.Isci('Mehmet','Usta')
yonetici1=oyuncular.Yonetici('Selim','Mudur')
print(asker1.rutbe)
print(asker1.guc)
print(asker1.isim)
"""















