import unittest
import opcodelibrary as ol


class test_opcodelibrary(unittest.TestCase):

    def setUp(self):
        self.opcodelibrary = ol.Opcodelibrary()
    
    
    def testLDA(self):
        LDA = self.opcodelibrary.get_all_rules("_LDA")
        self.assertEqual(LDA[0][0], "START")

    
    def testADD(self):
        ADD = self.opcodelibrary.get_all_rules("_ADD")
        self.assertEqual(ADD[0][0], "STadd")
        


if __name__ == '__main__':
    unittest.main()


