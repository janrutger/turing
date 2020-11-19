import unittest
import tapecommander as tc


class test_tapecommander(unittest.TestCase):

    def setUp(self):
        self.tapecommander = tc.Tapecommander()

    def test_gethead(self):
        self.tapecommander = tc.Tapecommander()
        tapes = {"ST", "RA"}
        testresult = self.tapecommander.get_head(tapes)
        self.assertEqual(testresult, {'RA': 2, 'ST': 2})
        tapes = {"ST"}
        testresult = self.tapecommander.get_head(tapes)
        self.assertEqual(testresult, {'ST': 2})
        tapes = {"ST", "RA", "RB", "S"}
        testresult = self.tapecommander.get_head(tapes)
        self.assertEqual(testresult, {'RA': 2, 'RB': 2, 'S': 2, 'ST': 2})
        

    def test_get_TapeValues(self):
        self.tapecommander = tc.Tapecommander()
        tapes = {"ST", "RA", "RB", "S"}
        testresult = self.tapecommander.get_tapeValues(tapes)
        self.assertEqual(testresult, {'RA': '_', 'ST': '_', 'S': '_', 'RB': '_'})

    def test_do_write_read_move(self):
        self.tapecommander = tc.Tapecommander()
        newValues = {"ST":"0", "RA":"1"}
        self.tapecommander.do_write(newValues)

        tapes = {"ST", "RA", "RB", "S"}
        testresult = self.tapecommander.get_tapeValues(tapes)
        self.assertEqual(testresult, {'RA': '1', 'ST': '0', 'S': '_', 'RB': '_'})




    


if __name__ == '__main__':
    unittest.main()