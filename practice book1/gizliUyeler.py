class Sinif_Gizli():
    __gizli='gizli'
    _yari_gizli='yari gizli' #yani herhangi bir fazladan özelligi yok sadece _ isareti class disinda kullanmasini istenmedigini söylüyor#

    def ornek_metodu(self):
        print(self.__gizli)
        print(self.__miraba)
        print('ornek metodu')

    @classmethod
    def sinif_metodu(cls):
        print('sinif metodu')


    @staticmethod
    def statik_metodu():
        print('statik metod')

