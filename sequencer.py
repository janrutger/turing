import state as st
import rule as rl

class Sequencer():
    def __init__(self, statelibrary):
        self.statelibrary = statelibrary
        self.currentstate = "start"
        self.findcurrentrules()
        
    def findcurrentrules(self):
        for state in self.statelibrary:
            if self.currentstate == state.getState():
                print("Requested state found")
                self.currentrules = state.getRules()
                self.execmatch()
#                print(self.currentrules)
#                print(type(self.currentrules))
                return True
            else:
                print("No valid state found")
                return False
    
    def ismatch(self, matchwaardes):
        return True
    
    def execmatch(self):
        for rule in self.currentrules:
            if self.ismatch(rule.getMatchWaardes()) == True:
                print("Set new value")
                print("Do move")
                print("Get new state")
                return
#             else: ## Deze else is niet de juiste plek, de no found hoort onder de FOR loop
        print("No matching rule found, check your JSON")
        return False
            