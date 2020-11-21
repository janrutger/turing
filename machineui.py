from string import Template
import PySimpleGUI as sg
import executer as ex



class MachineUi:
    def __init__(self):
        self.ecexuter = ex.Executer() 
        self.ALLTAPES = ["ST", "RA", "RB", "S"]     

        sg.theme('Dark Blue 3')
        
        self.frame_Interpreter=[
            [sg.Text('Opcode', size=(15,1),font='Courier 12'),
             sg.Text('Operand', size=(15,1),font='Courier 12')],
            [sg.Input(key='-OPCODE-', size=(11,1)),
             sg.Input(key='-OPERANDS-',size=(15,1))],
            [sg.Button('Execute', key='Execute',font='Courier 10', size=[45,1], bind_return_key='true'),]
            ]

        
        self.frame_TapeInformatie =[
             self.tapeLayout('Stack',      '-TapeLeftPos0-', '-TapeHeadPos0-','-TapeRightPos0-', 'STACK Tape'),
             self.tapeLayout('Register A', '-TapeLeftPos1-', '-TapeHeadPos1-','-TapeRightPos1-', 'Register A'),
             self.tapeLayout('Register B', '-TapeLeftPos2-', '-TapeHeadPos2-','-TapeRightPos2-', 'Register B'),
             self.tapeLayout('Status',     '-TapeLeftPos3-', '-TapeHeadPos3-','-TapeRightPos3-', 'STATUS')
            ]

        layout = [
            [sg.Frame('Tape Informatie', self.frame_TapeInformatie,font='Courier 12')],
            [sg.Frame('Command Interpreter', self.frame_Interpreter,font='Courier 12')],
            [sg.Button('Exit',font='Courier 10', size=[10,1])]]          

        self.window = sg.Window('Christopher (TM)', layout, font='courier 18', keep_on_top = True, no_titlebar=False, grab_anywhere=False)

    def tapeLayout(self, label, left, head, right, name):
        return [sg.Text(size=(12,1), key=left,justification='right', text=label),
        sg.Text(size=(1,1), key=head,justification='center'),
        sg.Text(size=(12,1), key=right,justification='left'),
        sg.Text(name)]

    def updateTapeInfo(self):
        pos = 0;
        result = self.ecexuter.run_commando("PRINT", self.ALLTAPES)
        for tape in result.keys():
            data = result[tape]
            self.window[Template('-TapeLeftPos${pos}-').substitute(pos = pos)].update(data[0])
            self.window[Template('-TapeHeadPos${pos}-').substitute(pos = pos)].update(data[1])
            self.window[Template('-TapeRightPos${pos}-').substitute(pos = pos)].update(data[2])
            pos += 1


    def run(self):       
        while True:  # Event Loop
            event, values = self.window.read(timeout = 1500)       # can also be written as event, values = window()
            print(event, values)
            if event is None or event == 'Exit':
                break
            if event == "Execute":
                opcode = str.upper(values["-OPCODE-"])
                if values["-OPERANDS-"] == "":
                    operand = None
                else:
                    raw = int(values["-OPERANDS-"])
                    operand = bin(raw)[2:]
                self.ecexuter.run_commando(opcode, operand)
                
            self.updateTapeInfo()


               
        
        self.window.close()