from assembler import ASMcompiler as c


class Assembler:
    def __init__(self):
        self.compiler = c.Compiler()


    def readASM(self, filename):
        ASMfile = []
        file = open(filename, "r")
        for line in file:
            ASMfile.append(line.strip())
        file.close()
        return(ASMfile)

    def compile(self, ASMfile):
        program    = self.compiler.parseProgram(ASMfile)
        program    = self.compiler.ProcesLabels(program)
        BINprogram = self.compiler.ProcesLines(program)

        return(BINprogram)

    def execute(self, programFile):
        pass

    

