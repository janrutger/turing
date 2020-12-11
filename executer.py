
import tapecommander as tc 
import exec_no_opcode as nop
import exec_opcode as op

class Executer:
    def __init__(self, memory):
        self.memory = memory
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
        if commando == "HALT":
            exitCode = "CPUstopped"
            self.pc = self.pc
            return(exitCode)
        if commando == "PULL":
            exitCode = self.execNOP.pull()
            self.pc = self.pc + 1
            return(exitCode)
        if commando == "JP":
            exitCode = "HALT"
            self.pc = operand
            return(exitCode)
        if commando == "JPT":
            exitCode = self.execNOP.returnStatus()
            if exitCode == "true":
                self.pc = operand
            else:
                self.pc = self.pc + 1
            return(exitCode)
        if commando == "JPF":
            exitCode = self.execNOP.returnStatus()
            if exitCode == "false":
                self.pc = operand
            else:
                self.pc = self.pc + 1
            return(exitCode)
        else:
            exitCode = self.execOP.run(commando)
            self.pc = self.pc + 1
            return(exitCode)

    def run_program(self, program):
        exitcode = ""
        self.pc = 0
        while self.pc < len(program) and exitcode != "CPUstopped":
            programline = program[self.pc]
            if len(tuple(programline)) == 2:
                opcode  = programline[0]
                operand = programline[1]
                exitcode = (self.run_commando(opcode, operand))

            if len(tuple(programline)) == 1:
                opcode = programline[0]
                exitcode = (self.run_commando(opcode, None))
                
        else:
            if self.pc == len(program):
                return("HALT")
            else:
                return("error")

    def run_memory(self, pc):
        self.pc = pc
        exitcode = "CPUrunning"

        while exitcode != "CPUstopped":
            adresValue = self.memory.readMem(self.pc)
            opcode  = adresValue[0]
            operand = adresValue[1]

            exitcode = self.run_commando(opcode, operand)

        if exitcode == "CPUstopped":
            return("HALT")
        else:
            return("error")

