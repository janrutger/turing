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

Dict2 = '{"LDA": [{"microcode" : {"State" : "S0","ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"actionstring" : {"write" : {"ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"move"  : {"ST" : "1","RA" : "0","RB" : "1","S"  : "0"},"nextstate" : {"newstate" : "S0"}}}]}'
MicroCode=json.loads(Dict2)
print(MicroCode)

print()

print(MicroCode["LDA"])
print()


jsonstring = json.dumps(MicroCode)
print(jsonstring) 
