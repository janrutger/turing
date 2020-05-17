import unittest
import OpcodeLoader as oc

class TestOpcodeLoader(unittest.TestCase):

    def test_load_simple_file(self):
        self.opcodeLoader = oc.OpcodeLoader('test-oc-data.json')
        opCodes = self.opcodeLoader.getOpcodes()

        self.assertEqual(len(opCodes), 1)
        self.assertEqual(opCodes[0].getName(), 'LDA')
        self.assertEqual(len(opCodes[0].getStates()), 1)
        # self.assertEqual(opCodes[0].getStates(), 'here we need an object')