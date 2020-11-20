import opcodes as oc 


class Exec_opcode:
    def __init__(self, tapecommander):
        self.tapecommander = tapecommander
        self.opcodes = self.opcodes = oc.Opcodes()


    def run(self, opcode):
        return(opcode)      #do something smarter over here
