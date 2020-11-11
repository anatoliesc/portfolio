from helpers import SetUp


class State:
    dataval = []
    PC = 96
    cycle = 1
    R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, opcode, dataval, addrs, arg1, arg2, arg3, numInstructs, opcodeStr, arg1Str, arg2Str, arg3Str):
        # self.instructions = instrs
        self.opcode = opcode
        self.dataval = dataval
        self.address = addrs
        self.numInstructions = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str

    def getIndexOfMemAddress(self, currAddr):
        index = 0
        for i in self.address:
            if i == currAddr:
                return index
            index += 1

    def incrementPC(self):
        self.pc = self.pc + 4

    def printState(self):

        outputFileName = SetUp.get_output_filename()

        with open(outputFileName + "_sim.txt", 'a') as outFile:

            i = self.getIndexOfMemAddress(self, PC)
            outFile.write("======================\n")
            outFile.write(
                "cycle: " + str(self.cycle) + "\t" + str(self.PC) + "\t" + self.opcodeStr[i] +
                self.arg2Str[i] + self.arg3[i] + "\n")
            outFile.write("\n")
            outFile.write("registers: \n")

            outStr = "r00:"
            for i in range(0, 8):
                outStr = outStr + "\t" + str(self.R[i])
                outFile.write(outStr + "\n")

            outStr = "r08:"
            for i in range(0, 8):
                outStr = outStr + "\t" + str(self.R[i])
                outFile.write(outStr + "\n")

            outStr = "r16:"
            for i in range(0, 8):
                outStr = outStr + "\t" + str(self.R[i])
                outFile.write(outStr + "\n")

            outStr = "r24:"
            for i in range(0, 8):
                outStr = outStr + "\t" + str(self.R[i])
                outFile.write(outStr + "\n")

            outFile.write("\n")

            outFile.write("data:" + "\n")
            for i in range(len(self.dataval)):

                if i % 8 == 0 and i != 0 or i == len(self.dataval):
                    outFile.write(outStr + "\n")

                if i % 8 == 0:
                    outStr = str(self.address[i + self.numInstructions]) + ":" + str(self.dataval[i])

                if i % 8 != 0:
                    outStr = outStr + "\t" + str(self.dataval[i])

            outFile.write(outStr + "\n")
            outFile.close()
