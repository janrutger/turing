import rule as r

class State:

    def __init__(self, dict):
        self.state = dict['state']
        self.rules = self.init(dict['rules'])

    def init(self, dict):
        rules = []
        for o in dict:
            rules.append(self.initOne(o))
        return rules

    def initOne(self, dict):
        return r.Rule(dict)
        
    def getState(self):
        return self.state

    def getRules(self):
        return self.rules