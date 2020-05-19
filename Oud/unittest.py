import unittest
import Opcodeloader as oc

class TestOpcodeLoader(unittest.TestCase):

    def test_load_simple_file(self):
        self.opcodeLoader = oc.OpcodeLoader('OpcodeData.json')
        opCodes = self.opcodeLoader.getOpcodes()

        self.assertEqual(len(opCodes), 1)
        self.assertEqual(opCodes[0].getName(), 'LDA')
        self.assertEqual(len(opCodes[0].getStates()), 1)
        # self.assertEqual(opCodes[0].getStates(), 'here we need an object') 