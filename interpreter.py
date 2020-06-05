import Opcodeloader as ol
import Opcode as oc
import sequencer as sq

class Interpreter():
    def __init__(self, opcodelibrary, tapecommander):
#    def __init__(self, opcodelibrary, opcode, operand, tapecommander):
        self.opcodelibrary = opcodelibrary
        self.opcodeintern = ["PUSH", "TEST"]
#        self.opcode = opcode
        self.opcodestates = []         
#        self.operand = operand
        self.tapecommander = tapecommander
#        self.check()
        
    def contains(self, value):
        for item in self.opcodelibrary:          
            if value == item.getName():
                self.opcodestates = item.getStates()
                return True
        return False

    def exec_PUSH(self, operand):
        print("Running: ", "PUSH", "- ", operand)
        self.tapecommander.write(["_","-","-","-"])
        self.tapecommander.move(["L","S","S","S"])
        for bit in operand:
            self.tapecommander.write([bit,"-","-","-"])
            self.tapecommander.move(["L","S","S","S"])
    
    def exec_TEST(self):
        print("Running: ", self.opcode, "- ", self.operand)
        
    def exec_JSON(self, opcode):
        print("Running JSON: ", opcode)
        sequencer = sq.Sequencer(self.opcodestates, self.tapecommander)
        if sequencer.currentstate == "halt":
            print(opcode, " exit code >>", sequencer.currentstate, "<CORRECT>")
        else:
            print(opcode, " exit code >>", sequencer.currentstate, "<ERROR>")

 
    def check(self, opcode, operand):
        if opcode in self.opcodeintern:
            print("Interne OPCODE", opcode)
            if opcode == "PUSH":
                self.exec_PUSH(operand)
            if opcode == "TEST":
                self.exec_TEST()
        
        elif self.contains(opcode) == True:
            print("JSON OPCODE", opcode)
            self.exec_JSON(opcode)
            
        else:
            print("No valid opcode, check your JSON", opcode)
            
 