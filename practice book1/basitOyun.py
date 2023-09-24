import time,random,sys

class Oyuncu():
    def __init__(self,isim,can=5,enerji=100):
        self.isim=isim
        self.darbe=0
        self.can=can
        self.enerji=enerji

    def mevcut_durumu_görüntüle(self):
        print('darbe: ',self.darbe)
        print('can: ',self.can)
        print('enerji: ',self.enerji)

    def saldir(self,rakip):
        print('Bir saldiri gerceklestirdiniz.')
        print('Saldiri sürüyor. Bekleyiniz.')

        for i in range(10):
            time.sleep(.3)
            print('.',end='',flush=True)

            sonuc=self.saldiri_sonucunu_hesapla()
        if sonuc==0:
            print('\nSONUC: kazanan taraf yok')

        if sonuc==1:
            print('\nSONUC: rakibinizi darbelediniz')
            self.darbele(rakip)

        if sonuc==2:
            print('\nSONUC: rakibinizden darbe aldiniz')
            self.darbele(self)

    def saldiri_sonucunu_hesapla(self):
        return random.randint(0,2)

    def kac(self):
        print('Kaciliyor....')
        for i in range(10):
            time.sleep(.3)
            print('\n',flush=True)

        print('Rakibiniz sizi yakaladi')

    def darbele(self,darbelenen):
        darbelenen.darbe+=1
        darbelenen.enerji-=1
        if darbelenen.darbe%5==0:
            darbelenen.can-=1
        if darbelenen.can<1:
            darbelenen.enerji=0
            print('Oyuncu {} kazandi!'.format(self.isim))
            self.oyundan_cik()

    def oyundan_cik(self):
        print('Cikiliyor...')
        sys.exit()














