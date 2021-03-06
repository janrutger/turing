import unittest
import executer as ex
from mmu import mmu as MMU

class test_executer(unittest.TestCase):

    def setUp(self):
        memory    = MMU.MMU()
        self.executer = ex.Executer(memory)

    def test_run_PUSH_commando(self):
        #self.executer.run_commando("PUSH","100001")
        self.assertEqual(self.executer.run_commando("PUSH","1011001"), "oke")
        tapelist = {"ST"}
        result = self.executer.refreshTapes(tapelist)
        self.assertEqual(result, {'ST': ['___#101100', '1', '']})

        self.assertEqual(self.executer.run_commando("PUSH","1011"), "oke")
        tapelist = {"ST"}
        result = self.executer.refreshTapes(tapelist)
        self.assertEqual(result, {'ST': ['___#1011001#101', '1', '']})

    def test_run_PUSH_LDA_opcodes(self):
        self.executer.run_commando("PUSH", "1101")
        self.executer.run_commando("PUSH", "0010")
        

        self.assertEqual(self.executer.run_commando("LDA", None), "HALT")
        tapeprint =self.executer.refreshTapes({"ST", "RA"})
        #self.assertEqual(tapeprint, {'RA': ['__111011', '1', '_'], 'ST': ['___#110110', '1', '________']})

        self.assertEqual(self.executer.run_commando("ADD", None), "HALT")
        self.executer.run_commando("PUSH", "1")
        self.assertEqual(self.executer.run_commando("ADD", None), "HALT")

    def test_run_aOther_commando(self):
        #self.executer.run_commando("PULL", None)
        self.assertEqual(self.executer.run_commando("PULL", None), "")

    def test_executer_program(self):
        program = [
            ("PUSH", "11"),
            ("LDB",),
            ("DECB",),
            ("JPF", 2),
            ("PUSH", "00")
        ]
        #exitcode = self.executer.run_program(program)
        #print(self.executer.run_program(program))
        self.assertEqual(self.executer.run_program(program), "HALT")


if __name__ == '__main__':
    unittest.main()