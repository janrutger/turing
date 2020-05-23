import unittest
import tape as tape
import json
import Opcode as o
import state as s
import interpreter as ip
import Opcodeloader as ol

class TestInterpreter(unittest.TestCase):


    def test_interpreter_opcode(self): 
        loader = ol.OpcodeLoader()
        loader.load()

        interpreter = ip.Interpreter(loader.get(), "LDA", "nog niet")


        self.assertEqual(interpreter.contains("LDA"), True)
        self.assertEqual(interpreter.contains("MOVE"), True)
        self.assertEqual(interpreter.contains("DD"),  False)
        
        print("----")
        print(interpreter.opcodestates)
