import json

# # print("een JSON met meerdere unieke commandos")
# # print("een commando bestaat uit meerdere (waarde - actiestrings)")
# # print("waarde Waarde uniek is en wijst naar 1 actie string")
# # print("de actie string bestaat uit een Write, Move en Next state")
# # print()
# # print()
# 
# Dict = {"LDA": [
#     {
#      "waarde" : {
#         "State" : "S0",
#         "ST" : "1",
#         "RA" : "0",
#         "RB" : "1",
#         "S"  : "0"},
#     "actionstring" : {
#         "write" : {
#             "ST" : "1",
#             "RA" : "0",
#             "RB" : "1",
#             "S"  : "0"},
#         "move"  : {
#             "ST" : "1",
#             "RA" : "0",
#             "RB" : "1",
#             "S"  : "0"},
#         "nextstate" : {"newstate" : "S0"}}
#     }]
# }
# Dict1 = {"LDA": [{"microcode" : {"State" : "S0","ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"actionstring" : {"write" : {"ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"move"  : {"ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"nextstate" : {"newstate" : "S0"}}}]}
# jsonstring = json.dumps(Dict1)
# print(jsonstring)
# 
# print()


Dict2 = '{"LDA": [{"microcode" : {"state" : "S0","ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"actionstring" : {"write" : {"ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"move"  : {"ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"nextstate" : {"newstate" : "S0"}}}]}'
MicroCode=json.loads(Dict2)
print(type(MicroCode))

##HOE VOEG IK EEN OBEJECT TOE
#MicroCode["HALT"]={MicroCode["HALT"][0]["microcode"]["state"]}
#MicroCode["HALT"][0]["microcode"]["state"])="xx"

print(len(MicroCode))
state=MicroCode["LDA"][0]["microcode"]["state"]
MicroCode["LDA"][0]["microcode"]["state"]="xx"
#print(type(state))
print(state)
print(len(state))

write=MicroCode["LDA"][0]["actionstring"]["write"]
#print(type(write))
print(write)
print(len(write))

jsonstring = json.dumps(MicroCode)
print(jsonstring) 

exit()


print()

print(MicroCode["LDA"])
print()



