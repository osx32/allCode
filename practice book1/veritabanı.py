import sqlite3
veritabani=sqlite3.connect("kutuphane.sqlite")
#veritabani.row_factory=sqlite3.Row
imlec=veritabani.cursor()
#imlec.execute("SELECT * FROM Kitap")
#veriler=imlec.fetchall()
#for veri in veriler:
#    print("Kitap adı:",veri["KitapAdi"],"Yazar adı:",veri["YazarAdi"])

"""
imlec.execute("CREATE TABLE IF NOT EXISTS Kitap(KitapAdi TEXT, YazarAdi TEXT, BasimYili INTEGER)")
imlec.execute("INSERT INTO Kitap(KitapAdi, YazarAdi, BasimYili) VALUES('Python3', 'Onur SEVLİ', 2018)")
imlec.execute("INSERT INTO Kitap VALUES('Her Yönüyle Python', 'Fırat ÖZGÜL', 2013)")
imlec.execute("INSERT INTO Kitap VALUES('Suc ve Ceza', 'Dostoyevski', 1991)")
imlec.execute("INSERT INTO Kitap VALUES('Vadideki Zambak', 'Balzac', 1983)")

kitaplar=[("Sefiller", "Victor Hugo", 1950),
          ("İki Şehrin Hikayesi", "Charles Dickens", 1963)]

for k in kitaplar:
    imlec.execute("INSERT INTO Kitap VALUES(?,?,?)",k)

imlec.execute("UPDATE Kitap SET KitapAdi='Python Programlama'")


imlec.execute("UPDATE Kitap SET BasimYili=2017 WHERE KitapAdi='Python 3'")

imlec.execute("UPDATE Kitap SET KitapAdi='Python Programlama Rehberi' WHERE YazarAdi='Onur SEVLİ' AND BasimYili=2017")
imlec.execute("UPDATE Kitap SET KitapAdi='Python Programlama Rehberi' WHERE YazarAdi='Onur SEVLİ' OR YazarAdi='Fırat ÖZGÜL'")

imlec.execute("DELETE FROM Kitap WHERE KitapAdi='Python Programlama Rehberi'")
imlec.execute("DELETE FROM Kitap WHERE YazarAdi='Balzac'")
"""

#imlec.execute("SELECT KitapAdi, YazarAdi, BasimYili FROM Kitap WHERE BasimYili>2011")
imlec.execute("SELECT * FROM Kitap")
#imlec.execute("SELECT * FROM Kitap WHERE BasimYili=2015")

#sonuc=imlec.fetchall()
#print(sonuc)
#print(type(sonuc))

#sonuc=imlec.fetchall()
#for s in sonuc:
#print(s[0])

#sonuc=imlec.fetchone()
#print(imlec.fetchone())
#print(imlec.fetchone())

#veriler=imlec.fetchmany(3)
#for veri in veriler:
#    print(veri)

#for veri in imlec:
#    print(veri)



#veritabani.commit()
veritabani.close()