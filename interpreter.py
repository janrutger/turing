import Opcodeloader as ol
import Opcode as oc

class Interpreter():
    def __init__(self, opcodelibrary, opcode, operand):
        self.opcodelibrary = opcodelibrary      
        self.opcode = opcode
        self.operand = operand       
        self.opcodeintern = ["PUSH", "TEST"] # Dit commando set de OPERAND op de stack, en kan niet door states worden afgehadeld
        self.check()
        
    def contains(self, value):
        i = 0
        for item in self.opcodelibrary:
            if value == item.getName():
                return True
            i = i + 1
        return False
#
    def exec_PUSH(self):
        print("Running: ", self.opcode, "- ", self.operand)
    
    def exec_TEST(self):
        print("Running: ", self.opcode, "- ", self.operand)
#    
# 
    def check(self):
        if self.opcode in self.opcodeintern:
            print("Interne OPCODE", self.opcode)
            if self.opcode == "PUSH":
                self.exec_PUSH()
            if self.opcode == "TEST":
                self.exec_TEST()
        
        elif self.contains(self.opcode) == True:
            print("JSON OPCODE", self.opcode)
            
        else:
            print("Onbekende opcode", self.opcode)
            
            
            
            
            
            
            
            
            
            
            
            #for waarde in self.opcodelibrary:
                
        
 
 
 
 
 
 
 
 
#print("Onbekende opcode", self.opcode)
 
 #if any(obj['shape'] == 'square' for obj in shapes):
           
#              for waarde in self.opcodelibrary:
#                  if waarde.name == self.opcode:
#                      print("JSON OPCODE", self.opcode)
# #                 
#  
#         if listOfStrings.count('at') > 0 :    
        
        
#elif any(opcodex == self.opcode for opcodex in self.opcodelibrary) == True:
        #elif self.opcodelibrary.count(self.opcode) > 0:
        
#        elif self.opcode in enumerate(self.opcodelibrary):
#        elif self.opcode in self.opcodelibrary:
            #print("JSON OPCODE", self.opcode)      
            

         
