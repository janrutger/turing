import unittest
import tape as tape
import json
import Opcode as o
import state as s
import interpreter as ip
import Opcodeloader as ol

class TestInterpreter(unittest.TestCase):

#     def setUp(self):
#         with open("state-test-data.json", 'r') as json_file:
#             self.data = json.loads(json_file.read())

    def test_interpreter_opcode(self):
        loader = ol.OpcodeLoader()
        loader.load()
        #interpreter = ip.Interpreter(loader.get(), o.Opcode(**self.data), "")
        interpreter = ip.Interpreter(loader.get(), "MOVE", "nog niet")
        print(interpreter.opcode)
        print(interpreter.operand)
        print(interpreter.opcodelibrary)
        print(type(interpreter.opcodelibrary))
        print(interpreter.contains(interpreter.opcode))

        self.assertEqual(interpreter.contains("LDA"), True)
        self.assertEqual(interpreter.contains("MOVE"), True)
        self.assertEqual(interpreter.contains("DD"),  False)
        
        print("----")
        i = 0
        for opcode in interpreter.opcodelibrary:
            neededStates = []
            if interpreter.opcode == opcode.getName():
                for state in opcode.getStates():
                    RulesVanState=state.getRules()
                    print(state, " -", RulesVanState)
                    
                    neededStates.append(state)
                    
                print(neededStates, "--> ", type(neededStates))
                return True
            i = i + 1