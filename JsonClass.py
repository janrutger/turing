import json 

class Opcodes:
    def __init__(self, Name, States):
        self.Name = Name
        self.States = States
        
    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict[0])

    def __repr__(self):
        return f'<Opcodes { self.Name }>'


        
        
        
# ###        
# json_string ="""[
#   {
#     "Name": "LDA",
#     "States": {
#       "S0": {
#         "Rules": [
#           {
#             "MatchWaardes": {
#               "ST": "1",
#               "RA": "1",
#               "RB": "1",
#               "S": "1"
#             },
#             "NieuweWaardes": {
#               "ST": "0",
#               "RA": "0",
#               "RB": "0",
#               "S": "0"
#             },
#             "Move": {
#               "ST": "L",
#               "RA": "R",
#               "RB": "L",
#               "S": "S"
#             },
#             "NieuweStatus": "S0"
#           },
#           {
#             "MatchWaardes": {
#               "ST": "1",
#               "RA": "1",
#               "RB": "1",
#               "S": "1"
#             },
#             "NieuweWaardes": {
#               "ST": "0",
#               "RA": "0",
#               "RB": "0",
#               "S": "0"
#             },
#             "Move": {
#               "ST": "L",
#               "RA": "R",
#               "RB": "L",
#               "S": "S"
#             },
#             "NieuweStatus": "S0"
#           }
#         ]
#       },
#       "S1": {
#         "Rules": [
#           {
#             "MatchWaardes": {
#               "ST": "1",
#               "RA": "1",
#               "RB": "1",
#               "S": "1"
#             },
#             "NieuweWaardes": {
#               "ST": "0",
#               "RA": "0",
#               "RB": "0",
#               "S": "0"
#             },
#             "Move": {
#               "ST": "L",
#               "RA": "R",
#               "RB": "L",
#               "S": "S"
#             },
#             "NieuweStatus": "S0"
#           },
#           {
#             "MatchWaardes": {
#               "ST": "1",
#               "RA": "1",
#               "RB": "1",
#               "S": "1"
#             },
#             "NieuweWaardes": {
#               "ST": "0",
#               "RA": "0",
#               "RB": "0",
#               "S": "0"
#             },
#             "Move": {
#               "ST": "L",
#               "RA": "R",
#               "RB": "L",
#               "S": "S"
#             },
#             "NieuweStatus": "S0"
#           }
#         ]
#       }
#     }
#   }
# ]"""

# Opcodes = Opcodes.from_json(json_string)
# print(Opcodes)
# print(Opcodes.Name)
# print(Opcodes.States)

Opcodeslist = []
with open('OpcodeData.json', 'r') as json_file:
    opcodedata = json.loads(json_file.read())
    for u in opcodedata:
        Opcodeslist.append(opcodedata[0])


print("--------")
print(Opcodeslist)
print(Opcodeslist.Name)

