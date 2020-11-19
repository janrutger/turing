import unittest
import opcodes as oc


class test_opcodes(unittest.TestCase):

    def setUp(self):
        self.opcodes = oc.Opcodes()
    
    def test_get_tape_list(self):
        opcode = "_LDA"                      #komt van executer
        tapelist = self.opcodes.get_tapelist(opcode)
        self.assertEqual(tapelist, ['ST', 'RA'])
        
        opcode = "_ADD"                      #komt van executer
        tapelist = self.opcodes.get_tapelist(opcode)
        self.assertEqual(tapelist, ['ST', 'Rb'])

    def test_get_turingrules(self):
        opcode    = "_LDA"                   #komt van executer
        tapevalue = {"ST":"1", "RA":"_"}    #komt van executer
        state     = "START"                 #komt van executer
        turingrules = self.opcodes.get_turingrule(opcode, tapevalue, state)
        self.assertEqual(turingrules, ({"ST":"_", "RA":"1"}, {"ST":"L", "RA":"L"}, "HALT"))

        opcode    = "_ADD"                   #komt van executer
        tapevalue = {"ST":"1", "Rb":"0"}    #komt van executer
        state     = "STadd"                 #komt van executer
        turingrules = self.opcodes.get_turingrule(opcode, tapevalue, state)
        self.assertEqual(turingrules, ({"ST":"_", "Rb":"1"}, {"ST":"L", "Rb":"L"}, "DONE"))

if __name__ == '__main__':
    unittest.main()