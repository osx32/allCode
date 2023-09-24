class Oyuncu:
    def __init__(self,isim,rutbe):
        self.isim=isim
        self.rutbe=rutbe
        self.guc=0

    def hareket_et(self):
        print('hareket ediliyor...')

    def puan_kazan(self):
        print('puan kazanildi')

    def puan_kaybet(self):
        print('puan kaybedildi')



class Asker(Oyuncu):
    def __init__(self,*args):
        super().__init__(*args)
        self.guc=100

    def hareket_et(self):
        super().hareket_et()
        print('hedefe ulasildi.')


class Isci(Oyuncu):
    def __init__(self,*args):
        super().__init__(*args)
        self.guc=70


class Yonetici(Oyuncu):
    def __init__(self,*args):
        super().__init__(*args)
        self.guc=20











