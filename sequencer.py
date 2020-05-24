import state as st
import rule as rl

class Sequencer():
    def __init__(self, statelibrary):
        self.statelibrary = statelibrary
        self.currentstate = ["PUSH", "TEST"]
        self.opcode = opcode
        self.opcodestates = []         
        self.operand = operand
        self.check()
