# -*- coding: utf-8 -*-
import mysql.connector as _connector
import klasy as klasy
import PyQt5.QtWidgets as qt
import numpy as np
import klasy_okien as okno
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
class System:
    def __init__(self,config):
        self._connection = _connector.connect(user=config.username, password=config.password, host=config.host, database=config.db_name)
        self.app=qt.QApplication([])
        self.okno=qt.QWidget()
        self.okno.resize(200,150)
        self.uklad=qt.QGridLayout()
        self.okno.setWindowTitle("System")
        self.image=QPixmap('zdrowie1.jpg')
        self.label=qt.QLabel()
        self.label.setPixmap(self.image)
        self.tekst = qt.QLabel("Wybierz co chcesz zrobic")  
        self.tekst_wyswietlanie=qt.QLabel()      
        self.uklad.addWidget(self.tekst,0,0)
        self.wyszukajDane=qt.QPushButton("Wyszukaj Dane Obywatela")
        self.zmodyfikujDane=qt.QPushButton("Zmodyfikuj Dane Obywatela")    
        self.wyszukajSklep=qt.QPushButton("Wyszukaj Sklep")
        self.wyszukajZakup=qt.QPushButton("Wyszukaj Zakupu")
        self.wyszukajZakup.clicked.connect(self.wyszukajZakupu)
        self.koniec=qt.QPushButton("Wyjscie")     
        self.wyszukajDane.clicked.connect(self.wyszukajObywatela)
        self.wyszukajSklep.clicked.connect(self.wyszukajSklepo)
        self.uklad.addWidget(self.label,1,0)
        self.uklad.addWidget(self.wyszukajDane,2,0)
        self.uklad.addWidget(self.zmodyfikujDane,3,0)
        self.zmodyfikujDane.clicked.connect(self.zmodyfikuj)
        self.koniec.clicked.connect(self.wyjscie)
        self.uklad.addWidget(self.wyszukajSklep,4,0)
        self.uklad.addWidget(self.wyszukajZakup,5,0)
        self.uklad.addWidget(self.koniec,6,0)
        self.okno.setLayout(self.uklad)
        self.okno.show()
        self.msg = None
        self.app.exec()
    def zmodyfikuj(self):
        if self.msg is not None:
            self.msg.done(1)
            self.msg = None
        obiekt_modyfikacji=okno.modyfikacja()
        obiekt_modyfikacji.exec()
        if(obiekt_modyfikacji.result() == 1):
            if len(obiekt_modyfikacji.Pesel.text())==11:                
                cursor = self._connection.cursor(prepared=True)
                sql_stan = "SELECT stan FROM obywatel WHERE obywatel.pesel=?"
                pesel=obiekt_modyfikacji.Pesel.text()
                stan= obiekt_modyfikacji.stanOkno.text()
                cursor.execute(sql_stan, [pesel])
                result = cursor.fetchone()
                if result is None:
                    obiekt_modyfikacji.msg1.setIcon(QMessageBox.Information)
                    obiekt_modyfikacji.msg1.setWindowTitle('BŁĄD')
                    obiekt_modyfikacji.msg1.setText('Brak Obywatela o takim nr PESEL')               
                    obiekt_modyfikacji.msg1.setInformativeText('Wcisnij OK aby rozpocząć wyszukiwanie jeszcze raz')
                    obiekt_modyfikacji.msg1.buttonClicked.connect(self.zmodyfikuj)
                    self.msg = obiekt_modyfikacji.msg1
                    obiekt_modyfikacji.msg1.exec()
                    return
                sql = "UPDATE obywatel SET stan=? WHERE obywatel.pesel=?";
                cursor.execute(sql, (stan, pesel))
                self._connection.commit()
                cursor.execute(sql_stan, [pesel])
                result = cursor.fetchone()
                cursor.close()
                if result is None or result[0].decode() != stan:
                    obiekt_modyfikacji.msg1.setIcon(QMessageBox.Information)
                    obiekt_modyfikacji.msg1.setWindowTitle('BŁĄD')
                    obiekt_modyfikacji.msg1.setText('Błąd podczas aktualizacji danych')               
                    obiekt_modyfikacji.msg1.setInformativeText('Wcisnij OK aby rozpocząć wyszukiwanie jeszcze raz')
                    obiekt_modyfikacji.msg1.buttonClicked.connect(self.zmodyfikuj)
                    self.msg = obiekt_modyfikacji.msg1
                    obiekt_modyfikacji.msg1.exec()
                    return
                else:
                    pass
            else:               
                obiekt_modyfikacji.msg1.setIcon(QMessageBox.Information)
                obiekt_modyfikacji.msg1.setWindowTitle('BŁĄD')
                obiekt_modyfikacji.msg1.setText('Pesel ma niewlasciwa dlugosc')               
                obiekt_modyfikacji.msg1.setInformativeText('Wcisnij OK aby rozpocząć wyszukiwanie jeszcze raz')
                obiekt_modyfikacji.msg1.buttonClicked.connect(self.zmodyfikuj)
                self.msg = obiekt_modyfikacji.msg1
                obiekt_modyfikacji.msg1.exec()
    def wyszukajObywatela(self):  
        if self.msg is not None:
            self.msg.done(1)
            self.msg = None
        obiekt2=okno.wyszukiwanie()
        obiekt2.exec()
        if(obiekt2.result() == 1):
            if len(obiekt2.Pesel.text())==11:  
                pesel=obiekt2.Pesel.text()
                cursor = self._connection.cursor(prepared=True)
                sql = "SELECT imie,nazwisko,dataUrodzenia,stan,nr_telefonu,adres.miasto,adres.ulica,adres.numer_domu,adres.numer_lokalu,adres.kod_pocztowy FROM obywatel INNER JOIN adres ON adres.id=obywatel.adres WHERE pesel=?"
                cursor.execute(sql, [pesel])
                result = cursor.fetchone()
                cursor.close()
                if result is None:
                    obiekt2.msg.setIcon(QMessageBox.Information)
                    obiekt2.msg.setWindowTitle('BŁĄD')
                    obiekt2.msg.setText('Brak Obywatela o takim nr PESEL')               
                    obiekt2.msg.setInformativeText('Wcisnij OK aby rozpocząć wyszukiwanie jeszcze raz')
                    obiekt2.msg.buttonClicked.connect(self.wyszukajObywatela)
                    self.msg = obiekt2.msg
                    obiekt2.msg.exec()
                    return 0

                imie = result[0].decode()
                nazwisko = result[1].decode()
                dataUrodzenia = result[2]
                stan = result[3].decode()
                nr_telefonu = result[4]
                if nr_telefonu is not None:
                    nr_telefonu = nr_telefonu.decode()
                else:
                    nr_telefonu = False
        
                miasto = result[5].decode()
                ulica = result[6].decode()
                numer_domu = result[7].decode()
                numer_lokalu = result[8]
                if numer_lokalu is not None:
                    numer_lokalu = numer_lokalu.decode()
                kod_pocztowy = result[9].decode()
                        
                adres = klasy.adres(miasto, ulica, numer_domu, numer_lokalu, kod_pocztowy)
                obiekt_Wyswietlania=okno.okno_Wyswietlania(pesel,imie,nazwisko,str(dataUrodzenia),stan,nr_telefonu,miasto, ulica, numer_domu, numer_lokalu, kod_pocztowy)
                obiekt_Wyswietlania.exec()
                return klasy.obywatel(pesel,imie,nazwisko,dataUrodzenia,adres,stan,nr_telefonu)
            else:
                obiekt2.msg.setIcon(QMessageBox.Information)
                obiekt2.msg.setWindowTitle('BŁĄD')
                obiekt2.msg.setText('Pesel ma niewlasciwa dlugosc')               
                obiekt2.msg.setInformativeText('Wcisnij OK aby rozpocząć wyszukiwanie jeszcze raz')
                obiekt2.msg.buttonClicked.connect(self.wyszukajObywatela)
                self.msg = obiekt2.msg
                obiekt2.msg.exec()

    def wyszukajSklepo(self):
        if self.msg is not None:
            self.msg.done(1)
            self.msg = None
        sklep=okno.Sklep()
        sklep.exec()
        if(sklep.result()==1):
            idSklepu=sklep.id.text()
            if idSklepu=='':
                sklep.msg.setIcon(QMessageBox.Information)
                sklep.msg.setWindowTitle('BŁĄD')
                sklep.msg.setText('Brak sklepu o takim ID')               
                sklep.msg.setInformativeText('Wcisnij OK aby rozpocząć wyszukiwanie jeszcze raz')
                sklep.msg.buttonClicked.connect(self.wyszukajSklepo)
                self.msg = sklep.msg
                sklep.msg.exec()
                return 0
            cursor = self._connection.cursor(prepared=True)
            sql = "SELECT nazwa, peselWlasciciela, adres.miasto, adres.ulica, adres.numer_domu, adres.numer_lokalu, adres.kod_pocztowy FROM sklep INNER JOIN adres ON adres.id=sklep.adres WHERE sklep.id=?"
            cursor.execute(sql, [idSklepu])    
            result = cursor.fetchone()
            cursor.close()
            if result is None:
                sklep.msg.setIcon(QMessageBox.Information)
                sklep.msg.setWindowTitle('BŁĄD')
                sklep.msg.setText('Brak sklepu o takim ID')               
                sklep.msg.setInformativeText('Wcisnij OK aby rozpocząć wyszukiwanie jeszcze raz')
                sklep.msg.buttonClicked.connect(self.wyszukajSklepo)
                self.msg = sklep.msg
                sklep.msg.exec()
                return 0
        
            miasto = result[2].decode()
            ulica = result[3].decode()
            numer_domu = result[4].decode()
            numer_lokalu = result[5]
            if numer_lokalu is not None:
                numer_lokalu = numer_lokalu.decode()
            else:
                numer_lokalu = False
            kod_pocztowy = result[6].decode()
            nazwa=result[0].decode()
            peselWlasciciela=result[1].decode()
            obiektDanych=okno.daneSklepu(idSklepu,nazwa,peselWlasciciela,miasto,ulica,numer_domu,numer_lokalu,kod_pocztowy)
            obiektDanych.exec()
            adres = klasy.adres(miasto, ulica, numer_domu, numer_lokalu, kod_pocztowy)
            return klasy.sklep(idSklepu, nazwa, adres, peselWlasciciela)
    def wyszukajZakupu(self):
        if self.msg is not None:
            self.msg.done(1)
            self.msg = None
        zakup=okno.wyszukiwanie()
        zakup.exec()
        if(zakup.result() == 1):
            if len(zakup.Pesel.text())==11:
                pesel=zakup.Pesel.text()
                cursor = self._connection.cursor(prepared=True)
                sql = "SELECT zakup.id, zakup.substancja, zakup.ilosc, rachunek.idSklepu, rachunek.data FROM zakup INNER JOIN rachunek ON rachunek.id=zakup.idRachunku WHERE rachunek.peselKlienta=?"
                cursor.execute(sql, [pesel])
                result = cursor.fetchall()
                cursor.close()
                if result is None or len(result) == 0:
                    zakup.msg.setIcon(QMessageBox.Information)
                    zakup.msg.setWindowTitle('BŁĄD')
                    zakup.msg.setText('Brak Zakupu obywatela o takim nr PESEL')               
                    zakup.msg.setInformativeText('Wcisnij OK aby rozpocząć wyszukiwanie jeszcze raz')
                    zakup.msg.buttonClicked.connect(self.wyszukajZakupu)
                    self.msg = zakup.msg
                    zakup.msg.exec()
                    return 0
            
                zakup = [None] * len(result)
                strings=[]
                for i in range(len(result)):
                    strings.append('')
                for i in range(0, len(result)):
                    zakup[i] = klasy.zakup(result[i][0], result[i][3], result[i][1].decode(), result[i][2], result[i][4])
                    strings[i]=strings[i]+str(result[i][0])+' '+str(result[i][3])+' '+str(result[i][1].decode())+' '+str(result[i][2])+' '+str(result[i][4])             
                daneZak=okno.daneZakupu(strings)
                daneZak.exec()
                return zakup
            else:
                zakup.msg.setIcon(QMessageBox.Information)
                zakup.msg.setWindowTitle('BŁĄD')
                zakup.msg.setText('Pesel ma niewlasciwa dlugosc')               
                zakup.msg.setInformativeText('Wcisnij OK aby rozpocząć wyszukiwanie jeszcze raz')
                zakup.msg.buttonClicked.connect(self.wyszukajZakupu)
                self.msg = zakup.msg
                zakup.msg.exec()
    def wyjscie(self):
        self.app.closeAllWindows()
        self._connection.close()
config=okno._config('localhost','io_sem4_211a_uzaleznienia','root','')
obiekt = System(config)