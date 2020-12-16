from string import Template
import PySimpleGUI as sg
import threading

from assembler import assembler as ASM
from mmu       import mmu       as MMU
from cpu       import executer  as ex


memory    = MMU.MMU()
executer  = ex.Executer(memory) 
assembler = ASM.Assembler()
ALLTAPES = ["ST", "RA", "RB", "S"] 
THREAD = False
BINfile = ""

def runner(pc):
    executer.run_memory(pc)

def updateTapeInfo():
    pos = 0;
    #result = executer.run_commando("PRINT", ALLTAPES)
    result = executer.refreshTapes(ALLTAPES)
    for tape in result.keys():
        data = result[tape]
        window[Template('-TapeLeftPos${pos}-').substitute(pos = pos)].update(data[0])
        window[Template('-TapeHeadPos${pos}-').substitute(pos = pos)].update(data[1])
        window[Template('-TapeRightPos${pos}-').substitute(pos = pos)].update(data[2])
        pos += 1

# UI definitions
sg.theme('Dark Blue 3')

def tapeLayout(label, left, head, right, name):
    return [
        sg.Text(size=(12,1), key=left, justification='right', text=label),
        sg.Text(size=(1,1),  key=head, justification='center'),
        sg.Text(size=(12,1), key=right,justification='left'),
        sg.Text(name)
        ]
    

frame_TapeInformatie =[
    tapeLayout('Stack',      '-TapeLeftPos0-', '-TapeHeadPos0-','-TapeRightPos0-', 'Stack'),
    tapeLayout('Register A', '-TapeLeftPos1-', '-TapeHeadPos1-','-TapeRightPos1-', 'A Register'),
    tapeLayout('Register B', '-TapeLeftPos2-', '-TapeHeadPos2-','-TapeRightPos2-', 'B Register'),
    tapeLayout('Status',     '-TapeLeftPos3-', '-TapeHeadPos3-','-TapeRightPos3-', 'Status')
    ]

frame_MemInformatie=[
    [sg.Text('#', size=(12,1), key='-adres-'),
     sg.Text('Opcode', size=(12,1), key='-opcode-'),
     sg.Text('Operand', size=(12,1), key='-operand-')]
    ]



layout = [
    [sg.Multiline("Dit wordt standaard ouput/error", size=(65, 5))],
    [sg.FileBrowse("Open",font='Courier 10', size=[10,1], key="-open-"),
     sg.Button("Compile", font='Courier 10', size=[10,1], key="-compile-"),
     sg.Button("Load", font='Courier 10', size=[10,1], key="-load-"),
     sg.Button("Run", font='Courier 10',  size=[10,1], key="-run-")],
    [sg.Frame('Tape Informatie', frame_TapeInformatie,font='Courier 12')],
    [sg.Frame('Memory Stack', frame_MemInformatie, font='Courier 12')],
    [sg.Button("Shutdown", font='Courier 10', size=[10,1], key='-shutdown-')]
]


# Create the Window
window = sg.Window('Christopher (TM)', layout)
window.Finalize()
window['-compile-'].update(disabled=True)
window['-load-'].update(disabled=True)
window['-run-'].update(disabled=True)

# Event Loop to process "events"
while True:             
    event, values = window.read(timeout=1000)
    print(event, values)
    #print(values['-open-'])
    if event == sg.WIN_CLOSED or event == '-shutdown-':
        break
    if (values['-open-']) != '':
        window['-compile-'].update(disabled=False)
    if event == '-compile-':
        ASMfile = assembler.readASM(values['-open-'])
        BINfile = assembler.compile(ASMfile)
    if BINfile != "" and THREAD == False:
            window['-load-'].update(disabled=False)
    if event == '-load-':
        memory.loadMem(BINfile)
        window['-run-'].update(disabled=False)
    if event == '-run-':
        pc = 0
        window['-load-'].update(disabled=True)
        window['-run-'].update(disabled=True)
        
        job = threading.Thread(target=runner, args=((pc,)))
        job.start()
        THREAD = True
    
    updateTapeInfo()


    

window.close()