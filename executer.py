import opcodes as oc 
import tapecommander as tc 

class Executer:
    def __init__(self):
        self.opcodes = oc.Opcodes()
        self.tapecommander = tc.Tapecommander()
        self.nop_commandos = {"PUSH", "PULL"}

    def run_nop_commando(self, commando, operant):
        if commando == "PUSH":
            return("DONE nop")
        if commando == "PULL":
            return("DONE nop")

    def run_opcode_commando(self, commando):
        print(commando)
        return("DONE")


    def run__commando(self, commando, operant):
        if commando in self.nop_commandos:
            return(self.run_nop_commando(commando, operant))
            
        else:
            return(self.run_opcode_commando(commando))
            
            
    
