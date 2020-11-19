import tape as t


class  Tapecommander:
    def __init__(self):
        alltapesnames = {"ST", "RA", "RB", "S"}
        self.alltapes = {}
        for tape in alltapesnames:
            self.alltapes[tape] = t.Tape(tape, ['_','_','_','_'], 2)

    
    def get_head(self, tapelist):
        head = {}
        for tape in tapelist:
            currenttape = self.alltapes[tape]
            resultvalue = currenttape.getHead()
            head[tape] = resultvalue
        return(head)