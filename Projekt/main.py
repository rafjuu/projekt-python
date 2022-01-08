import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot
from cryptography.fernet import Fernet
from tkinter import filedialog





def wczytajPlik(sciezka): # wczytuje dane z pliku z podanej ścieżki i zwraca dane
    plik = open(sciezka)
    try:
        tekst = plik.read()
    finally:
        plik.close()

    return tekst


def load_key(): # wybór klucza
    filename = filedialog.askopenfilename()
    return open(filename, "rb").read()


class MainWindow(QMainWindow): # klasa okno główne
    def __init__(self, parent=None): # funkcja inicjująca
        super().__init__(parent)
        # tu będą widgety

        self.window = QWidget




        loader = QUiLoader()
        self.window = loader.load("untitled.ui", self)

        # sygnał połączenia


        self.window.clearButton_2.clicked.connect(self.clear2) # czyszczenie textbox2
        self.window.clearButton_3.clicked.connect(self.clear3) # i text box3


        self.window.loadButton.clicked.connect(self.szyfrowanie) #wywołanie szyfrowania
        self.window.loadButton_2.clicked.connect(self.deszyfrowanie)
        self.window.wczytajzaszyfrowany.clicked.connect(self.wczytajzaszyfrowany)
        self.window.wczytajdozaszyfrowania.clicked.connect(self.wczytajtekstdoszaszyfrowania)
        self.window.pushtext.clicked.connect(self.pushtext)
        self.window.zapiszzaszyfrowany.clicked.connect(self.zapiszzaszyfrowany)
        self.window.zapiszodszyfrowany.clicked.connect(self.zapiszodszyfrowany)
        self.window.genizapisz.clicked.connect(self.genizapisz)


        # pokaż
        self.show()




    @Slot()


    def pushtext(self): #przniesienie tekstu

        tekst = self.window.textEdit_2.toPlainText()
        self.window.textEdit_2.clear()
        self.window.textEdit_3.setMarkdown(tekst)

    def zapiszzaszyfrowany(self): #jak nazwa
        tekst = self.window.textEdit_2.toPlainText()
        new_file = filedialog.asksaveasfile()
        new_file.write(tekst)
        new_file.close()

    def zapiszodszyfrowany(self): #jak nazwa
        tekst = self.window.textEdit_3.toPlainText()
        new_file = filedialog.asksaveasfile()
        new_file.write(tekst)
        new_file.close()

        #zapisztresc(filename, tekst)


    def wczytajzaszyfrowany(self): #jak nazwa
        filename = filedialog.askopenfilename()


        tekst = wczytajPlik(filename)
        self.window.textEdit_3.setMarkdown(tekst)

    def wczytajtekstdoszaszyfrowania(self): #jak nazwa
        filename = filedialog.askopenfilename()
        tekst = wczytajPlik(filename)
        self.window.textEdit_2.setMarkdown(tekst)



    def genizapisz(self): # generuje i zapisuje klucz do pliku
        key = Fernet.generate_key()
        new_key = filedialog.asksaveasfile()
        new_key.write(key.decode())
        new_key.close()




    def clear2(self):#czyszczenie okna 2
        self.window.textEdit_2.clear()

    def clear3(self):#czyszczenie okna 3
        self.window.textEdit_3.clear()





    def szyfrowanie(self): #szyfrowanie
        key = load_key()

        f = Fernet(key)
        text = self.window.textEdit_2.toPlainText()
        zasztext = f.encrypt(text.encode())
        self.window.textEdit_2.setMarkdown(zasztext.decode())
        #print(zasztext)




    def deszyfrowanie(self): # jak nazwa

        key = load_key()
        texttodecrypt = self.window.textEdit_3.toPlainText()
        f = Fernet(key)
        textdecrypt = f.decrypt(texttodecrypt.encode())
        self.window.textEdit_3.setMarkdown(textdecrypt.decode())




if __name__ == "__main__": # potrzebne do wczytania okna
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())