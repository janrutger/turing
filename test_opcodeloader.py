import unittest
import Opcodeloader as o

class TestTape(unittest.TestCase):

    def setUp(self):
        pass

    def test_loader(self):
        ol = o.OpcodeLoader()
        ol.load()
        data = ol.get()
        self.assertEqual(len(data), 2)