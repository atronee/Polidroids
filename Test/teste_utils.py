import pygame

import sys


sys.path.insert(0, "./States")

import utils as ut
import unittest
from unittest.mock import Mock


def setUpModule():
    pass
def tearDownModule():
    pass

class Test_utils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_case_wrap_position(self):
        surf = pygame.Surface((200, 300))
        result = ut.wrap_position((3,5), surf)
        self.assertEqual(result, pygame.Vector2((3,5)))

    def test_case_get_random_position(self):
        surf = pygame.Surface((600, 800))
        result = ut.get_random_position(surf)
        x, y = result
        self.assertTrue(type(x) == float and type(y) == float)
        self.assertTrue(0 <= x <= 600 and 0 <= y <= 800)

    def test_case_get_random_velocity(self):
        min_speed, max_speed = 20, 90
        result = ut.get_random_velocity(min_speed, max_speed)
        self.assertTrue(type(result) == pygame.math.Vector2)



if __name__ == '__main__':
    unittest.main(verbosity=2)
