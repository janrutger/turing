#https://github.com/PrettyPrinted/youtube_video_code/blob/master/2019/07/31/How%20to%20Convert%20JSON%20Data%20Into%20a%20Python%20Object/json_example/script.py


import json 

class Opcode:
    def __init__(self, Name, States):
        self.Name = Name
        self.States = States
#       self.StateS0 = States['S0']["Rules"][0]
        
    def __repr__(self):
        return self.Name

    def getName(self):
        return self.Name

    def getStates(self):
        return self.States
      

# OpcodeLib = []
# with open('OpcodeData.json', 'r') as json_file:
#     opcodedata = json.loads(json_file.read())
#     for u in opcodedata:
#         OpcodeLib.append(Opcode(**u))     ### Hier begreep ik de voorbeerld niet met ** users_list.append(User(**u))
# 
# 
# print("--------")
# print(OpcodeLib)
# print(type(OpcodeLib))