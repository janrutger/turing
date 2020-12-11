from string import Template
import PySimpleGUI as sg
import threading
from assembler import assembler as ASM
import executer as ex
 

# Design pattern 2 - First window remains active

executer  = ex.Executer() 
assembler = ASM.Assembler()
ALLTAPES = ["ST", "RA", "RB", "S"]   

def runner(opcode, operand):
    executer.run_commando(opcode, operand)
def runner2(program):
    executer.run_program(program)

sg.theme('Dark Blue 3')

frame_Interpreter=[
    #[sg.Text('Opcode', size=(15,1),font='Courier 12'),
    # sg.Text('Operand', size=(15,1),font='Courier 12')],
    #[sg.Input(key='-OPCODE-', size=(11,1)),
    # sg.Input(key='-OPERANDS-',size=(15,1))],
    [sg.Button('Run Program', key='RunProg',font='Courier 10', size=[45,1], bind_return_key='true'),]
    ]

def tapeLayout(label, left, head, right, name):
    return [
        sg.Text(size=(12,1), key=left,justification='right', text=label),
        sg.Text(size=(1,1), key=head,justification='center'),
        sg.Text(size=(12,1), key=right,justification='left'),
        sg.Text(name)
        ]

def updateTapeInfo():
    pos = 0;
    #result = executer.run_commando("PRINT", ALLTAPES)
    result = executer.refreshTapes(ALLTAPES)
    for tape in result.keys():
        data = result[tape]
        tapeWindow[Template('-TapeLeftPos${pos}-').substitute(pos = pos)].update(data[0])
        tapeWindow[Template('-TapeHeadPos${pos}-').substitute(pos = pos)].update(data[1])
        tapeWindow[Template('-TapeRightPos${pos}-').substitute(pos = pos)].update(data[2])
        pos += 1

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
 

tapeWindow = sg.Window('Christopher (TM)', tapeLayout)

win2_active = False
while True: #event loop tapewindow (window 1)
    tapeEvent, tapeValues = tapeWindow.read(timeout=100)
    #print("tapewin",tapeEvent, tapeValues)
    if tapeEvent == sg.WIN_CLOSED or tapeEvent == 'Exit':
        break

    updateTapeInfo()
    
    if not win2_active: #define window 2
        win2_active = True
        commandLayout = [
            [sg.Frame('Command Line', frame_Interpreter,font='Courier 12')]
            #[sg.Button('Exit',font='Courier 10', size=[10,1])]
            ] 
        
        commandWindow = sg.Window('Interpreter', commandLayout, no_titlebar=False)

    if win2_active: #event loop commandwindow (window 2)
        CommandEvent, CommandValues = commandWindow.read(timeout=100)
        #print("commandwin",tapeEvent, tapeValues)
        if CommandEvent == sg.WIN_CLOSED or CommandEvent == 'Exit':
            win2_active  = False
            commandWindow.close()
        if CommandEvent == "Execute":
            opcode = str.upper(CommandValues["-OPCODE-"])
            if CommandValues["-OPERANDS-"] == "":
                operand = None
            else:
                raw = int(CommandValues["-OPERANDS-"])
                operand = bin(raw)[2:]

            job = threading.Thread(target=runner, args= (opcode, operand,) )
            job.start()
        if CommandEvent == "RunProg":
            ASMfile    = assembler.readASM("/home/pi/projects/turing2/assembler/jrk.asm")
            BINprogram = assembler.compile(ASMfile)

            job = threading.Thread(target=runner2, args=((BINprogram,)))
            job.start()

            #executer.run_program(program)