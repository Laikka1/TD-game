import unittest
from coordinates import Coordinates
from world import World
import json


class Test(unittest.TestCase):

    def setUp(self):
        self.test_world = World(24, 15)
        file = 'path.json'
        with open(file, "r") as p:
            data = json.load(p)
        path = []
        for item in data['path']:
            path.append(Coordinates(item[0], item[1]))
        for item in path:
            self.test_world.add_path(item)

    def test_is_path(self):
        self.assertEqual(True, self.test_world.is_path(Coordinates(15, 2)))

    def test_is_not_path(self):
        self.assertEqual(False, self.test_world.is_path(Coordinates(2, 4)))


if __name__ == "__main__":
    unittest.main()
