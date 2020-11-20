#import opcodes as oc ## verplaatst naar de exec_opcode class
import tapecommander as tc 
import exec_no_opcode as nop
import exec_opcode as op

class Executer:
    def __init__(self):
        #self.opcodes = oc.Opcodes() # verplaatst naar de exec_opcode class
        tapecommander = tc.Tapecommander()
        #self.no_opcodes = {"PUSH", "PULL"}
        self.execNOP = nop.Exec_no_opcode(tapecommander)
        self.execOP  = op.Exec_opcode(tapecommander)


    def run_commando(self, commando, operand):
        if commando == "PUSH":
             return(self.execNOP.push(operand))
        if commando == "PULL":
             return(self.execNOP.pull())
        else:
            return(self.execOP.run(commando))

    # def run_no_opcode(self, commando, operand):
    #     if commando == "PUSH":
    #         return(self.execNOP.push(operand))
    #     if commando == "PULL":
    #         return(self.execNOP.pull())
    #     else:
    #         return(-1)

    # def run_opcode(self, commando):
    #     print(commando)
    #     return(self.execOP.run(commando))


    # def run__commando(self, commando, operand):
    #     if commando in self.no_opcodes:
    #         return(self.run_no_opcode(commando, operand))
            
    #     else:
    #         return(self.run_opcode(commando))
            
            
    
