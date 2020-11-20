import unittest
import executer as ex


class test_executer(unittest.TestCase):

    def setUp(self):
        self.executer = ex.Executer()

    def test_run_commando(self):
        #self.executer.run__commando("PUSH","100001")
        self.assertEqual(self.executer.run__commando("PUSH","100001"), "100001")

        #self.executer.run__commando("PULL", None)
        self.assertEqual(self.executer.run__commando("PULL", None), "0")

        #self.executer.run__commando("LDA", None)
        self.assertEqual(self.executer.run__commando("LDA", None), "LDA")


if __name__ == '__main__':
    unittest.main()