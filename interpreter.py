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
import opcode as oc

class Interpreter():
    def __init__(self, opcodelibrary, opcode, operand):
        self.opcodelibrary = opcodelibrary
        self.opcode = opcode
        self.operand = operand       
        self.opcodeintern = ["PUSH"] # Dit commando set de OPERAND op de stack, en kan niet door states worden afgehadeld
        self.libopcode = self.opcodelibrary[0]
        self.print()
        
    def print(self):
        print(self.opcodelibrary)
        print(self.libopcode)
        print(type(self.libopcode))
        print(self.opcode)
        print(self.operand)
        print(self.opcodeintern)

        

