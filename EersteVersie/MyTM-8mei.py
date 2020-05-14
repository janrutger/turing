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
                    print(AllTapes[TapeIndex])
                    print(AllHeads[TapeIndex])
                    ThisHead=AllHeads[TapeIndex]
                    ThisTape[ThisHead] = '1'
                    #print(AllTapes[TapeIndex])
                    #print(AllHeads[TapeIndex])
                TapeIndex=TapeIndex+1
                    
                
                

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

layout = [[sg.Text('Tape Informatie')],
            TapeLayout('Stack',      '-TapeLeftPos0-', '-TapeHeadPos0-','-TapeRightPos0-', 'STACK Tape'),
            TapeLayout('Register A', '-TapeLeftPos1-', '-TapeHeadPos1-','-TapeRightPos1-', 'Register A'),
            TapeLayout('Register B', '-TapeLeftPos2-', '-TapeHeadPos2-','-TapeRightPos2-', 'Register B'),
            TapeLayout('Status',     '-TapeLeftPos3-', '-TapeHeadPos3-','-TapeRightPos3-', 'STATUS'),
          
            [sg.Input(key='-TapeCommand-', size=(12,1), focus='true'),
             sg.Input(key='-STval-', size=(1,1)),
             sg.Input(key='-RAval-', size=(1,1)),
             sg.Input(key='-RBval-', size=(1,1)),
             sg.Input(key='-Sval-', size=(1,1))],
          
            [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout, font='courier 20', keep_on_top = True, no_titlebar=False, grab_anywhere=False)

while True:  # Event Loop
    event, values = window.read(timeout = None)       # can also be written as event, values = window()
 #   print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Show':
        TapeCommand=values['-TapeCommand-']
        CommandValues=[values['-STval-'],values['-RAval-'],values['-RBval-'],values['-Sval-']]
        TapeCommander(TapeCommand, CommandValues)
        
        
## Read all tapes en schow
        PrintTape=SplitTape(AllTapes[0], AllHeads[0])
    #    print(PrintTape)
        window['-TapeLeftPos0-'].update(PrintTape[0]) 
        window['-TapeHeadPos0-'].update(PrintTape[1])
        window['-TapeRightPos0-'].update(PrintTape[2])
#        AllHeads[0]=AllHeads[0]+1
#       if AllHeads[0] == len(AllTapes[0]):
#            AllHeads[0]=0
            
        PrintTape=SplitTape(AllTapes[1], AllHeads[1])
    #    print(PrintTape)
        window['-TapeLeftPos1-'].update(PrintTape[0]) 
        window['-TapeHeadPos1-'].update(PrintTape[1])
        window['-TapeRightPos1-'].update(PrintTape[2])
#        AllHeads[1]=AllHeads[1]+1
#       if AllHeads[1] == len(AllTapes[1]):
#           AllHeads[1]=0
            
        PrintTape=SplitTape(AllTapes[2], AllHeads[2])
    #   print(PrintTape)
        window['-TapeLeftPos2-'].update(PrintTape[0]) 
        window['-TapeHeadPos2-'].update(PrintTape[1])
        window['-TapeRightPos2-'].update(PrintTape[2])
#        AllHeads[2]=AllHeads[2]+1
#        if AllHeads[2] == len(AllTapes[2]):
#            AllHeads[2]=0
            
        PrintTape=SplitTape(AllTapes[3], AllHeads[3])
    #    print(PrintTape)
        window['-TapeLeftPos3-'].update(PrintTape[0]) 
        window['-TapeHeadPos3-'].update(PrintTape[1])
        window['-TapeRightPos3-'].update(PrintTape[2])
#        AllHeads[3]=AllHeads[3]+1
#        if AllHeads[3] == len(AllTapes[3]):
#            AllHeads[3]=0            
            
            
        #window['-TapeLeftPos0-'].update(values['-IN-'])
        # above line can also be written without the update specified
        #window['-OUTPUT-'](values['-IN-'])

window.close()