from string import Template
import PySimpleGUI as sg
import tapecommander as tc
import interpreter as i
import Opcodeloader as ol


class MachineUi:
    def __init__(self):
        self.tapeCommander = tc.TapeCommander()
        self.interpreter = i.Interpreter("opcodelibray", "opcode", "operand")
        self.OpcodeLoader = ol.OpcodeLoader()
      

        sg.theme('Dark Blue 3')
        
        self.frame_Interpreter=[
            [sg.Text('Opcode', size=(15,1),font='Courier 12'),
             sg.Text('Operands', size=(15,1),font='Courier 12')],
            [sg.Input('opcode', key='-OPCODE-', size=(11,1)),
             sg.Input('Not in Use', key='-OPERANDS-',size=(15,1))],
            [sg.Button('Execute', key='Execute',font='Courier 10', size=[12,1], bind_return_key='true'),
             sg.Button('Edit Opcode', key='EditOpcode',font='Courier 10', size=[12,1], bind_return_key='true'),
             sg.Button('LoadJSON', key='LoadJSON',font='Courier 10', size=[12,1], bind_return_key='true')]]

        self.frame_TapeCommando =[
            [sg.Button('INIT Tapes', key='INIT' ,font='Courier 10', size=[20,1])],
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
            [sg.Button('Read Tape', key='Show',font='Courier 10', size=[20,1], bind_return_key='true')]
            ]
        


        self.frame_TapeInformatie =[
             self.tapeLayout('Stack',      '-TapeLeftPos0-', '-TapeHeadPos0-','-TapeRightPos0-', 'STACK Tape'),
             self.tapeLayout('Register A', '-TapeLeftPos1-', '-TapeHeadPos1-','-TapeRightPos1-', 'Register A'),
             self.tapeLayout('Register B', '-TapeLeftPos2-', '-TapeHeadPos2-','-TapeRightPos2-', 'Register B'),
             self.tapeLayout('Status',     '-TapeLeftPos3-', '-TapeHeadPos3-','-TapeRightPos3-', 'STATUS')
            ]

        layout = [
            [sg.Frame('Tape Informatie', self.frame_TapeInformatie,font='Courier 12')],
            [sg.Frame('Tape Commando', self.frame_TapeCommando,font='Courier 12')],
            [sg.Frame('Command Interpreter', self.frame_Interpreter,font='Courier 12')],
            [sg.Button('Exit',font='Courier 10', size=[20,1])]]          

        self.window = sg.Window('Window Title', layout, font='courier 18', keep_on_top = True, no_titlebar=False, grab_anywhere=False)

    def tapeLayout(self, label, left, head, right, name):
        return [sg.Text(size=(12,1), key=left,justification='right', text=label),
        sg.Text(size=(1,1), key=head,justification='center'),
        sg.Text(size=(12,1), key=right,justification='left'),
        sg.Text(name)]

    def updateWindow(self):
        pos = 0;
        for label in self.tapeCommander.getLabels():
            print(label)
            data = self.tapeCommander.print(label)
            self.window[Template('-TapeLeftPos${pos}-').substitute(pos = pos)].update(data[0])
            self.window[Template('-TapeHeadPos${pos}-').substitute(pos = pos)].update(data[1])
            self.window[Template('-TapeRightPos${pos}-').substitute(pos = pos)].update(data[2])
            pos += 1


    def run(self):       
        while True:  # Event Loop
            event, values = self.window.read(timeout = None)       # can also be written as event, values = window()
            print(event, values)
            if event is None or event == 'Exit':
                break
            if event == 'INIT':
                self.tapeCommander = tc.TapeCommander()
            if event == 'write':
                self.tapeCommander.write([values['-WST-'],values['-WRA-'],values['-WRB-'],values['-WS-']])
            if event == 'move':
                self.tapeCommander.move([values['-MST-'],values['-MRA-'],values['-MRB-'],values['-MS-']])
            if event == 'Show':
                self.updateWindow()
            if event == 'LoadJSON':
                loader = ol.OpcodeLoader()
                self.Opcodelibrary = loader.load()
                self.Opcodelibrary = loader.get()
                print(self.Opcodelibrary)
                print(type(self.Opcodelibrary))
            if event == 'Execute':
                try:
                    loader
                except NameError:
                    print("JSON niet geladen")
                else:
                    Opcodelibrary = loader.get()
                    i.Interpreter(self.Opcodelibrary, values['-OPCODE-'], values['-OPERANDS-'])
               
               
#                 loader = ol.OpcodeLoader()
                  
#                 if Opcodelibrary == "":
#                      print("JSON-file not loaded")
#                 else:


        self.window.close()
