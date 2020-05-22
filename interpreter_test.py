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
        interpreter = ip.Interpreter(loader.get(), "TEST", "nog niet")
        print(interpreter.opcode)
        print(interpreter.operand)
        print(interpreter.opcodelibrary)
        print(type(interpreter.opcodelibrary))
        print(interpreter.contains(interpreter.opcode))

        self.assertEqual(interpreter.contains("LDA"), True)
        self.assertEqual(interpreter.contains("MOVE"), True)
        self.assertEqual(interpreter.contains("DD"),  False)
        #print(interpreter.opcodelibrary[1])
        
#         if interpreter.opcode in interpreter.opcodelibrary:
#             print("match")
#         else:
#             print("NO match")
#             
            
            
            
            
            
#         for name in interpreter.opcodelibrary:
#             if name == interpreter.opcode:
#                 print("match")
#             else:
#                 print("NO match")
#             
        
        #print(type(interpreter.opcode))