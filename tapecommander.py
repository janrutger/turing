import tape as t


class  Tapecommander:
    def __init__(self):
        alltapesnames = {"ST", "RA", "RB", "S"}
        self.alltapes = {}
        for tape in alltapesnames:
            self.alltapes[tape] = t.Tape(tape, ['_','_','_','_'], 2)

    def get_tapeValues(self, tapeList):
        tapeValues = {}
        for tape in tapeList:
            thisTape = self.alltapes[tape]
            resultValue = thisTape.read()
            tapeValues[tape] = resultValue
        return(tapeValues)

    def do_write(self, writeValues):
        tapeList = list(writeValues.keys())
        for tape in tapeList:
            thisTape = self.alltapes[tape]
            thisTape.write(writeValues[tape])

    def do_move(self, moveValues):
        tapeList = list(moveValues.keys())
        for tape in tapeList:
            thisTape = self.alltapes[tape]
            thisTape.move(moveValues[tape])
    
    def get_head(self, tapelist):
        head = {}
        for tape in tapelist:
            currenttape = self.alltapes[tape]
            resultvalue = currenttape.getHead()
            head[tape] = resultvalue
        return(head)