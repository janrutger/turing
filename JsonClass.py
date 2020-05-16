import json 

class Opcodes:
    def __init__(self, Name, States):
        self.Name = Name
        self.States = States
        
    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict[0])

    def __repr__(self):
        return f'<Opcodes { self.Name }>'
      
    

Opcodeslist = []
with open('OpcodeData.json', 'r') as json_file:
    opcodedata = json.load(json_file.read())
    for u in opcodedata:
        Opcodeslist.append(opcodedata[0])


print("--------")
print(Opcodeslist)


