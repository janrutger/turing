import Opcodeloader as ol
import Opcode as oc
import sequencer as sq

class Interpreter():
    def __init__(self, opcodelibrary, opcode, operand, tapecommander):
        self.opcodelibrary = opcodelibrary
        self.opcodeintern = ["PUSH", "TEST"]
        self.opcode = opcode
        self.opcodestates = []         
        self.operand = operand
        self.tapecommander = tapecommander
        self.check()
        
    def contains(self, value):
        for item in self.opcodelibrary:          
            if value == item.getName():
                self.opcodestates = item.getStates()
                return True
        return False

    def exec_PUSH(self):
        print("Running: ", self.opcode, "- ", self.operand)
    
    def exec_TEST(self):
        print("Running: ", self.opcode, "- ", self.operand)
        
    def exec_JSON(self):
        print("Running JSON: ", self.opcode)
        sequencer = sq.Sequencer(self.opcodestates, self.tapecommander)
        if sequencer.currentstate == "halt":
            print(self.opcode, " exit code >>", sequencer.currentstate, " == CORRECT")
        else:
            print(self.opcode, " exit code >>", sequencer.currentstate, " == ERROR ")

 
    def check(self):
        if self.opcode in self.opcodeintern:
            print("Interne OPCODE", self.opcode)
            if self.opcode == "PUSH":
                self.exec_PUSH()
            if self.opcode == "TEST":
                self.exec_TEST()
        
        elif self.contains(self.opcode) == True:
            print("JSON OPCODE", self.opcode)
            self.exec_JSON()
            
        else:
            print("No valid opcode, check your JSON", self.opcode)
            
 