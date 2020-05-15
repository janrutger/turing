# de opcode interpreter is verantwoordelijk voor het uitvoeren van de opcode
# krijgt de opcode(en operand) van de machinegui (later een list can opcodes)
# de interpreter kijkt of de opcode het een (100%) tapecommando is
# in dat geval stuurt de interpreter de opcode en de current tapewaardes naar de sequencer die de states van de uitvoerd via de tapecommander
#
# Als het een intern commando is (dus niet 100% rape commando, zoals het inlezen van de waardes van de stack
# en later het jump commando, wordt het commando door de interpreter uitgevoerd, en stuurt de tapecommander aan.
# Deze commandoś zijn dus niet (zelf) te definieren via de JSON

# Bij aanroepen van opcodeinterpreter wordt de JSON gelezen
# (maar wellichtdat het inlzen van de JSNO ergens anders moet, nu leest hij het bestand bij ieder commando)
#
import sequencer as s
import tapecommander as tc

class OpcodeInterpreter():
    def __init__(self):
        self.JSONfromTape={"LDA": {"S0": {"Microcode": [{"RB": "1", "ST": "1", "RA": "1", "S": "1", "MOVES": {"ST": "L", "RA": "R", "RB": "L", "S": "S"}, "nieuwestatus": {"status": "S0"}, "Nieuwewaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}}]}, "S1": {"Microcode": [{"RB": "1", "ST": "1", "RA": "1", "S": "1", "MOVES": {"ST": "L", "RA": "R", "RB": "L", "S": "S"}, "nieuwestatus": {"status": "S0"}, "Nieuwewaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}}]}}, "ADD": {"S0": {"Microcode": [{"RB": "1", "ST": "1", "RA": "1", "S": "1", "MOVES": {"ST": "L", "RA": "R", "RB": "L", "S": "S"}, "nieuwestatus": {"status": "S0"}, "Nieuwewaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}}]}}}
        
        print(self.JSONfromTape)
    
#     pass
# 
# 
# def __init__(self):
#         self.TapeLabels={'ST','RA', 'RB', 'S'}
#         self.Tape=""