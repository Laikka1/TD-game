

class Coordinates():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return '({:.0f}, {:.0f})'.format(self.get_x(), self.get_y())