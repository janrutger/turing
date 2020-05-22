#https://github.com/PrettyPrinted/youtube_video_code/blob/master/2019/07/31/How%20to%20Convert%20JSON%20Data%20Into%20a%20Python%20Object/json_example/script.py

import state as s
import json 

class Opcode:
    def __init__(self, name, states):
        self.name = name
        self.states = []
        for state in states:
            self.states.append(s.State(state))
        
    def __repr__(self):
        return self.name

    def getName(self):
        return self.name

    def getStates(self):
        return self.states
      

