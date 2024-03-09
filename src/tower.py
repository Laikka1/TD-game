from PyQt6.QtWidgets import QGraphicsPixmapItem, QLabel
from PyQt6.QtGui import QPixmap
import math


class Tower:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attacking = False
        self.placed = False
        self.square_size = 52
        self.range = self.square_size * 3
        self.enemyx = None
        self.enemyy = None
        self.shooting = False

    def place_tower(self, gui):
        self.Tower = self.get_tower_image()
        ret = self.set_center()
        if ret:
            gui.scene.addItem(self.Tower)
            self.Tower.show()
            self.placed = True

    def set_center(self):
        self.center_x = round(self.x / self.square_size)
        self.center_y = round(self.y / self.square_size)


        self.center_x_2 = self.center_x * self.square_size - 3 * self.square_size
        self.center_y_2 = self.center_y * self.square_size - self.square_size + 2
        self.Tower.setOffset(self.center_x_2, self.center_y_2)
        return 1

    def attack(self, gui):

        for enemy in gui.enemys:
            if enemy.Finished == False:
                distanece_from_tower = math.sqrt(pow(self.center_x_2 - enemy.x, 2) + pow(self.center_y_2 - enemy.y, 2))
                if distanece_from_tower <= self.range:
                    self.hit_enemy(enemy)
                    break

    def remove_tower(self, gui):
        gui.scene.removeItem(self.Tower)

class tower1(Tower):

    def __init__(self, x, y):
        super(tower1, self).__init__(x, y)
        self.damage = 3

    def hit_enemy(self, enemy):
        enemy.health -= self.damage

    def get_tower_image(self):
        T = QGraphicsPixmapItem(QPixmap("Visuals/Textures/Tower1.png"))
        return T

class tower2(Tower):

    def __init__(self, x, y):
        super(tower2, self).__init__(x, y)
        self.damage = 8

    def hit_enemy(self, enemy):
        enemy.health -= self.damage

    def get_tower_image(self):
        T = QGraphicsPixmapItem(QPixmap("Visuals/Textures/Tower2.png"))
        return T
