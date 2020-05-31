import tape as t

class TapeCommander:

    def __init__(self):
        self.TapeLabels={'ST','RA', 'RB', 'S'}
        self.Tape=""

##De volgorde lijkt omgekeerd dan op het scherm getoont wordt
#wat je neit merkt als je alles gelijk inititaleert, en daarna werkt het oke
#    def inittapes(self):
        self.tapes = [
            t.Tape('ST', ['S','T','_','_'], 3),
            t.Tape('RA', ['R','A','_','_'], 3),
            t.Tape('RB', ['R','B','_','_'], 3),
            t.Tape('S', ['_','S','_','_'], 3)]

    def getLabels(self):
        return self.TapeLabels

    def move(self, moves):
        index = 0
        for tape in self.tapes:
           tape.move(moves[index]) 
           index += 1

    def write(self, values):
        index = 0
        for tape in self.tapes:
            tape.write(values[index])
            index += 1

    def get(self, name):
        for tape in self.tapes:
            if tape.hasName(name):
                return tape
        print('tape not found')

    def print(self, name):
        tape = self.get(name)
        return tape.print()
