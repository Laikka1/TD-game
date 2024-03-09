from PyQt6.QtWidgets import QGraphicsEllipseItem
from PyQt6.QtGui import QColor, QBrush
import json


class Enemy(object):

    def __init__(self, y):
        self.square_size = 52
        self.s_y = y
        self.x = 0
        self.y = 0
        self.Dead = False
        self.Finished = False
        self.n_current_block = 0
        self.enemyPath = []
        self.last_path_point = 0

    def create_enemy(self, gui):
        file_2 = open('pathname.txt', 'r')
        path = file_2.readline()
        path = path.split(",")
        path = path[0]
        file_2.close()

        with open(f"json_files/{path}", "r") as p:
            data = json.load(p)

        if data['path'][0] < data['path'][1]:
            start = data['path'][0]
            self.x = start[0] * self.square_size - self.s_y * 60
            self.y = start[1] * self.square_size + 6
        else:
            start = data['path'][0]
            self.x = start[0] * self.square_size + 6
            self.y = start[1] * self.square_size - self.s_y * 60

        self.circle = self.get_circle()
        self.circle.setPos(self.x, self.y)
        gui.scene.addItem(self.circle)

    def move(self, gui):
        file_2 = open('pathname.txt', 'r')
        path = file_2.readline()
        path = path.split(",")
        path = path[0]
        file_2.close()

        with open(f"json_files/{path}", "r") as p:
            data = json.load(p)

        path = []
        for item in data['path']:
            path.append(item)

        lenght_path = len(path)
        step = self.step

        point_x = path[self.last_path_point][0] * self.square_size + 6
        point_y = path[self.last_path_point][1] * self.square_size + 6
        next_point_x = path[self.last_path_point + 1][0] * self.square_size + 6
        next_point_y = path[self.last_path_point + 1][1] * self.square_size + 6

        if self.last_path_point == (lenght_path - 2):
            gui.scene.removeItem(self.circle)
            self.Finished = True
            return
        else:
            if point_x == self.x and point_y == self.y:
                self.last_path_point += 1

            elif point_x == self.x:
                if next_point_y > self.y:
                    self.y += step
                else:
                    self.y -= step

            elif point_y == self.y:
                if next_point_x > self.x:
                    self.x += step
                else:
                    self.x -= step

        self.circle.setPos(self.x, self.y)
        self.circle.show()

    def check_if_dead(self):

        if self.health <= 0:
            self.Dead = True

    def remove_enemy(self, gui):
        gui.scene.removeItem(self.circle)

class red_enemy(Enemy):
    step = 1
    health = 370
    start = 2

    def __init__(self, y):
        super(red_enemy, self).__init__(y)

    def get_circle(self):
        circle = QGraphicsEllipseItem(0, 0, 35, 35)
        brush = QBrush(QColor(150, 14, 24))
        circle.setBrush(brush)
        return circle

class yellow_enemy(Enemy):
    step = 2
    health = 600
    start = 10

    def __init__(self, y):
        super(yellow_enemy, self).__init__(y)

    def get_circle(self):
        circle = QGraphicsEllipseItem(0, 0, 40, 40)
        brush = QBrush(QColor(228, 208, 28))
        circle.setBrush(brush)
        return circle

class gray_enemy(Enemy):
    step = 1
    health = 1800
    start = 1

    def __init__(self, y):
        super(gray_enemy, self).__init__(y)

    def get_circle(self):
        circle = QGraphicsEllipseItem(-5, -5, 50, 50)
        brush = QBrush(QColor(105, 105, 105))
        circle.setBrush(brush)
        return circle






