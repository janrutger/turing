#import opcodes as oc ## verplaatst naar de exec_opcode class
import tapecommander as tc 
import exec_no_opcode as nop
import exec_opcode as op

class Executer:
    def __init__(self):
        tapecommander = tc.Tapecommander()
        self.execNOP = nop.Exec_no_opcode(tapecommander)
        self.execOP  = op.Exec_opcode(tapecommander)


    def run_commando(self, commando, operand):
        if commando == "PUSH":
             return(self.execNOP.push(operand))
        if commando == "PULL":
             return(self.execNOP.pull())
        else:
            return(self.execOP.run(commando))

   