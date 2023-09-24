class Calisan():
    __personel=[]

    def __init__(self,isim):
        self.isim=isim
        self.kabiliyetleri=[]
        self.__personele_ekle()

    @classmethod
    def personel_sayisini_görüntüle(cls):
        print(len(cls.__personel))

    def __personele_ekle(self):
        self.__personel.append(self.isim)
        print("{} adli kisi personele eklendi".format(self.isim))

    @classmethod
    def personeli_görüntüle(cls):
        print("Personel listesi:")
        for kisi in cls.__personel:
            print(kisi)

    def kabiliyet_ekle(self,kabiliyet):
        self.kabiliyetleri.append(kabiliyet)

    def kabiliyetleri_görüntüle(self):
        print("{} adli kisinin kabiliyetleri:".format(self.isim))
        for kabiliyet in self.kabiliyetleri:
            print(kabiliyet)














