import opcodes as oc 
import tapecommander as tc 

class Executer:
    def __init__(self):
        self.opcodes = oc.Opcodes()
        self.tapecommander = tc.Tapecommander()
        self.nop_commandos = {"PUSH", "PULL"}

    def run_nop_commando(self, commando, operant):
        print(commando, operant)

    def run_opcode_commando(self, commando):
        print(commando)


    def run__commando(self, commando, operant):
        if commando in self.nop_commandos:
            self.run_nop_commando(commando, operant)
            return("DONE nop")
        else:
            self.run_opcode_commando(commando)
            return("DONE")
            
    
