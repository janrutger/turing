
class TapeSet:

    def __init__(self, dict):
        self.tapeset = dict

    def getST(self):
        return self.get("ST")

    def getRA(self):
        return self.get("RA")

    def getRB(self):
        return self.get("RB")

    def getS(self):
        return self.get("S")

    def get(self, key):
        return self.tapeset[key]