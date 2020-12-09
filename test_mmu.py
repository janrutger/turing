import unittest
from assembler import assembler as asm
from mmu       import mmu       as mmu
import executer as e



class test_opcodes(unittest.TestCase):

    def setUp(self):
        self.assembler = asm.Assembler()
        self.executer  = e.Executer()
        self.memMgr    = mmu.MMU()
        ASMfile        = self.assembler.readASM("/home/pi/projects/turing2/mmu/test_mmu.asm")
        self.BINprogram = self.assembler.compile(ASMfile)


    def test_load(self):
        self.memMgr.loadMem(self.BINprogram)

    def test_dump(self):
        self.memMgr.loadMem(self.BINprogram)
        memDump = self.memMgr.dumpMem()
        self.assertEqual(memDump, [('PUSH', '1010'), ('LDA', ''), ('PUSH', '1010')])
    
    def test_read(self):
        self.memMgr.loadMem(self.BINprogram)
        memVal = self.memMgr.readMem(2)
        self.assertEqual(memVal, ('PUSH', '1010'))

    def test_write(self):
    
        self.memMgr.loadMem(self.BINprogram)
        print(self.memMgr.dumpMem())

        memVal = ('MEM', '1001')
        self.memMgr.writeMem("$jr", memVal)
        memVal = ('MEM', '1111')
        self.memMgr.writeMem("$jrk", memVal)

        memVal = self.memMgr.readMem("$jr3")
        self.assertEqual(memVal, "error")

        memVal = self.memMgr.readMem("$jr")
        self.assertEqual(memVal, ('MEM', '1001'))

        memVal = self.memMgr.readMem("$jrk")
        self.assertEqual(memVal, ('MEM', '1111'))

        print(self.memMgr.dumpMem())
        

if __name__ == '__main__':
    unittest.main()
