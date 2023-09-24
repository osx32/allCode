class Sinif():
    sinif_niteligi=0
    def __init__(self,veri):
        self.veri=veri

    def örnek_methodu(self):
        return self.veri

    @classmethod
    def sinif_metodu(cls):
        return cls.sinif_niteligi

    @staticmethod
    def statik_metot():
        print('merhaba statik metot!')

class Mat():

    @staticmethod
    def pi():
        return 22/7

    @staticmethod
    def karekök(sayi):
        return sayi ** 0.5

    def pi2(self):
        return 22/7

    def karekök2(self,sayi):
        return sayi**0.5






