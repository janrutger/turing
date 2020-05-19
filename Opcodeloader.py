import json
import Opcode as oc

class OpcodeLoader():
    def __init__(self, file = None):
        self.opcode=oc.Opcode("Name", "States")
        self.file = file or 'OpcodeData.json'
        self.opcodeLib="" #self.load()
    
    def load(self):
        self.opcodeLib = []
        with open(self.file, 'r') as json_file:
            opcodedata = json.loads(json_file.read())
            for o in opcodedata:
                self.opcodeLib.append(oc.Opcode(**o))

    def get(self):
            naam=self.opcodeLib
            return naam

    
    
    

