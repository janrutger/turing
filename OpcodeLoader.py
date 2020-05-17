import json
import Opcode as oc

class OpcodeLoader():
    def __init__(self):
        self.opcodeLib = []
        self.opcode=oc.Opcode("Name", "States")
        self.defaultOpcodesFile = 'opcode-data.json'
    
    def reload(self, file = None):
        self.opcodeLib = []
        with open(file or self.defaultOpcodesFile, 'r') as json_file:
            opcodedata = json.loads(json_file.read())
            for u in opcodedata:
                self.opcodeLib.append(oc.Opcode(**u))     ### Hier begreep ik de voorbeerld niet met ** users_list.append(User(**u))
#         JSONdict=json.loads(self.JSONfromFile)
#         return JSONdict

    def getOpcodes(self):
        return self.opcodeLib
            