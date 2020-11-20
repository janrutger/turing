


class Exec_no_opcode:
    def __init__(self, tapecommander):
        self.tapecommander = tapecommander


    def push(self, operand):
        moveLeft = {"ST": "L"}
        writeSeperator = {"ST": "#"}
        writeBit = {}
        self.tapecommander.do_move(moveLeft)
        self.tapecommander.do_write(writeSeperator)
        for bit in operand:
            writeBit["ST"] = bit
            self.tapecommander.do_move(moveLeft)
            self.tapecommander.do_write(writeBit)
        return("oke")    

    def print(self, tapeList):
        resultValue = {}
        resultValue = self.tapecommander.print_tape(tapeList)
        return(resultValue)


    def pull(self):
        return("0")           #do something smarter over here