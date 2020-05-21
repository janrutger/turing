import unittest
import tape as tape
import json
import Opcode as o
import state as s

class TestTape(unittest.TestCase):

    def setUp(self):
        with open("state-test-data.json", 'r') as json_file:
            self.data = json.loads(json_file.read())


    def test_load_opcode(self):
        opcode = o.Opcode(**self.data)
        self.assertEqual(opcode.getName(), "LDA")
        self.assertEqual(len(opcode.states), 1)
        state = opcode.getStates()[0]
        self.assertEqual(state.getState(), "S0")
        rules = state.getRules()
        self.assertEqual(len(rules), 2)
        rule = rules[0]
        print("RULE:", rule.__dict__)
        tapeSet = rule.getMatchWaardes()
        print("MatchWaardes: ", tapeSet.__dict__)
        self.assertEqual(tapeSet.getST(), "1")
