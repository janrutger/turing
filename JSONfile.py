import json

class JSONfile():
    def __init__(self):
        self.JSONfromFile="""{
            "LDA": {"States": [
                {"S0": {
                    "Rules": [
                        {"MatchWaardes": {"ST": "1", "RA": "1", "RB": "1", "S": "1"},
                         "NieuweWaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"},
                         "Move": {"ST": "L", "RA": "R", "RB": "L", "S": "S"},
                         "NieuweStatus": "S0"}]}},
                {"S1":
                 {"Rules": [
                    {"MatchWaardes": {"ST": "1", "RA": "1", "RB": "1", "S": "1"},
                     "NieuweWaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"},
                     "Move": {"ST": "L", "RA": "R", "RB": "L", "S": "S"},
                     "NieuweStatus": "S0"}]}}
                ]},
            "ADD": {"States":[
                {"S0":
                  {"Rules": [
                    {"MatchWaardes": {"ST": "1", "RA": "1", "RB": "1", "S": "1"},
                     "NieuweWaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"},
                     "Move": {"ST": "L", "RA": "R", "RB": "L", "S": "S"},
                     "NieuweStatus": "S0"}]}}]}}"""

    
    def reload(self):
        JSONdict=json.loads(self.JSONfromFile)
        return JSONdict
        
