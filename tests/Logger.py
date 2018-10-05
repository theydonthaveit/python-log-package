import unittest
from Logger import *

class MyFirstTests(unittest.TestCase):

    def test_logger_init(self):
        self.assertTrue(Logger())


if __name__ == '__main__':
    unittest.main()