import json

class JSONfile():
    def __init__(self):
        self.JSONfromFile="""{
                        "LDA":
                           {"S0": {"Microcode": [
                                 {"RB": "1", "ST": "1", "RA": "1", "S": "1",
                                    "MOVES": {"ST": "L", "RA": "R", "RB": "L", "S": "S"},
                                    "nieuwe status": {"status": "S0"},
                                    "Nieuwewaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}}]},
                            "H": {"Microcode": [
                                     {"RB": "1", "ST": "1", "RA": "1", "S": "1",
                                      "MOVES": {"ST": "L", "RA": "R", "RB": "L", "S": "S"},
                                      "nieuwestatus": {"status": "S0"},
                                      "Nieuwewaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}}]}},
                        "ADD":
                           {"S0": {"Microcode": [
                               {"RB": "1", "ST": "1", "RA": "1", "S": "1",
                                "MOVES": {"ST": "L", "RA": "R", "RB": "L", "S": "S"},
                                "nieuwestatus": {"status": "S0"},
                                "Nieuwewaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}}]}}}"""
    
    def reload(self):
        JSONdict=json.loads(self.JSONfromFile)
        return JSONdict
        
