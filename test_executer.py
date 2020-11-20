import unittest
import executer as ex


class test_executer(unittest.TestCase):

    def setUp(self):
        self.executer = ex.Executer()

    def test_run_PUSH_commando(self):
        #self.executer.run_commando("PUSH","100001")
        self.assertEqual(self.executer.run_commando("PUSH","1011001"), "oke")
        tapelist = {"ST"}
        result = self.executer.run_commando("PRINT", tapelist)
        self.assertEqual(result, {'ST': ['___#101100', '1', '']})

        self.assertEqual(self.executer.run_commando("PUSH","1011"), "oke")
        tapelist = {"ST"}
        result = self.executer.run_commando("PRINT", tapelist)
        self.assertEqual(result, {'ST': ['___#1011001#101', '1', '']})



    def test_run_aOther_commando(self):
        #self.executer.run_commando("PULL", None)
        self.assertEqual(self.executer.run_commando("PULL", None), "0")

    def test_run_PUSH_LDA_opcodes(self):
        self.executer.run_commando("PUSH", "1")
        self.executer.run_commando("PUSH", "11")
        

        self.assertEqual(self.executer.run_commando("LDA", None), "HALT")
        tapeprint =self.executer.run_commando("PRINT", {"ST", "RA"})
        #self.assertEqual(tapeprint, {'RA': ['__111011', '1', '_'], 'ST': ['___#110110', '1', '________']})

        self.assertEqual(self.executer.run_commando("ADD", None), "HALT")
        self.executer.run_commando("PUSH", "111")
        self.assertEqual(self.executer.run_commando("ADD", None), "HALT")


if __name__ == '__main__':
    unittest.main()