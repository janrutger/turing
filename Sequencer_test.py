import unittest
import tape as tape
import json
import Opcode as o
import state as s
import rule as rl

import Opcodeloader as ol
import interpreter as ip
import sequencer as sq

class TestSequencer(unittest.TestCase):


    def test_sequencers(self):       
        loader = ol.OpcodeLoader()
        loader.load()

        interpreter = ip.Interpreter(loader.get(), "LDA", "nog niet")
#        print(interpreter.opcodestates)
        
        sequencer = sq.Sequencer(interpreter.opcodestates)
#        print(sequencer.statelibrary)
#        print(type(sequencer.statelibrary))        
        
        for state in sequencer.statelibrary:
            if sequencer.currentstate == state.getState():
                print("state found")
                currentrules = state.getRules()
                print(currentrules)
                print(type(currentrules))
                return True
            else:
                print("No valid state found")
                return False
            
        
     
        
# 
# 
#         self.assertEqual(interpreter.contains("LDA"), True)
#         self.assertEqual(interpreter.contains("MOVE"), True)
#         self.assertEqual(interpreter.contains("DD"),  False)
#         
#         print("----")
#         print(interpreter.opcodestates)
