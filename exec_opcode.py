import opcodes as oc 


class Exec_opcode:
    def __init__(self, tapecommander):
        self.tapecommander = tapecommander
        self.opcodes = self.opcodes = oc.Opcodes()


    def run(self, opcode):
        tapeList    = self.opcodes.get_tapelist(opcode)
        state       = "START"
        tapeValues  = self.tapecommander.do_read(tapeList)
        turingRules = self.opcodes.get_turingrule(opcode, tapeValues, state)

        writeValue  = turingRules[0]
        moveValue   = turingRules[1]
        nextState   = turingRules[2]

        self.tapecommander.do_write(writeValue)
        self.tapecommander.do_move(moveValue)

        tapeprint =self.tapecommander.print_tape(tapeList)
        print(tapeprint)

        while nextState != "HALT":
            state       = nextState
            tapeValues  = self.tapecommander.do_read(tapeList)
            turingRules = self.opcodes.get_turingrule(opcode, tapeValues, state)
        
            writeValue  = turingRules[0]
            moveValue   = turingRules[1]
            nextState   = turingRules[2]

            self.tapecommander.do_write(writeValue)
            self.tapecommander.do_move(moveValue)
        
            tapeprint =self.tapecommander.print_tape(tapeList)
            print(tapeprint)
    
        return(nextState)      #do something smarter over here
