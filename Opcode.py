#https://github.com/PrettyPrinted/youtube_video_code/blob/master/2019/07/31/How%20to%20Convert%20JSON%20Data%20Into%20a%20Python%20Object/json_example/script.py

import state as s
import json 

class Opcode:
    def __init__(self, name, states):
        self.name = name
        print(states)
        self.states = []
        for state in states:
            self.states.append(s.State(state['state'], state["rules"]))
#       self.StateS0 = States['S0']["Rules"][0]
        
    def __repr__(self):
        return self.name

    def getName(self):
        return self.name

    def getStates(self):
        return self.states
      

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