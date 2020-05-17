import json
import Opcode as OC

class OpcodeLoad():
    def __init__(self):
        self.opcodeLib = []
        self.Opcode=OC.Opcode("Name", "States")

    
    def reload(self):
        self.OpcodeLib = []
        with open('OpcodeData.json', 'r') as json_file:
            opcodedata = json.loads(json_file.read())
            for u in opcodedata:
                self.OpcodeLib.append(self.Opcode(**u))     ### Hier begreep ik de voorbeerld niet met ** users_list.append(User(**u))

#         JSONdict=json.loads(self.JSONfromFile)
#         return JSONdict
        
            