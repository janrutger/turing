import json

# # print("een JSON met meerdere unieke commandos")
# # print("een commando bestaat uit meerdere (waarde - actiestrings)")
# # print("waarde Waarde uniek is en wijst naar 1 actie string")
# # print("de actie string bestaat uit een Write, Move en Next state")
# # print()
# # print()

Dict1={
  "LDA": {
    "States": [
      {
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
    ]
  }
}


#Dit is de JSON dump
#  {"LDA": {"S0": {"Microcode": [{"RB": "1", "ST": "1", "RA": "1", "S": "1", "MOVES": {"ST": "L", "RA": "R", "RB": "L", "S": "S"}, "nieuwestatus": {"status": "S0"}, "Nieuwewaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}}]}}}
# einde dump
# 
Commands=Dict1
LDA=Dict1["LDA"]
ListOfStates=Dict1["LDA"]['States'][0]

# 
# 
print('Alle Commando in command.com :', Commands)
print("LDA = ", LDA)
print('Alle States van LDA :', ListOfStates)

#print(Dict1['LDA'])
#Dict1["halt"]=
Dict1["ADD"]={"States": [{"S0": {"Rules": [{"MatchWaardes": {"ST": "1", "RA": "1", "RB": "1", "S": "1"}, "NieuweWaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}, "Move": {"ST": "L", "RA": "R", "RB": "L", "S": "S"}, "NieuweStatus": "S0"}]}}]}
#Dict1["LDA"]["States"].append =[{'S1': {'Rules': [{'MatchWaardes': {'ST': '1', 'RA': '1', 'RB': '1', 'S': '1'}, 'NieuweWaardes': {'ST': '0', 'RA': '0', 'RB': '0', 'S': '0'}, 'Move': {'ST': 'L', 'RA': 'R', 'RB': 'L', 'S': 'S'}, 'NieuweStatus': 'S0'}]}}]
states=Dict1["LDA"]["States"]
states.append({'S0': {'Rules': [{'MatchWaardes': {'ST': '1', 'RA': '1', 'RB': '1', 'S': '1'}, 'NieuweWaardes': {'ST': '0', 'RA': '0', 'RB': '0', 'S': '0'}, 'Move': {'ST': 'L', 'RA': 'R', 'RB': 'L', 'S': 'S'}, 'NieuweStatus': 'S0'}]}})
states.append({'S1': {'Rules': [{'MatchWaardes': {'ST': '1', 'RA': '1', 'RB': '1', 'S': '1'}, 'NieuweWaardes': {'ST': '0', 'RA': '0', 'RB': '0', 'S': '0'}, 'Move': {'ST': 'L', 'RA': 'R', 'RB': 'L', 'S': 'S'}, 'NieuweStatus': 'S0'}]}})

print(type(states))
print('--------------')
#print(type(Dict1["LDA"]["States"]))


#Dict1["LDA"]['States'][0]["S0"]["Rules"]={"MatchWaardes": {"ST": "O", "RA": "1", "RB": "1", "S": "1"}, "NieuweWaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}, "Move": {"ST": "L", "RA": "R", "RB": "L", "S": "S"}, "NieuweStatus": "S0"}
# Dict1['halt']=
# Dict1['halt']['S0']=

#print(Dict1)
print('--------------')
jsonstring = json.dumps(Dict1)
print(jsonstring)

exit




