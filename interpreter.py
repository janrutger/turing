import Opcodeloader as ol
import Opcode as oc

class Interpreter():
    def __init__(self, opcodelibrary, opcode, operand):
        self.opcodelibrary = opcodelibrary
        self.opcodeintern = ["PUSH", "TEST"]
        self.opcode = opcode
        self.opcodestates = []         
        self.operand = operand
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
            print("Onbekende opcode", self.opcode)
            
 