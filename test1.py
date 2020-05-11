Dict = {'Command':[
    {
    'LDA': [
    {
#   'state'  : 'S0',
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
    }]}]
}


print(Dict)
print(type(Dict))

command=(Dict['Command'])
print(command)
print(type(command))

LDA=(command[0])
print(LDA)
print(type(LDA))

nn=(LDA['LDA'])
print(nn)
print(type(nn))

yy=(nn[0])
print(yy)
print(type(yy))

waarde=(yy['waarde'])
print(waarde)
print(type(waarde))

Action=(yy['actionstring'])
print(Action)
print(type(Action))


WriteAction=(Action['write'])
print(WriteAction)
print(type(WriteAction))
MoveAction=(Action['move'])
print(MoveAction)
print(type(MoveAction))
Nextstep=(Action['nextstate'])
print(Nextstep)
print(type(Nextstep))


 
