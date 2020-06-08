class obywatel:
    def __init__(self,pesel,imie,nazwisko,dataUrodzenia,adres,stan,nrTelefonu=False):
        self.__pesel=pesel
        self.__imie=imie
        self.__nazwisko=nazwisko
        self.__dataUrodzenia=dataUrodzenia
        self.__adres=adres
        self.__stan=stan
        self.__nrTelefonu=nrTelefonu
class adres:
    def __init__(self,miasto,ulica,numerDomu,numerLokalu,kodPocztowy):
        self.__miasto=miasto
        self.__ulica=ulica
        self.__numerDomu=numerDomu
        self.__numerLokalu=numerLokalu
        self.__kodPocztowy=kodPocztowy
class sklep:
    def __init__(self,id,nazwa,adres,peselWlasciciela):
        self.__id=id
        self.__nazwa=nazwa
        self.__adres=adres
        self.__peselWlasciciela=peselWlasciciela
class rachunek:
    def __init__(self,idRachunku,idSklepu,peselKlienta,data):
        self.__idRachunku=idRachunku
        self.__idSklepu=idSklepu
        self.__peselKlienta=peselKlienta
        self.__data=data
class zakup:
    def __init__(self,idKupna,idSklepu,substancja,ilosc,dataKupna):
        self.__idKupna=idKupna
        self.__idSklepu=idSklepu
        self.__substancja=substancja
        self.__ilosc=ilosc
        self.__dataKupna=dataKupna