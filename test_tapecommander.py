import unittest
import tapecommander as tc


class test_tapecommander(unittest.TestCase):

    def setUp(self):
        self.tapecommander = tc.Tapecommander()

    def test_gethead(self):
        self.tapecommander = tc.Tapecommander()
        tapes = {"ST", "RA", "RB", "S"}
        testresult = self.tapecommander.get_head(tapes)
        print(testresult)

    


if __name__ == '__main__':
    unittest.main()