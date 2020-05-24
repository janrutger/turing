import state as st
import rule as rl

class Sequencer():
    def __init__(self, statelibrary):
        self.statelibrary = statelibrary
        self.currentstate = ["start"]
        self.check()
