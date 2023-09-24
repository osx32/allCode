import sqlite3
veritabani=sqlite3.connect(":memory:")

imlec=veritabani.cursor()

imlec.execute("CREATE TABLE IF NOT EXISTS Kayitlar(Ad TEXT, Soyad TEXT, Numara INTEGER)")

imlec.execute("INSERT INTO Kayitlar VALUES('Leyla','Gunes', 123)")
imlec.execute("INSERT INTO Kayitlar VALUES('Ayhan', 'Aydın', 465)")

veritabani.commit()

imlec.execute("SELECT * FROM Kayitlar")

for kayit in imlec:
    print(kayit)
