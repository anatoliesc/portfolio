import sys

import masking_constants as MASKs
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
        index = self.address.index(currAddr)

        if index >= self.numInstructions:
            index = index - self.numInstructions
        return index

    def incrementPC(self):
        self.PC = self.PC + 4

    def printState(self):

        outputFileName = SetUp.get_output_filename()

        with open(outputFileName + "_sim.txt", 'a') as outFile:

            i = self.getIndexOfMemAddress(self.PC)
            outFile.write("======================\n")
            outFile.write("cycle: " + str(self.cycle) + "\t" + str(self.PC) + "\t" + self.opcodeStr[i] +
                          self.arg1Str[i] + self.arg2Str[i] + self.arg3Str[i] + "\n")
            outFile.write("\n")
            outFile.write("registers: \n")

            outStr = "r00:"
            for i in range(0, 8):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")

            outStr = "r08:"
            for i in range(8, 16):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")

            outStr = "r16:"
            for i in range(16, 24):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr + "\n")

            outStr = "r24:"
            for i in range(24, 32):
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


class Simulator:

    def __init__(self, opcode, dataval, address, arg1, arg2, arg3, numInstructs, opcodeStr, arg1Str, arg2Str, arg3Str):
        # self.instructions = instrs
        self.opcode = opcode
        self.dataval = dataval
        self.address = address
        self.numInstructions = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str
        self.specialMask = MASKs.specialMask

    def run(self):
        foundBreak = False
        armState = State(self.opcode, self.dataval, self.address, self.arg1, self.arg2, self.arg3,
                         self.numInstructions, self.opcodeStr, self.arg1Str, self.arg2Str, self.arg3Str)

        while not foundBreak:
            jumpAddr = armState.PC
            # get the next instruction
            i = armState.getIndexOfMemAddress(armState.PC)

            # TODO test and delete the need for instructions if self.instrctions[i] ==
            #  '00000000000000000000000000000000' : # NOP this might still be wrong need to test more

            if self.opcode[i] == 0:  # NOP
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go right back to top

            elif 160 <= self.opcode[i] <= 191:  # B
                jumpAddr = jumpAddr + ((self.arg1[i] * 4) - 4)

            elif self.opcode[i] == 1112:  # ADD
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] + armState.R[self.arg2[i]]
                # self.arg3 = self.arg1 + self.arg2
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo armState.cycle += 1

            elif self.opcode[i] == 1624:  # SUB
                armState.R[self.arg3[i]] = (armState.R[self.arg1[i]] - armState.R[self.arg2[i]])
                # .arg3 = self.arg1 - self.arg2
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo armState.cycle += 1

            elif self.opcode[i] == 1690:  # LSR
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] // (2 ** self.arg2[i])
                # self.arg3 = self.arg1 // (2 ** self.arg2)  # arg3 = arg1//2^arg2
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo armState.cycle += 1

            elif self.opcode[i] == 1691:  # LSL
                armState.R[self.arg3[i]] = (armState.R[self.arg1[i]] * (2 ** armState.R[self.arg2[i]]))
                # self.arg3 = self.arg1 * (2 ** self.arg2)  # arg3 = arg1*2^arg2
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo armState.cycle += 1

            elif self.opcode[i] == 1104:  # AND
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] & armState.R[self.arg2[i]]
                # self.arg3 = self.arg1 & self.arg2
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo armState.cycle += 1

            elif self.opcode[i] == 1360:  # ORR
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] | armState.R[self.arg2[i]]
                # self.arg3 = self.arg1 | self.arg2
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo armState.cycle += 1

            elif self.opcode[i] == 1872:  # EOR
                armState.R[self.arg3[i]] = (armState.R[self.arg1[i]] ^ armState.R[self.arg2[i]])
                # self.arg3 = self.arg1 ^ self.arg2
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo rmState.cycle += 1

            elif self.opcode[i] == 1160 or self.opcode[i] == 1161:  # ADDI
                armState.R[self.arg2[i]] = armState.R[self.arg1[i]] + self.arg3[i]  # todo armState.R[self.arg2[i]])
                # self.arg3 = self.arg1 + self.arg2
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo armState.cycle += 1

            elif self.opcode[i] == 1672 or self.opcode[i] == 1673:  # SUBI
                armState.R[self.arg1[i]] = (armState.R[self.arg2[i]] - self.arg3[i])  # todo armState.R[self.arg2[i]])
                # self.arg3 = self.arg1 - self.arg2
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo armState.cycle += 1

            elif self.opcode[i] == 1984:  # STUR
                if self.address[0] > (armState.R[self.arg2[i]] + (4 * self.arg1[i])):
                    sys.exit("Attempting to store in memory below lower bound")
                while self.address[-1] < (armState.R[self.arg2[i]] + (4 * self.arg1[i])):
                    for k in range(8):
                        self.address.append(self.address[-1] + 4)
                        self.dataval.append(0)
                memIndex = armState.getIndexOfMemAddress(armState.R[self.arg2[i]] + (4 * self.arg1[i]))
                armState.dataval[memIndex] = armState.R[self.arg3[i]]

            elif self.opcode[i] == 1986:  # LDUR
                memIndex = armState.getIndexOfMemAddress(armState.R[self.arg2[i]] + (4 * self.arg1[i]))
                armState.R[self.arg3[i]] = armState.dataval[memIndex]

            elif 1440 <= self.opcode[i] <= 1447:  # CBZ
                if armState.R[self.arg2[i]] == 0:
                    jumpAddr = jumpAddr + ((self.arg1[i] * 4) - 4)
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo armState.cycle += 1

            elif 1448 <= self.opcode[i] <= 1455:  # CBNZ
                if armState.R[self.arg2[i]] != 0:
                    jumpAddr = jumpAddr + ((self.arg1[i] * 4) - 4)
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo armState.cycle += 1

            elif self.opcode[i] == 2038:  # Break
                foundBreak = True

            elif 1684 <= self.opcode[i] <= 1687:  # MOVZ
                armState.R[self.arg3[i]] = self.arg2[i] % 0x100000000 >> self.arg1[i]
                # self.arg3 = self.arg2 << self.arg1
                # todo armState.printState()
                # todo armState.incrementPC()  # to do LSR do arg1 % 0x100000000 >> arg2
                # todo armState.cycle += 1

            elif 1940 <= self.opcode[i] <= 1943:  # MOVK
                armState.R[self.arg3[i]] = armState.R[self.arg3[i]] | (self.arg2[i] >> self.arg1[i])
                # self.arg3 = self.arg3 | (self.arg2 << self.arg1)  #CHANGE TO: arg3 = arg3 | (arg2 << arg1)
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo armState.cycle += 1

            elif self.opcode[i] == 1692:  # ASR
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] >> self.arg2[i]
                # todo armState.printState()
                # todo armState.incrementPC()
                # todo armState.cycle += 1


            else:
                print("IN SIM -- UNKNOWN INSTRUCTION ----------- !!!!")

            armState.printState()
            armState.PC = jumpAddr
            armState.incrementPC()
            armState.cycle += 1
