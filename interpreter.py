# de opcode interpreter is verantwoordelijk voor het uitvoeren van de opcode
# krijgt de opcode(en operand) van de machinegui (later een list can opcodes)
# de interpreter kijkt of de opcode het een (100%) tapecommando is
# in dat geval stuurt de interpreter de opcode en de current tapewaardes naar de sequencer die de states van de uitvoerd via de tapecommander
#
# Als het een intern commando is (dus niet 100% rape commando, zoals het inlezen van de waardes van de stack
# en later het jump commando, wordt het commando door de interpreter uitgevoerd, en stuurt de tapecommander aan.
# Deze commandoś zijn dus niet (zelf) te definieren via de JSON

# De JSON file is gelezen door de knop load JSON in machineui.py
#
import Opcodeloader as ol
import Opcode as oc

class Interpreter():
    def __init__(self, opcodelibrary, opcode, operand):
        self.opcodelibrary = opcodelibrary
      #  print(self.opcodelibrary, "----",  type(self.opcodelibrary))
         
        self.opcode = opcode
        self.operand = operand       
        self.opcodeintern = ["PUSH", "TEST"] # Dit commando set de OPERAND op de stack, en kan niet door states worden afgehadeld
        print(self.opcodeintern, "----",  type(self.opcodeintern))
        self.check()
   
    def contains(self, value):
        print(value)
        print(self.opcodelibrary, "----",  type(self.opcodelibrary))
        i = 0
        for item in self.opcodelibrary:
            print(self.opcodelibrary[i])
            if value == self.opcodelibrary[i]:
                return True
            i = i + 1
        return False
            
   

    def check(self):
        if self.opcode in self.opcodeintern:
            print("Interne OPCODE", self.opcode)
        
        elif self.contains(self.opcode) == True:
            print("JSON OPCODE", self.opcode)
            
        else:
            print("Onbekende opcode", self.opcode.__dict__)
            
            
            
            
            
            
            
            
            
            
            
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
            

         
