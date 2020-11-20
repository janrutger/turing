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

        #self.executer.run_commando("LDA", None)
        self.executer.run_commando("PUSH", "10101")
        
        self.assertEqual(self.executer.run_commando("LDA", None), "LDA")


if __name__ == '__main__':
    unittest.main()