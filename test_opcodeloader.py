import unittest
import Opcodeloader as o
import json

class TestTape(unittest.TestCase):

    def setUp(self):
        pass

    def test_loader(self):
        ol = o.OpcodeLoader()
        ol.load()
        data = ol.get()
        self.assertEqual(len(data), 2)
        for opcode in data:
            print("OPCODE:", opcode.__dict__)
            self.goPrint(opcode.getStates())

    def goPrint(self, states):
        for state in states:
            print("STATE:", state.__dict__)
            self.goPrintRules(state.getRules())

    def goPrintRules(self, rules):
        for rule in rules:
            print("RULE:", rule.__dict__)
            print("MatchWaardes:", rule.getMatchWaardes().__dict__)
            print("NieuwWaardes:", rule.getNieuwWaardes().__dict__)
            print("Move:", rule.getMove().__dict__)
            print("NieuweStatus:", rule.getNieuwWaardes().__dict__)

        