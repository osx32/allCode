class Calisan2:
    _personel=[]

    def __init__(self,isim):
        self._isim=isim
        self.personel_ekle()

    def personel_ekle(self):
        self.personel.append(self.isim)
        print('{} adli kisi personele eklendi'.format(self._isim))

    @classmethod
    def personeli_görüntüle(cls):
        print('Personel listesi:')
        for kisi in cls._personel:
            print(kisi)

    @property
    def isim(self):
        return self._isim

    @isim.setter
    def isim(self,yeni_isim):
        kisi=self._personel.index(self.isim)
        self._personel[kisi]=yeni_isim
        print('yeni isim: ',yeni_isim)




