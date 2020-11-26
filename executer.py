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
        if commando == "PRINT":
            return(self.execNOP.print(operand))
        if commando == "PULL":
             return(self.execNOP.pull())
        else:
            return(self.execOP.run(commando))

    def run_program(self, program):
        PC = 0

        while PC < len(program):
            programline = program[PC]
            if len(tuple(programline)) == 2:
                opcode  = programline[0]
                operand = programline[1]
                exitcode = (self.run_commando(opcode, operand))
                PC = PC +1

            if len(tuple(programline)) == 1:
                opcode = programline[0]
                exitcode = (self.run_commando(opcode, None))
                PC = PC +1
                
            if len(tuple(programline)) == 0:
                #exitcode = "HALT"
                return(exitcode)
            
        else:
            return("error")


   