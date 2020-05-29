import unittest

import tape as tape
import tapecommander as tc

import json
import Opcode as o
import state as s
import rule as rl

import Opcodeloader as ol
import interpreter as ip
import sequencer as sq

class TestSequencer(unittest.TestCase):


    def test_sequencers(self):       
        loader = ol.OpcodeLoader()
        loader.load()

        interpreter = ip.Interpreter(loader.get(), "LDA", "nog niet")
#        print(interpreter.opcodestates)       
        sequencer = sq.Sequencer(interpreter.opcodestates)
        

#Verdere uitwerking van de ismatch methode uit sequencer
# #     def ismatch(self, matchwaardes):
# #         self.matchwaardes = matchwaardes
# #         print(self.matchwaardes)
# #         return True ## verder uitwerken

# in serquencer.matchwaardes zit het tapeset object met de waardes uit de json
# voor het ophalen van de huidige tape waardes is de tapecommander
# is dit zo goed, toch?
#        tapecomander = tc.TapeCommander()
# #
# # met getLabels kgrijg ik de tapelabels die gebruik bij het ophalen van de matchwaardes uit het tapeset object
# # en het ophalen van de huidige tape waarde van die tape
#         print(tapecomander.getLabels())
#         matchstatus = True
#        for tapename in tapecomander.getLabels():
#             print(tapename)
#             
#             print(sequencer.matchwaardes.get(tapename))
#             matchval = sequencer.matchwaardes.get(tapename)

# ik ga hier ervanuit dat de HEAD altijd index 1 is in de return van print
# KLOPT DIT?
#             tapeprint = (tapecomander.print(tapename))
#             currentval = tapeprint[1]
#             print(currentval)
# 
#             if matchval != currentval and matchval != "-":
#                 matchstatus = False
#         print(matchstatus)
#         return matchstatus
#         
        
        
#einde oefening       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#        print(sequencer.statelibrary)
#        print(type(sequencer.statelibrary))        
        
#         for state in sequencer.statelibrary:
#             if sequencer.currentstate == state.getState():
#                 print("Requested state found")
#                 currentrules = state.getRules()
#                 print(currentrules)
#                 print(type(currentrules))
#                 return True
#             else:
#                 print("No valid state found")
#                 return False

#        for rule in sequencer.currentrules:
#             print(rule.getMatchWaardes())
#             print(rule.getNieuwWaardes())
#             print(rule.getMove())
#             print(rule.getNieuweStatus())
#             print("-----next (or last) rule------")
            
            
        
     
        

