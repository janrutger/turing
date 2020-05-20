import tapeset as ts

class Rule:

    def __init__(self, dict):
        self.matchWaardes = ts.TapeSet(dict["MatchWaardes"])

    def getMatchWaardes(self):
        return self.matchWaardes
