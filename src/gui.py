from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGraphicsView, \
    QGraphicsScene, QMainWindow, QLabel, QGraphicsPixmapItem, QMessageBox
from PyQt6.QtGui import QFont, QFontDatabase, QPixmap
from PyQt6.QtCore import QTimer
from coordinates import Coordinates
from world import Square
from enemy import red_enemy, yellow_enemy, gray_enemy
from tower import tower1, tower2
import json
import os


class GUI(QMainWindow):

    def __init__(self, world, square_size):
        super().__init__()
        self.setCentralWidget(QWidget())
        self.horizontal = QHBoxLayout()
        self.vertical = QVBoxLayout()
        self.horizontal.insertLayout(0, self.vertical)
        self.centralWidget().setLayout(self.horizontal)
        self.setStyleSheet('background: rgb(0, 30, 0)')

        self.world = world
        self.square_size = square_size
        self.scene = QGraphicsScene()

        '''game values'''
        self.setFixedSize(1235, 670)
        self.enemys = []
        self.towers = []

        file_2 = open('pathname.txt', 'r')
        path = file_2.readline()
        parts = path.split(",")
        path = parts[0]
        difficulty = parts[1]
        file_2.close()

        self.difficulty = difficulty
        self.path = path

        if self.path == 'path_1.json':
            if self.difficulty == 'easy':
                self.credit = 250
            else:
                self.credit = 190
        else:
            if self.difficulty == 'easy':
                self.credit = 470
            else:
                self.credit = 199

        if self.difficulty == 'hard':
            self.lives = 1
        else:
            self.lives = 10

        self.wave = 0
        self.num_waves = 0
        self.last_clicked_button = None

        '''functions to make window'''
        self.window()
        self.add_buttons()
        self.top_bar()
        self.make_grid()

        self.show()

    def window(self):
        self.setWindowTitle('The GAME')
        self.scene.setSceneRect(0, 0, 1088, 600)
        self.view = QGraphicsView(self.scene, self)
        self.horizontal.insertWidget(1, self.view)

    def add_buttons(self):
        f_id = QFontDatabase.addApplicationFont("Visuals/Font/ComicMono.ttf")
        families = QFontDatabase.applicationFontFamilies(f_id)

        self.start_btn = QPushButton("Start")
        self.start_btn.setFixedSize(120, 70)
        self.start_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')
        self.start_btn.setFont(QFont(families[0], 20))
        self.vertical.addWidget(self.start_btn)
        self.start_btn.clicked.connect(self.start)

        self.tower_btn = QPushButton("Tower 1\n(100)")
        self.tower_btn.setFixedSize(120, 90)
        self.tower_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')
        self.tower_btn.setFont(QFont(families[0], 20))
        self.vertical.addWidget(self.tower_btn)
        self.tower_btn.clicked.connect(self.tower1_clicked)

        self.tower2_btn = QPushButton("Tower 2\n(300)")
        self.tower2_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')
        self.tower2_btn.setFont(QFont(families[0], 20))
        self.tower2_btn.setFixedSize(120, 90)
        self.vertical.addWidget(self.tower2_btn)
        self.tower2_btn.clicked.connect(self.tower2_clicked)

        self.Restart_btn = QPushButton("Restart")
        self.Restart_btn.setFixedSize(120, 70)
        self.Restart_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')
        self.Restart_btn.setFont(QFont(families[0], 20))
        self.vertical.addWidget(self.Restart_btn)
        self.Restart_btn.clicked.connect(self.restart)

        self.menu_btn = QPushButton("Menu")
        self.menu_btn.setFixedSize(120, 50)
        self.menu_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')
        self.menu_btn.setFont(QFont(families[0], 20))
        self.vertical.addWidget(self.menu_btn)
        self.menu_btn.clicked.connect(self.back_to_menu)

    def back_to_menu(self):
        self.close()
        os.system("menu_window.py")

    def top_bar(self):

        f_id = QFontDatabase.addApplicationFont("Visuals/Font/ComicMono.ttf")
        families = QFontDatabase.applicationFontFamilies(f_id)

        self.credit_bar = QLabel(self)
        self.credit_bar.setText(f"Credits:{self.credit}")
        self.credit_bar.setStyleSheet('color:tan;')
        self.credit_bar.setFont(QFont(families[0], 20))
        self.credit_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.credit_bar.setGeometry(30, 0, 400, 35)

        self.lives_bar = QLabel(self)
        self.lives_bar.setText(f"Lives:{self.lives}")
        self.lives_bar.setStyleSheet('color:tan;')
        self.lives_bar.setFont(QFont(families[0], 20))
        self.lives_bar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lives_bar.setGeometry(430, 0, 400, 35)

        self.waveBar = QLabel(self)
        self.waveBar.setText(f"Wave:{self.wave}")
        self.waveBar.setStyleSheet('color:tan;')
        self.waveBar.setFont(QFont(families[0], 20))
        self.waveBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.waveBar.setGeometry(830, 0, 400, 35)

    def make_grid(self):
        for i in range(self.world.get_width()):
            for j in range(self.world.get_height()):
                x = i * self.square_size
                y = j * self.square_size

                square_type = self.world.get_square(Coordinates(i, j))

                if Square.is_path_square(square_type):
                    r = QGraphicsPixmapItem(QPixmap("Visuals/Textures/dirt.png"))

                    r.setOffset(x, y)
                else:
                    r = QGraphicsPixmapItem(QPixmap("Visuals/Textures/grass.png"))
                    r.setOffset(x, y)
                self.scene.addItem(r)

    def restart(self):
        for tower in self.towers:
            tower.remove_tower(self)
        for enemy in self.enemys:
            enemy.remove_enemy(self)

        self.towers = []
        self.enemys = []
        self.wave = 0
        if self.difficulty == 'hard':
            self.lives = 1
        else:
            self.lives = 10

        if self.path == 'path_1.json':
            if self.difficulty == 'easy':
                self.credit = 250
            else:
                self.credit = 190
        else:
            if self.difficulty == 'easy':
                self.credit = 270
            else:
                self.credit = 199

        self.lives_bar.setText(f"Lives:{self.lives}")
        self.credit_bar.setText(f"Credits:{self.credit}")
        self.waveBar.setText(f"Wave:{self.wave}")

    def start(self):
        self.start_btn.hide()
        self.wave += 1
        self.waveBar.setText(f"Wave:{self.wave}")

        with open("json_files/wave.json", "r") as f:
            data = json.load(f)
        self.num_waves = data['num_of_waves'][0]
        current_wave = data[self.difficulty][self.wave - 1]
        red_units = current_wave["red"]
        yellow_units = current_wave["yellow"]
        gray_units = current_wave["gray"]

        i = 0
        while i < red_units:
            self.enemys.append(red_enemy(i))
            i += 1

        j = 13
        while j < (yellow_units + 13):
            self.enemys.append(yellow_enemy(j))
            j += 1

        k = 8
        while k < (gray_units + 8):
            self.enemys.append(gray_enemy(k))
            k += 1

        for enemy in self.enemys:
            enemy.create_enemy(self)
            self.show()

        self.timer = QTimer()
        self.timer.timeout.connect(self.run)
        self.timer.start(10)

    def run(self):
        if len(self.enemys) == 0:
            self.timer.stop()
            self.start_btn.show()

        for enemy in self.enemys:
            enemy.check_if_dead()
            if enemy.Finished:
                self.enemys.remove(enemy)
                self.lives -= 1
                self.lives_bar.setText(f"Lives:{self.lives}")
                if self.lives == 0:
                    self.defeat()
            if enemy.Dead:
                self.enemys.remove(enemy)
                enemy.remove_enemy(self)
                kerroin = 1 - (self.wave * 1.7) * 0.1
                if kerroin < 0.13:
                    kerroin = 0.13
                self.credit += round(25 * kerroin)
                self.credit_bar.setText(f"Credit:{self.credit}")
                if self.wave == self.num_waves:
                    if not self.enemys:
                        self.victory()

            else:
                enemy.move(self)

        for tower in self.towers:
            tower.attack(self)

    def tower1_clicked(self):
        if self.credit < 100:
            return

        if self.last_clicked_button == self.tower_btn:
            self.last_clicked_button = None
            self.tower_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')
        elif self.last_clicked_button == self.tower2_btn:
            self.tower2_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')
            self.last_clicked_button = self.tower_btn
            self.tower_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: Black;}')
        else:
            self.last_clicked_button = self.tower_btn
            self.tower_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: Black;}')

    def tower2_clicked(self):
        if self.credit < 300:
            return
        if self.last_clicked_button == self.tower2_btn:
            self.last_clicked_button = None
            self.tower2_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')
        elif self.last_clicked_button == self.tower_btn:
            self.tower_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')
            self.last_clicked_button = self.tower2_btn
            self.tower2_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: Black;}')
        else:
            self.last_clicked_button = self.tower2_btn
            self.tower2_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: Black;}')

    def mousePressEvent(self, event):
        x = event.pos().x()
        y = event.pos().y()

        if self.last_clicked_button == None:
            return

        p = self.is_pressed_path(x, y)
        if p == False:

            if self.last_clicked_button == self.tower_btn:
                self.credit -= 100
                self.credit_bar.setText(f"Credit:{self.credit}")
                self.towers.append(tower1(x, y))
                for tower in self.towers:
                    if tower.placed == False:
                        tower.place_tower(self)
                        self.tower_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')
                        self.last_clicked_button = None

            if self.last_clicked_button == self.tower2_btn:
                self.credit -= 300
                self.credit_bar.setText(f"Credit:{self.credit}")
                self.towers.append(tower2(x, y))
                for tower in self.towers:
                    if tower.placed == False:
                        tower.place_tower(self)
                        self.tower2_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')
                        self.last_clicked_button = None
        else:
            self.last_clicked_button = None
            self.tower_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')
            self.tower2_btn.setStyleSheet('QPushButton {background:url(Visuals/Textures/wood1.png); color: tan;}')

    def is_pressed_path(self, x, y):

        self.center_x = round(x / self.square_size)
        self.center_y = round(y / self.square_size)

        return self.world.is_path(Coordinates(self.center_x - 3, self.center_y - 1))

    def victory(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Victory!")
        msg.setText("You Won the game \nWould you like to play again?")
        msg.setStyleSheet("background-color:rgb(0, 30, 0); color:Tan; font-size: 20px")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        button = msg.exec()

        if button == QMessageBox.StandardButton.No:
            quit()
        else:
            self.restart()

    def defeat(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Defeat!")
        msg.setText("You lost the game \nWould you like to play again?")
        msg.setStyleSheet("background-color:rgb(0, 30, 0); color:Tan; font-size: 20px")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        button = msg.exec()

        if button == QMessageBox.StandardButton.No:
            quit()
        else:
            self.restart()




