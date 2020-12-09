class MMU:
    def __init__(self):
        self.memory = []
        self.virtMemAdresses = {}


    def loadMem(self, binProgram):
        i = 0
        while i < len(binProgram):
            self.memory.append(binProgram[i])
            i = i + 1
        

    def dumpMem(self):
        return(self.memory)
        

    def readMem(self, pc):
        if isinstance(pc, int):
            return(self.memory[pc])
        else:
            if pc in self.virtMemAdresses.keys():
                return(self.memory[self.virtMemAdresses[pc]])
            else:
                return("error")

    def writeMem(self, pc, memVal):
        if isinstance(pc, int):
            self.memory[pc] = memVal
        else:      
            if pc in self.virtMemAdresses.keys():
                self.memory[self.virtMemAdresses(pc)] = memVal
            if pc not in self.virtMemAdresses.keys() and pc[0] == "$":
                self.virtMemAdresses[pc] = len(self.memory)
                self.memory.append(memVal)
            else:
                return("error")
    

