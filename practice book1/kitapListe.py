liste=[('79456412321','Greenberg','Sana Gül Bahçesi Vadetmedim','Metis'),
       ('3214556489','Evren','Postmodern Bir Kız Sevdim','İthaki'),
       ('456138721','Nietzsche','Böyle Buyurdu Zerdüşt','Cem')]

class Sorgu():
    def __init__(self,deger=None,sira=None):
        self.liste=[('79456412321','Greenberg','Sana Gül Bahçesi Vadetmedim','Metis'),
       ('3214556489','Evren','Postmodern Bir Kız Sevdim','İthaki'),
       ('456138721','Nietzsche','Böyle Buyurdu Zerdüşt','Cem')]

        if not deger and not sira:
            l=self.liste
        else:
            l=[li for li in self.liste if deger==li[sira]]

        for i in l:
            print(*i,sep=',')

    @classmethod
    def isbnden(cls,isbn):
        cls(isbn,0)

    @classmethod
    def yazardan(cls,yazar):
        cls(yazar,1)

    @classmethod
    def eserden(cls,eser):
        cls(eser,2)

    @classmethod
    def yayinevinden(cls,yayinevi):
        cls(yayinevi,3)












"""class Sorgu():
    def __init__(self):
        self.liste=[('79456412321','Greenberg','Sana Gül Bahçesi Vadetmedim','Metis'),
       ('3214556489','Evren','Postmodern Bir Kız Sevdim','İthaki'),
       ('456138721','Nietzsche','Böyle Buyurdu Zerdüşt','Cem')]

    def bul(self,deger,sira):
        return[li for li in self.liste if deger==li[sira]]

    def sorgula(self,ölcüt=None,deger=None):
        d={'isbn':self.bul(deger,0),
           'yazar':self.bul(deger,1),
           'eser':self.bul(deger,2),
           'yayinevi':self.bul(deger,3)
           }
        for oge in d.get(ölcüt,self.liste):
            print(*oge,sep=',')
"""







"""def sorgula(ölcüt=None,deger=None):
    for li in liste:
        if not ölcüt and not deger:
            print(*li,sep=',')
        elif ölcüt=='isbn':
            if deger==li[0]:
                print(*li,sep=',')

        elif ölcüt=='yazar':
            if deger==li[1]:
                print(*li,sep=',')

        elif ölcüt=='eser':
            if deger==li[2]:
                print(*li,sep=',')

        elif ölcüt=='yayinevi':
            if deger==li[3]:
                print(*li,sep=',')
"""

"""
def sorgula(ölcüt=None,deger=None):
    d={'isbn':[li for li in liste if deger==li[0]],
       'yazar':[li for li in liste if deger==li[1]],
       'eser':[li for li in liste if deger==li[2]],
       'yayinevi':[li for li in liste if deger==li[3]]
        }
    for oge in d.get(ölcüt,liste):
        print(*oge,sep=',')
"""

"""def bul(deger,sira):
    return [li for li in liste if deger==li[sira]]

def sorgula(olcut=None,deger=None):
    d={'isbn':bul(deger,0),
        'yazar':bul(deger,1),
        'eser':bul(deger,2),
        'yayinevi':bul(deger,3)
       }

    for oge in d.get(olcut,liste):
        print(*oge,sep=',')
"""
