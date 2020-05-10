import PySimpleGUI as sg

TapeLabels={'ST','RA', 'RB', 'S'}
Tape=""
Tape0=['A','B','C','D','E','F']
TapeHead0=3

Tape1=['Z','X','Y','M','N','G','D','E','F']
TapeHead1=0

Tape2=['A','B','C','D','E','F','Z','X','Y','M','N','G','D','E','F']
TapeHead2=8

Tape3=['1','0','1']
TapeHead3=1
#print(Tape0[TapeHead0])

AllTapes=[Tape0, Tape1, Tape2, Tape3]
AllHeads=[TapeHead0, TapeHead1, TapeHead2, TapeHead3]
print(AllTapes)


def SplitTape(tape, head):
    TapeHeadPos0=(tape[head])
    TH=head
    TapeLeftPos0=Tape.join((tape[:(TH)]))
    TH=head+1
    TapeRightPos0=Tape.join((tape[(TH):]))
    var=[TapeLeftPos0,TapeHeadPos0,TapeRightPos0]
    return var

def TapeCommander(TapeCommand, TapeVal):
    if TapeCommand == 'init':
        print('init!!')
        TapeIndex=0
        for label in TapeLabels:
            AllTapes[TapeIndex]=['_','_','_']
            AllHeads[TapeIndex]=1
            #print(label)
            TapeIndex=TapeIndex+1
    elif TapeCommand == 'move':
        print('move!!')
        TapeIndex=0
        for label in TapeLabels:
            ThisMove=TapeVal[TapeIndex]
            #print(label, ThisMove)
            if ThisMove == 'S':
                print('stay')
            elif ThisMove == 'R':
                print('rechts')
                if AllHeads[TapeIndex] == 0:
                    AllTapes[TapeIndex].insert(0, '_')
                elif AllHeads[TapeIndex] != 0:
                    AllHeads[TapeIndex] = AllHeads[TapeIndex] - 1
            elif ThisMove == 'L':
                print('links')
                if AllHeads[TapeIndex] == (len(AllTapes[TapeIndex])-1):
                    AllTapes[TapeIndex].append('_')
                    AllHeads[TapeIndex]=(AllHeads[TapeIndex]+1)
                elif AllHeads[TapeIndex] != (len(AllTapes[TapeIndex])-1):
                    AllHeads[TapeIndex] = AllHeads[TapeIndex] + 1
                else:
                    print('Invallid move action')     
            TapeIndex=TapeIndex+1
    elif TapeCommand == 'write':
            print('write!!')
            TapeIndex=0
            for label in TapeLabels:
                ThisVal=TapeVal[TapeIndex]
                #print(label, ThisMove)
                if ThisVal == '1':
                    print('write 1')
                    ThisTape=AllTapes[TapeIndex]
                    ThisHead=AllHeads[TapeIndex]
                    ThisTape[ThisHead] = '1'
                elif ThisVal =='0':
                    print('write 0')
                    ThisTape=AllTapes[TapeIndex]
                    ThisHead=AllHeads[TapeIndex]
                    ThisTape[ThisHead] = '0'
                elif ThisVal =='$':
                    print('write $')
                    ThisTape=AllTapes[TapeIndex]
                    ThisHead=AllHeads[TapeIndex]
                    ThisTape[ThisHead] = '$'
                elif ThisVal =='#':
                    print('write $')
                    ThisTape=AllTapes[TapeIndex]
                    ThisHead=AllHeads[TapeIndex]
                    ThisTape[ThisHead] = '#'
                elif ThisVal =='-':
                    print('write - (do not write)')
                    #doe helaal niks'
                else:
                    print('Invallid write character')
                TapeIndex=TapeIndex+1
    elif TapeCommand == 'read':
        print('read!! and update')
    #STACK TAPE
        PrintTape=SplitTape(AllTapes[0], AllHeads[0])
        print(PrintTape)
        window['-TapeLeftPos0-'].update(PrintTape[0]) 
        window['-TapeHeadPos0-'].update(PrintTape[1])
        window['-TapeRightPos0-'].update(PrintTape[2])
    #Register A  
        PrintTape=SplitTape(AllTapes[1], AllHeads[1])
        window['-TapeLeftPos1-'].update(PrintTape[0]) 
        window['-TapeHeadPos1-'].update(PrintTape[1])
        window['-TapeRightPos1-'].update(PrintTape[2])
    #Register B   
        PrintTape=SplitTape(AllTapes[2], AllHeads[2])
        window['-TapeLeftPos2-'].update(PrintTape[0]) 
        window['-TapeHeadPos2-'].update(PrintTape[1])
        window['-TapeRightPos2-'].update(PrintTape[2])
    #STATUS TAPE
        PrintTape=SplitTape(AllTapes[3], AllHeads[3])
        window['-TapeLeftPos3-'].update(PrintTape[0]) 
        window['-TapeHeadPos3-'].update(PrintTape[1])
        window['-TapeRightPos3-'].update(PrintTape[2])
                    
                
                

##Kan weg code
#voorbeeld=SplitTape(AllTapes[0],AllHeads[0])
#Tape0Lengte=len(Tape0)
#TapeHead0=0
#print(voorbeeld, Tape0Lengte)


#exit()
##Kan weg code

def TapeLayout(label, left, head, right, name):
    return [sg.Text(size=(12,1), key=left,justification='right', text=label),
    sg.Text(size=(1,1), key=head,justification='center'),
    sg.Text(size=(12,1), key=right,justification='left'),
    sg.Text(name)]


        
sg.theme('Dark Blue 3')

frame_TapeCommando =[[sg.Button('INIT Tapes', key='INIT' ,font='Courier 10', size=[20,1])],
               [sg.Button('Write Tape', key='write',font='Courier 10', size=[20,1]),
                sg.Input(key='-WST-', size=(1,1)),
                sg.Input(key='-WRA-',size=(1,1)),
                sg.Input(key='-WRB-',size=(1,1)),
                sg.Input(key='-WS-', size=(1,1))],
               [sg.Button('Move Tape', key='move',font='Courier 10', size=[20,1]),
                sg.Input(key='-MST-', size=(1,1)),
                sg.Input(key='-MRA-',size=(1,1)),
                sg.Input(key='-MRB-',size=(1,1)),
                sg.Input(key='-MS-', size=(1,1))],
               [sg.Button('Read Tape', key='Show',font='Courier 10', size=[20,1], bind_return_key='true')]]

frame_TapeInformatie =[
             TapeLayout('Stack',      '-TapeLeftPos0-', '-TapeHeadPos0-','-TapeRightPos0-', 'STACK Tape'),
             TapeLayout('Register A', '-TapeLeftPos1-', '-TapeHeadPos1-','-TapeRightPos1-', 'Register A'),
             TapeLayout('Register B', '-TapeLeftPos2-', '-TapeHeadPos2-','-TapeRightPos2-', 'Register B'),
             TapeLayout('Status',     '-TapeLeftPos3-', '-TapeHeadPos3-','-TapeRightPos3-', 'STATUS')
            ]

layout = [  [sg.Frame('Tape Informatie', frame_TapeInformatie,font='Courier 12')],
            [sg.Frame('Tape Commando', frame_TapeCommando,font='Courier 12')],
            [sg.Button('Exit',font='Courier 10', size=[20,1])]]
           

window = sg.Window('TM Jan Rutger', layout, font='courier 18', keep_on_top = True, no_titlebar=False, grab_anywhere=False)

while True:  # Event Loop
    event, values = window.read(timeout = None)       # can also be written as event, values = window()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'INIT':
        CommandValues=['1','1','1','1']      # De CommandValues worden niet gebruikt maar moeten wel meegegven worden
        TapeCommander('init', CommandValues) # De CommandValues worden niet gebruikt maar moeten wel meegegven worden
        TapeCommander('read', CommandValues) # De CommandValues worden niet gebruikt maar moeten wel meegegven worden
    if event == 'write':
        CommandValues=[values['-WST-'],values['-WRA-'],values['-WRB-'],values['-WS-']]
        #print(CommandValues)
        TapeCommander('write', CommandValues)
        TapeCommander('read', CommandValues) # De CommandValues worden niet gebruikt maar moeten wel meegegven worden
    if event == 'move':
        CommandValues=[values['-MST-'],values['-MRA-'],values['-MRB-'],values['-MS-']]
        #print(CommandValues)
        TapeCommander('move', CommandValues)
        TapeCommander('read', CommandValues) # De CommandValues worden niet gebruikt maar moeten wel meegegven worden
    if event == 'Show':
        CommandValues=['1','1','1','1']      # De CommandValues worden niet gebruikt maar moeten wel meegegven worden
        TapeCommander('read', CommandValues) # De CommandValues worden niet gebruikt maar moeten wel meegegven worden
        


window.close()