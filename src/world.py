
class World:
    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.squares = self.create_square()

    def create_square(self):
        square = []
        for x in range(self.width):
            row = []
            for y in range(self.height):
                row.append(Square())
            square.append(row)
        return square

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def add_path(self, location):

        return self.get_square(location).set_path()

    def get_square(self, coordinates):

        if self.contains(coordinates):
            return self.squares[coordinates.get_x()][coordinates.get_y()]
        else:
            return Square(True)

    def contains(self, coordinates):

        x_coordinate = coordinates.get_x()
        y_coordinate = coordinates.get_y()
        return 0 <= x_coordinate < self.get_width() and 0 <= y_coordinate < self.get_height()

    def is_path(self, coordinates):
        tmp = self.get_square(coordinates).is_path_square()
        return tmp



class Square:

    def __init__(self, is_path=False):
        self.is_path = is_path

    def is_path_square(self):
        return self.is_path

    def is_empty(self):
        return not self.is_path_square()

    def set_path(self):
        if self.is_empty():
            self.is_path = True
            return True
        else:
            return False