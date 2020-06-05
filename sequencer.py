import state as st
import rule as rl
import tapecommander as tc

class Sequencer():
    def __init__(self, tapecommander):
#     def __init__(self, statelibrary, tapecommander):
#        self.statelibrary = statelibrary
        self.currentstate = "start"
        self.tapecommander = tapecommander
#        self.findcurrentrules()

        
    def findcurrentrules(self, statelibrary):
        self.statelibrary = statelibrary
        if self.currentstate == "halt":
            self.dohousekeeping()
            
        else:
            for state in self.statelibrary:
                if self.currentstate == state.getState():
                    print("Requested state found: ", self.currentstate)
                    self.currentrules = state.getRules()
                    self.execmatch()
                    return #deze return voorkomt verder zoeken als match gevonden is
    #            else: #deze else is niet goed
            print("No valid state found, check your JSON")
    #                return 

    def dohousekeeping(self):
        print("Entering halt state, do some housekeeping")
        return

    def ismatch(self, matchwaardes):
        #tapecommander = self.tapecommander
        self.matchwaardes = matchwaardes
        matchstatus = True
        for tapename in self.tapecommander.getLabels():
            matchval = self.matchwaardes.get(tapename)     
            tapeprint = (self.tapecommander.print(tapename))
            currentval = tapeprint[1]     # ik ga hier er vanuit de de tapewaarde van het head altijd in index 1 zit
            if matchval != currentval and matchval != "-":
                matchstatus = False
        return matchstatus
        
    def setnew(self, newvalues):
#        tapecommander = self.tapecommander()
        self.newvalues = newvalues
        writeval = {}
        for tapename in self.tapecommander.getLabels():
            writeval[tapename] = self.newvalues.get(tapename)
        print("Write new values on tapes") 
        self.tapecommander.write([writeval['ST'],writeval['RA'],writeval['RB'],writeval['S']])
        
    def domove(self, moves):
#        tapecommander = self.tapecommander()
        self.moves = moves
        moveval = {}
        for tapename in self.tapecommander.getLabels():
            moveval[tapename] = self.moves.get(tapename)
        print("Perform moves of tapes") 
        self.tapecommander.move([moveval['ST'],moveval['RA'],moveval['RB'],moveval['S']])
    
    def execmatch(self):
        for rule in self.currentrules:
            if self.ismatch(rule.getMatchWaardes()) == True:
                print("Matching rule found")
                self.setnew(rule.getNieuwWaardes())
                self.domove(rule.getMove())
                print("Get next state to run")
                self.currentstate = rule.getNieuweStatus()
                self.findcurrentrules(self.statelibrary)
                return
#                print(self.currentstate) #een eigen method getNewCurrentstate
#                return #new current state
#             else: ## Deze else is niet de juiste plek, de no found hoort onder de FOR loop
        print("No matching rule found, check your JSON")
#        return False
            