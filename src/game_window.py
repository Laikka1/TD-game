import sys
import json
from PyQt6.QtWidgets import QApplication
from coordinates import Coordinates
from world import World
from gui import GUI


def main():

    file_2 = open('pathname.txt', 'r')
    path = file_2.readline()
    path = path.split(",")
    path = path[0]
    file_2.close()

    world = World(24, 15)
    file = path
    with open(f"json_files/{file}", "r") as p:
        data = json.load(p)

    for item in data['path']:
        world.add_path(Coordinates(item[0], item[1]))

    app = QApplication(sys.argv)
    gui = GUI(world, 52)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

