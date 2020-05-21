import tapeset as ts
import move as m

class Rule:

    def __init__(self, dict):
        self.matchWaardes = ts.TapeSet(dict["MatchWaardes"])
        self.nieuweWaardes = ts.TapeSet(dict["NieuweWaardes"])
        self.move = m.Move(dict["Move"])
        self.nieuweStatus = dict["NieuweStatus"]

    def getMatchWaardes(self):
        return self.matchWaardes

    def getNieuwWaardes(self):
        return self.nieuweWaardes

    def getMove(self):
        return self.move

    def getNieuweStatus(self):
        return self.nieuweWaardes
