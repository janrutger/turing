import json

# # print("een JSON met meerdere unieke commandos")
# # print("een commando bestaat uit meerdere (waarde - actiestrings)")
# # print("waarde Waarde uniek is en wijst naar 1 actie string")
# # print("de actie string bestaat uit een Write, Move en Next state")
# # print()
# # print()

Dict1={
  "LDA": {
    "S0": {
      "Mocrocode": [
        {
          "RB": "1",
          "ST": "1",
          "RA": "1",
          "S": "1",
          "MOVES": {
            "ST": "L",
            "RA": "R",
            "RB": "L",
            "S": "S"
          },
          "nieuwestatus": {
            "status": "S0"
          },
          "Nieuwewaardes": {
            "ST": "0",
            "RA": "0",
            "RB": "0",
            "S": "0"
          }
        }
      ]
    }
  }
}

# 
# Commands=Dict1
# LDA=Dict1["LDA"]
# microcodelda=Dict1["LDA"]["S0"]["microcode"]
# NU=Dict1["LDA"]["S0"]["microcode"]['huidigewaardes']
# move=Dict1["LDA"]["S0"]["microcode"]["input"]["MOVES"]
# Nieuwewaardes=Dict1["LDA"]["S0"]["microcode"]["input"]["Nieuwewaardes"]
# nieuwestatus=Dict1["LDA"]["S0"]["microcode"]["input"]["nieuwestatus"]
# 
# 
# # print('Alle Commando in command.com :', Commands)
# # print('Alle States van LDA :', LDA)
# # print('Alle combinaties binnen een state (S0) :', microcodelda)
# # print('De hudige waardes die horen bij een geldige combinatie :', NU)
# # print('De nieuwe waardes die horen bij een geldige combinatie :', Nieuwewaardes)
# # print('De tape beweging die horen bij een geldige combinatie :', move)
# # print('De volgende status die hoort bij een geldige combinatie :', nieuwestatus)


#print(Dict1['LDA'])
#Dict1["halt"]=
#Dict1["LDA"]={"S0": {"ST": "1", "RA": "1", "RB": "1", "S": "1", "input": {"MOVES": {"ST": "L", "RA": "R", "RB": "L", "S": "S"}, "Nieuwewaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}, "nieuwestatus": {"status": "S0"}}}}
#Dict1["LDA"]["S1"]={"ST": "0", "RA": "1", "RB": "1", "S": "1", "input": {"MOVES": {"ST": "L", "RA": "R", "RB": "L", "S": "S"}, "Nieuwewaardes": {"ST": "0", "RA": "0", "RB": "0", "S": "0"}, "nieuwestatus": {"status": "S0"}}}

# Dict1['halt']=
# Dict1['halt']['S0']=

#print(Dict1)

jsonstring = json.dumps(Dict1)
print(jsonstring)

exit


















# # Dict1 = {"LDA": [{"microcode" : {"State" : "S0","ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"actionstring" : {"write" : {"ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"move"  : {"ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"nextstate" : {"newstate" : "S0"}}}]}
# # jsonstring = json.dumps(Dict1)
# # print(jsonstring)
# # 
# # print()
# 
# #Dict2 = '{"LDA": [{"microcode" : {"state" : "S0","ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"actionstring" : {"write" : {"ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"move"  : {"ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"nextstate" : {"newstate" : "S0"}}}]}'
# 
# Dict2 = '{"LDA": [{"microcode" : {"state" : "S0","ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"actionstring" : {"write" : {"ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"move"  : {"ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"nextstate" : {"newstate" : "S0"}}}]}'
# MicroCode=json.loads(Dict2)
# print(type(MicroCode))
# 
# 
# 
# #NewVal={"HALT": [{"microcode": {"state": "xx", "ST": "1", "RA": "0", "RB": "1", "S": "0"}, "actionstring": {"write": {"ST": "1", "RA": "0", "RB": "1", "S": "0"}, "move": {"ST": "1", "RA": "0", "RB": "1", "S": "0"}, "nextstate": {"newstate": "S0"}}}]}
# #MicroCode = MicroCode + NewVal
# ##HOE VOEG IK EEN OBEJECT TOE
# MicroCode=dict({MicroCode["HALT"][0]["microcode"]["state"]})
# #MicroCode["HALT"][0]["microcode"]["state"])="xx"
# 
# print(len(MicroCode))
# state=MicroCode["LDA"][0]["microcode"]["state"]
# 
# #print(type(state))
# print(state)
# print(len(state))
# 
# write=MicroCode["LDA"][0]["actionstring"]["write"]
# #print(type(write))
# print(write)
# print(len(write))
# 
# MicroCode["LDA"][0]["microcode"]["state"]="xx"
# jsonstring = json.dumps(MicroCode)
# print(jsonstring) 
# 
# exit()
# 
# 
# print()
# 
# print(MicroCode["LDA"])
# print()



