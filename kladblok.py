from string import Template
import PySimpleGUI as sg
import executer as ex

# Design pattern 2 - First window remains active

ecexuter = ex.Executer() 
ALLTAPES = ["ST", "RA", "RB", "S"]   

sg.theme('Dark Blue 3')

frame_Interpreter=[
    [sg.Text('Opcode', size=(15,1),font='Courier 12'),
     sg.Text('Operand', size=(15,1),font='Courier 12')],
    [sg.Input(key='-OPCODE-', size=(11,1)),
     sg.Input(key='-OPERANDS-',size=(15,1))],
    [sg.Button('Execute', key='Execute',font='Courier 10', size=[45,1], bind_return_key='true'),]
    ]

def tapeLayout(self, label, left, head, right):
    return [
        sg.Text(size=(12,1), key=left,justification='right', text=label),
        sg.Text(size=(1,1), key=head,justification='center'),
        sg.Text(size=(12,1), key=right,justification='left')
        ]

frame_TapeInformatie =[
    tapeLayout('Stack',      '-TapeLeftPos0-', '-TapeHeadPos0-','-TapeRightPos0-', 'Stack'),
    tapeLayout('Register A', '-TapeLeftPos1-', '-TapeHeadPos1-','-TapeRightPos1-', 'A Register'),
    tapeLayout('Register B', '-TapeLeftPos2-', '-TapeHeadPos2-','-TapeRightPos2-', 'B Register'),
    tapeLayout('Status',     '-TapeLeftPos3-', '-TapeHeadPos3-','-TapeRightPos3-', 'Status')
    ]

tapeLayout = [
    [sg.Frame('Tape Informatie', frame_TapeInformatie,font='Courier 12')],
    [sg.Button('Exit',font='Courier 10', size=[10,1])]
    ] 
 

tapeWindow = sg.Window('Window 1', tapeLayout)

win2_active = False
while True: #event loop tapewindow (window 1)
    tapeEvent, tapeValues = tapeWindow.read(timeout=100)
    if tapeEvent == sg.WIN_CLOSED or tapeEvent == 'Exit':
        break

    if not win2_active: #define window 2
        win2_active = True
        commandLayout = [
            [sg.Frame('Command Interpreter', frame_Interpreter,font='Courier 12')]
            #[sg.Button('Exit',font='Courier 10', size=[10,1])]
            ] 
        
        commandWindow = sg.Window('Window 2', commandLayout)

    if win2_active: #event loop commandwindow (window 2)
        CommandEvent, CommandValues = commandWindow.read(timeout=100)
        if CommandEvent == sg.WIN_CLOSED or CommandEvent == 'Exit':
            win2_active  = False
            commandWindow.close()