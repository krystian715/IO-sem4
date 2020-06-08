import  PyQt5.QtWidgets as qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
class wyszukiwanie(QDialog):
    def __init__(self):
        super().__init__()
        self.uklad_Wyszukiwania=qt.QGridLayout()
        self.setWindowTitle("Wyszkiwanie danych o Obywatelu")
        self.Pesel = QLineEdit() 
        self.Pesel_tekst=qt.QLabel("Podaj PESEL")  
        self.msg=qt.QMessageBox()
        self.wroc=QPushButton('OK')
        self.tekst=qt.QLabel()
        self.ok = qt.QPushButton("OK")
        self.ok.clicked.connect(self.accept)
        self.uklad_Wyszukiwania.addWidget(self.Pesel_tekst,0,0)
        self.uklad_Wyszukiwania.addWidget(self.Pesel,1,0)
        self.uklad_Wyszukiwania.addWidget(self.ok,2,0)
        self.uklad_Wyszukiwania.addWidget(self.tekst,3,0)
        self.setLayout(self.uklad_Wyszukiwania) 
class okno_Wyswietlania(QDialog):
    def __init__(self,pesel,imie,nazwisko,dataUrodzenia,stan,nr_telefonu,miasto,ulica,numerDomu,numerLokalu,kodPocztowy):
        super().__init__()       
        self.uklad_Wyswietlania=qt.QGridLayout()
        self.setWindowTitle("Wyswietlanie danych")
        self.Pesel=qt.QLabel(pesel)
        self.Imie=qt.QLabel(imie)
        self.Nazwisko=qt.QLabel(nazwisko)
        self.dataUrodzenia=qt.QLabel(dataUrodzenia)
        self.stan=qt.QLabel(stan)
        self.Peseltekst=qt.QLabel('Pesel')
        self.Imietekst=qt.QLabel('Imie')
        self.Nazwiskotekst=qt.QLabel('Nazwisko')
        self.dataUrodzeniatekst=qt.QLabel('Data urodzenia')
        self.stantekst=qt.QLabel('Stan')
        self.nrTelefonutekst=qt.QLabel('Numer telefonu')
        if nr_telefonu==False:
            self.nrTelefonu=qt.QLabel('brak')
        else:
            self.nrTelefonu=qt.QLabel(nr_telefonu)       
        self.miasto=qt.QLabel(miasto)
        if ulica==None:
            self.ulica=qt.QLabel('Brak')
        else:
            self.ulica=qt.QLabel(ulica)
        if numerDomu==None:
            self.numerDomu=qt.QLabel('Brak')
        else:
            self.numerDomu=qt.QLabel(numerDomu)
        if numerLokalu==None:
            self.numerLokalu=qt.QLabel('Brak')
        else:
            self.numerLokalu=qt.QLabel(numerLokalu)
        self.kodPocztowy=qt.QLabel(kodPocztowy)
        self.miastotekst=qt.QLabel('Miasto')
        self.ulicatekst=qt.QLabel('Ulica')
        self.numerDomutekst=qt.QLabel('Numer domu')
        self.numerLokalutekst=qt.QLabel('Numer lokalu')
        self.kodPocztowytekst=qt.QLabel('Kod pocztowy')
        self.uklad_Wyswietlania.addWidget(self.Pesel,1,0)
        self.uklad_Wyswietlania.addWidget(self.Imie,3,0)
        self.uklad_Wyswietlania.addWidget(self.dataUrodzenia,5,0)
        self.uklad_Wyswietlania.addWidget(self.stan,7,0)
        self.uklad_Wyswietlania.addWidget(self.nrTelefonu,9,0)
        self.uklad_Wyswietlania.addWidget(self.miasto,1,1)
        self.uklad_Wyswietlania.addWidget(self.ulica,3,1)
        self.uklad_Wyswietlania.addWidget(self.numerDomu,5,1)
        self.uklad_Wyswietlania.addWidget(self.numerLokalu,7,1)
        self.uklad_Wyswietlania.addWidget(self.kodPocztowy,9,1)
        self.uklad_Wyswietlania.addWidget(self.Peseltekst,0,0)
        self.uklad_Wyswietlania.addWidget(self.Imietekst,2,0)
        self.uklad_Wyswietlania.addWidget(self.dataUrodzeniatekst,4,0)
        self.uklad_Wyswietlania.addWidget(self.stantekst,6,0)
        self.uklad_Wyswietlania.addWidget(self.nrTelefonutekst,8,0)
        self.uklad_Wyswietlania.addWidget(self.miastotekst,0,1)
        self.uklad_Wyswietlania.addWidget(self.ulicatekst,2,1)
        self.uklad_Wyswietlania.addWidget(self.numerDomutekst,4,1)
        self.uklad_Wyswietlania.addWidget(self.numerLokalutekst,6,1)
        self.uklad_Wyswietlania.addWidget(self.kodPocztowytekst,8,1)
        self.setLayout(self.uklad_Wyswietlania)
class daneSklepu(QDialog):
    def __init__(self,id,nazwa,peselWlasciciela,miasto,ulica,numer_domu,numer_lokalu,kod_pocztowy):
        super().__init__()
        self.ukladSklepu=qt.QGridLayout()
        self.setWindowTitle("Dane Sklepu")
        self.id=qt.QLabel(id)
        self.nazwa=qt.QLabel(nazwa)
        self.peselWlasciciela=qt.QLabel(peselWlasciciela)
        self.miasto=qt.QLabel(miasto)
        if ulica==None:
            self.ulica=qt.QLabel('Brak')
        else:
            self.ulica=qt.QLabel(ulica)
        if numer_domu==None:
            self.numerDomu=qt.QLabel('Brak')
        else:
            self.numerDomu=qt.QLabel(numer_domu)
        if numer_lokalu==False:
            self.nrLokalu=qt.QLabel('brak')
        else:
            self.nrLokalu=qt.QLabel(numer_lokalu)
        self.kodPocztowy=qt.QLabel(kod_pocztowy)
        self.idtekst=qt.QLabel('ID Sklepu')
        self.nazwatekst=qt.QLabel('Nazwa Sklepu')
        self.peselWlascicielatekst=qt.QLabel('Pesel Wlasciciela')
        self.miastotekst=qt.QLabel('Miasto')
        self.ulicatekst=qt.QLabel('Ulica')
        self.numerDomutekst=qt.QLabel('Numer domu')
        self.nrLokalutekst=qt.QLabel('Numer lokalu')
        self.kodPocztowytekst=qt.QLabel('Kod pocztowy')
        self.ukladSklepu.addWidget(self.idtekst,0,0)
        self.ukladSklepu.addWidget(self.id,1,0)
        self.ukladSklepu.addWidget(self.nazwatekst,2,0)
        self.ukladSklepu.addWidget(self.nazwa,3,0)
        self.ukladSklepu.addWidget(self.peselWlascicielatekst,4,0)
        self.ukladSklepu.addWidget(self.peselWlasciciela,5,0)
        self.ukladSklepu.addWidget(self.miastotekst,6,0)
        self.ukladSklepu.addWidget(self.miasto,7,0)
        self.ukladSklepu.addWidget(self.ulicatekst,0,1)
        self.ukladSklepu.addWidget(self.numerDomutekst,1,1)
        self.ukladSklepu.addWidget(self.numerDomu,2,1)
        self.ukladSklepu.addWidget(self.nrLokalutekst,3,1)
        self.ukladSklepu.addWidget(self.nrLokalu,4,1)
        self.ukladSklepu.addWidget(self.kodPocztowytekst,5,1)
        self.ukladSklepu.addWidget(self.kodPocztowy,6,1)
        self.setLayout(self.ukladSklepu)
class Sklep(QDialog):
    def __init__(self):
        super().__init__()
        self.ukladRachunkow=qt.QGridLayout()
        self.setWindowTitle('Wyszukaj Sklep')
        self.id=QLineEdit()
        self.msg=qt.QMessageBox()#zrobic jak by nie bylo takiego
        self.ok=qt.QPushButton('OK')
        self.ok.clicked.connect(self.accept)
        self.info=qt.QLabel('Podaj ID sklepu')
        self.ok=qt.QPushButton('OK')
        self.ok.clicked.connect(self.accept)
        self.ukladRachunkow.addWidget(self.info,0,0)
        self.ukladRachunkow.addWidget(self.id,1,0)
        self.ukladRachunkow.addWidget(self.ok,2,0)
        self.setLayout(self.ukladRachunkow)
class daneZakupu(QDialog):
    def __init__(self,strings):
        super().__init__()
        self.ukladZakupu=qt.QGridLayout()
        self.setWindowTitle('Dane zakupu')
        self.idKupnatekst=qt.QLabel('ID Kupna, ID Sklepu, substancja, ilosc, data kupna')
        self.ukladZakupu.addWidget(self.idKupnatekst,0,0)
        self.zak=[]
        for i in range(len(strings)):
            self.zakup=qt.QLabel(strings[i])
            self.zak.append(self.zakup)
        for i in range(1,len(strings)):
            self.ukladZakupu.addWidget(self.zak[i-1],i,0)        
        self.setLayout(self.ukladZakupu)
class modyfikacja(QDialog):
    def __init__(self):
        super().__init__()
        self.uklad_Modyfikacji=qt.QGridLayout()
        self.setWindowTitle("Modyfikacja danych")
        self.Pesel = QLineEdit() 
        self.msg1=qt.QMessageBox()
        self.informacja=qt.QLabel("Podaj PESEL obywatela ,ktorego dane chcesz zmodyfikowac")
        self.uklad_Modyfikacji.addWidget(self.informacja,0,0)
        self.uklad_Modyfikacji.addWidget(self.Pesel,1,0)
        self.przycisk=qt.QPushButton("Zmień stan")
        self.przycisk.clicked.connect(self.metoda)
        self.uklad_Modyfikacji.addWidget(self.przycisk,2,0)
        self.setLayout(self.uklad_Modyfikacji)
    def metoda(self):
        self.stanTekst=qt.QLabel('Wpisz nowy stan')
        self.stanWybor=qt.QLabel('Możliwe stany: W trakcie, Zakończony, Nie podjęto akcji')
        self.stanOkno=qt.QLineEdit()       
        self.stanPotwierdzenie=qt.QPushButton('OK')
        self.stanPotwierdzenie.clicked.connect(self.accept)
        self.uklad_Modyfikacji.addWidget(self.stanTekst,3,0)
        self.uklad_Modyfikacji.addWidget(self.stanWybor,4,0)
        self.uklad_Modyfikacji.addWidget(self.stanOkno,5,0)
        self.uklad_Modyfikacji.addWidget(self.stanPotwierdzenie,6,0)   
class _config():
    def __init__(self,host,db_name,username,password):
        self.host=host
        self.db_name=db_name
        self.username=username
        self.password=password