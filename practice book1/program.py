class Program:
    def __init__(self):
        self._sayi=0

    @property
    def sayi(self):
        return self._sayi

    @sayi.setter
    def sayi(self,yeni_deger):
        if yeni_deger%2==0:
            self._sayi=yeni_deger
        else:
            print('cift degil!')

        return self.sayi

    @sayi.deleter
    def sayi(self):
        del self._sayi






