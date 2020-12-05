import unittest
from assembler import assembler as asm
import executer as e



class test_opcodes(unittest.TestCase):

    def setUp(self):
        self.assembler = asm.Assembler()
        self.executer  = e.Executer()


    def test_readASM(self):
        #self.assembler = asm.Assembler()
        #self.assembler.readASM('./demo.asm')
        result = self.assembler.readASM("/home/pi/projects/assembler/test1.asm")
        self.assertEqual(result, ['#'])

    def test_compile(self):
        program = self.assembler.readASM("/home/pi/projects/turing2/assembler/jrk.asm")
        program = self.assembler.compile(program)
        print(program)

    def test_run_program(self):
        ASMfile    = self.assembler.readASM("/home/pi/projects/turing2/assembler/jrk.asm")
        BINprogram = self.assembler.compile(ASMfile)
        self.executer.run_program(BINprogram) 
        

if __name__ == '__main__':
    unittest.main()
