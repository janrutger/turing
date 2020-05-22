import unittest
import tape as tape
import json
import Opcode as o
import state as s
import interpreter as ip
import Opcodeloader as ol

class TestTape(unittest.TestCase):

    def setUp(self):
        with open("state-test-data.json", 'r') as json_file:
            self.data = json.loads(json_file.read())

    def test_load_opcode(self):
        loader = ol.OpcodeLoader()
        loader.load()
        interpreter = ip.Interpreter(loader.get(), o.Opcode(**self.data), "")
        interpreter.