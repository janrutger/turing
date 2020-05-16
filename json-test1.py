import json

# # print("een JSON met meerdere unieke commandos")
# # print("een commando bestaat uit meerdere (waarde - actiestrings)")
# # print("waarde Waarde uniek is en wijst naar 1 actie string")
# # print("de actie string bestaat uit een Write, Move en Next state")
# # print()
# # print()

Dict1={
  "LDA": {
    "States": {
      "S0": {
        "Rules": [
          {
            "MatchWaardes": {
              "ST": "1",
              "RA": "1",
              "RB": "1",
              "S": "1"
            },
            "NieuweWaardes": {
              "ST": "0",
              "RA": "0",
              "RB": "0",
              "S": "0"
            },
            "Move": {
              "ST": "L",
              "RA": "R",
              "RB": "L",
              "S": "S"
            },
            "NieuweStatus": "S0"
          }
        ]
      }
    }
  }
}


print('ADD (met twee states)-------------')
# 
Dict1["ADD"]                ={"States": {"S0": {"Rules": [{"MatchWaardes": {"ST": "1", "RA": "1", "RB": "1", "S": "1"}, "NieuweWaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}, "Move": {"ST": "L", "RA": "R", "RB": "L", "S": "S"}, "NieuweStatus": "S0"}]}}}
Dict1["ADD"]["States"]["S1"]={'Rules': [{'MatchWaardes': {'ST': '1', 'RA': '1', 'RB': '1', 'S': '1'}, 'NieuweWaardes': {'ST': '0', 'RA': '0', 'RB': '0', 'S': '0'}, 'Move': {'ST': 'L', 'RA': 'R', 'RB': 'L', 'S': 'S'}, 'NieuweStatus': 'S0'}]}
#
#print(states)
#print(type(states))
print('HALT (met een state)--------------')
# 
Dict1["HALT"]={"States": {"S0": {"Rules": [{"MatchWaardes": {"ST": "1", "RA": "1", "RB": "1", "S": "1"}, "NieuweWaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}, "Move": {"ST": "L", "RA": "R", "RB": "L", "S": "S"}, "NieuweStatus": "S0"}]}}}


print('toevoegen RULE 2 (LDA, S0)--------------')
rules=Dict1["LDA"]["States"]["S0"]["Rules"]
#
rules.append({'MatchWaardes': {'ST': '1', 'RA': '1', 'RB': '1', 'S': '1'}, 'NieuweWaardes': {'ST': '0', 'RA': '0', 'RB': '0', 'S': '0'}, 'Move': {'ST': 'L', 'RA': 'R', 'RB': 'L', 'S': 'S'}, 'NieuweStatus': 'S0'})
#

print('----RESULT STRING----------')
jsonstring = json.dumps(Dict1)
print(jsonstring)

exit




