import tapecommander as tc 
import exec_no_opcode as nop
import exec_opcode as op

class Executer:
    def __init__(self):
        tapecommander = tc.Tapecommander()
        self.execNOP = nop.Exec_no_opcode(tapecommander)
        self.execOP  = op.Exec_opcode(tapecommander)
        self.pc = int(0)

    def refreshTapes(self, tapeList):
        exitCode = self.execNOP.print(tapeList)
        return(exitCode)

    def run_commando(self, commando, operand):
        if commando == "PUSH":
            exitCode = self.execNOP.push(operand)
            self.pc = self.pc + 1
            return(exitCode)
        if commando == "PULL":
            exitCode = self.execNOP.pull()
            self.pc = self.pc + 1
            return(exitCode)
        else:
            exitCode = self.execOP.run(commando)
            self.pc = self.pc + 1
            return(exitCode)

    def run_program(self, program):
        self.pc = 0
        print(type(self.pc))
        while self.pc < len(program):
            programline = program[self.pc]
            if len(tuple(programline)) == 2:
                opcode  = programline[0]
                operand = programline[1]
                exitcode = (self.run_commando(opcode, operand))
                #pc = pc +1

            if len(tuple(programline)) == 1:
                opcode = programline[0]
                exitcode = (self.run_commando(opcode, None))
                #pc = pc +1
                
        else:
            if self.pc == len(program):
                return("HALT")
            else:
                return("error")


   