
class Siniförnekler():
    """sinif_niteligi=0

    def __init__(self,param1,param2):
        self.param1=param1
        self.param2=param2
        self.örnek_niteligi=0

    def örnek_metodu(self):
        self.örnek_niteligi+=1
        return self.örnek_niteligi

    @classmethod
    def sinif_metodu(cls):
        cls.sinif_niteligi+=1
        return cls.sinif_niteligi
    """

    """
    def __init__(self,mesaj='Müsteri numaraniz: '):
        cevap=input(mesaj)
        print('Hosgeldiniz')

    @classmethod
    def paroladan(snf):
        mesaj='Lütfen parolanizi giriniz: '
        snf(mesaj)

    @classmethod
    def tcknden(snf):
        mesaj='Lütfen TC kimlik numaranizi giriniz: '
        snf(mesaj)

    """

    sinif_niteligi='sinif niteligi'
    def __init__(self):
        self.örnek_niteligi='örnek niteligi'

    def örnek_metodu(self):
        print('örnek metodu')

    @classmethod
    def sinif_metot(cls):
        print('sinif metodu')

    @staticmethod
    def statik_metot():
        print('statik metod')























