from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow
from PyQt6.QtGui import QFont, QFontDatabase
import sys
import os



class Menuwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tornipuolustus peli")

        self.setFixedSize(1265, 640)
        self.setStyleSheet('background: rgb(0, 30, 0)')
        self.create_widgets()

    def create_widgets(self):

        id = QFontDatabase.addApplicationFont("Visuals/Font/ComicMono.ttf")
        families = QFontDatabase.applicationFontFamilies(id)

        map1e_btn = QPushButton('', self)
        map1e_btn.setGeometry(208, 150, 324, 200)
        map1e_btn.setFont(QFont(families[0], 40))
        map1e_btn.setStyleSheet('QPushButton {background:url(Visuals/Maps/map1_easy.png);border: 0px}')

        map1h_btn = QPushButton('', self)
        map1h_btn.setGeometry(208, 400, 324, 200)
        map1h_btn.setFont(QFont(families[0], 40))
        map1h_btn.setStyleSheet('QPushButton {background:url(Visuals/Maps/map1_hard.png);border: 0px}')

        map2e_btn = QPushButton('', self)
        map2e_btn.setGeometry(732, 150, 327, 200)
        map2e_btn.setFont(QFont(families[0], 40))
        map2e_btn.setStyleSheet('QPushButton {background:url(Visuals/Maps/map2_easy.png);border: 0px}')

        map2h_btn = QPushButton('', self)
        map2h_btn.setGeometry(732, 400, 327, 200)
        map2h_btn.setFont(QFont(families[0], 40))
        map2h_btn.setStyleSheet('QPushButton {background:url(Visuals/Maps/map2_hard.png);border: 0px}')

        map1e_btn.clicked.connect(self.start_map_1_easy)
        map2e_btn.clicked.connect(self.start_map_2_easy)
        map1h_btn.clicked.connect(self.start_map_1_hard)
        map2h_btn.clicked.connect(self.start_map_2_hard)

        label_game = QLabel("TorniPuolustus", self)
        label_game.setGeometry(370, 0, 600, 100)
        label_game.setStyleSheet('color: rgb(150,0,0)')
        label_game.setFont(QFont(families[0], 50))

        label_m = QLabel("Valitse Kartta", self)
        label_m.setGeometry(470, 80, 330, 60)
        label_m.setStyleSheet('color: tan')
        label_m.setFont(QFont(families[0], 30))

    def start_map_1_easy(self):
        filename = 'pathname.txt'
        file = open(filename, "w")
        file.write("path_1.json,easy")
        file.close()
        self.close()
        os.system("game_window.py")

    def start_map_1_hard(self):
        filename = 'pathname.txt'
        file = open(filename, "w")
        file.write("path_1.json,hard")
        file.close()
        self.close()
        os.system("game_window.py")

    def start_map_2_easy(self):
        filename = 'pathname.txt'
        file = open(filename, "w")
        file.write("path_2.json,easy")
        file.close()
        self.close()
        os.system("game_window.py")

    def start_map_2_hard(self):
        filename = 'pathname.txt'
        file = open(filename, "w")
        file.write("path_2.json,hard")
        file.close()
        self.close()
        os.system("game_window.py")



app = QApplication(sys.argv)
window = Menuwindow()
window.show()
app.exec()
