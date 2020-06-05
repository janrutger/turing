import unittest

import tape as tape
import tapecommander as tc
import machineui as ui
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
        tapecommander = tc.TapeCommander()
        interpreter = ip.Interpreter(loader.get(), tapecommander)
        
        print(tapecommander.print("ST"))
        print(tapecommander.print("RA"))
        print(tapecommander.print("RB"))
        print(tapecommander.print("S"))
        
        interpreter.check("PUSH", "101#10011")
        
#        interpreter = ip.Interpreter(loader.get(), "PUSH", "101#10011", tapecommander)      
# 
        print(tapecommander.print("ST"))
        print(tapecommander.print("RA"))
        print(tapecommander.print("RB"))
        print(tapecommander.print("S"))
        
        interpreter.check("LDA", "not relevant")
#         
#         interpreter = ip.Interpreter(loader.get(), "LDA", "101#10011", tapecommander)      
# # 
        print(tapecommander.print("ST"))
        print(tapecommander.print("RA"))
        print(tapecommander.print("RB"))
        print(tapecommander.print("S"))
