print('een JSON met meerdere unieke commandos')
print('een commando bestaat uit meerdere (waarde - actiestrings)')
print('waarde Waarde uniek is en wijst naar 1 actie string')
print('de actie string bestaat uit een Write, Move en Next state')
print()
print()

Dict = {'LDA': [
    {
     'waarde' : {
        'State' : 'S0',
        'ST' : '1',
        'RA' : '0',
        'RB' : '1',
        'S'  : '0'},
    'actionstring' : {
        'write' : {
            'ST' : '1',
            'RA' : '0',
            'RB' : '1',
            'S'  : '0'},
        'move'  : {
            'ST' : '1',
            'RA' : '0',
            'RB' : '1',
            'S'  : '0'},
        'nextstate' : {'newstate' : 'S0'}}
    }]
}



print(type(Dict), 'alle commandos')
print(Dict)
print()

ListOfStates=(Dict['LDA'])
print(type(ListOfStates), 'Alle States van 1 commando')
print(ListOfStates)
print()
# # 
State=(ListOfStates[0])
print(type(State), 'Loop door de lijst met States en Match waarde met de TAPES')
print(State)
print()
# # 
waarde=(State['waarde'])
print(type(waarde), 'Als je de juiste waarde hebt gevonden, pak de actie string -zelfde list index als waarde-')
print(waarde)
print()

Acties=(State['actionstring'])
print(type(Acties), 'De actie string heeft een write een move en een nextstate')
print(Acties)
print()

write=(Acties['write'])
print(type(write), 'de schrijf actie')
print(write)
print()

move=(Acties['write'])
print(type(move), 'de move actie')
print(move)
print()

nextstate=(Acties['nextstate'])
print(type(nextstate), ' de next stae')
print(move)
print()



 
