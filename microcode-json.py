import json

#Start stae is altijd S0 en bij finisch is de slot state H

#Ieder commando bestaat uit 1 commandostring bestaat
#een commandostring bestaat uit meerdere State (+read values)
# en geeft een actiestring die bestaat uit een Write, Move en Next actie

#het LDA commando laad de eerste waarde van de Stack i Register A
 
x={
    'Commando':'LDA',
    'MicroCode': [
        {'state':'S0','ST':'1','RA':'0', 'RB':'0', 'S' :'1',
         'ActionString':[
                {
                    'write' :{'ST':'0','RA':'1', 'RB':'1', 'S' :'0'},
                    'Move'  :{'ST':'L','RA':'S', 'RB':'R', 'S' :'L'},
                    'Next'  :{'State':'S0'}
                }
                ]
        }
        ]   
}

y=json.loads(x)

#print(json.dumps(x, indent=4))
type(x)

exit()

# ik zou een functie schrijven die de micro code van van het commando ophaalt
# def StateMachine('command')
# 
# als return waarde geeft hij of sw sequense succesvol tot status Halt heeft volbracht
# of dat de sequnce onderbroken is (inhet geval van een deadlock, of tijdens het bouwen)
# 
# Deze functie roept een andere functie aan die de juiste actie string opzoekt
# als geen actiestring gevonden worden, of als er meer actiestrings gevonden worden komt er eeb (multiline) edit popup
# def action(state, waardes)
# return (Next state, Nieuwe Waardes)
# Wanneer er een geldige actiestring gevonden wordt wordt deze uitgevoerd met de TapeComander
# en worden de huidie waarde en de volgende actie string terug gegeven en wordt de functie opnnieuw aangeroepen
# To hij tot status halt is aangekomen en StateMachine brengt de tape naar de startpositie en geeft een succesvol terug
# ..........en wacht op het volgende commando

