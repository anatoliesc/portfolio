from helpers import SetUp
import os
import masking_constants as MASKs
import sys


class Disassembler:
    # these lists contain the info for each instr decoded to enable the dis. file
    opcodeStr = []
    instrSpaced = []
    arg1 = []
    arg2 = []
    arg3 = []
    arg1Str = []
    arg2Str = []
    arg3Str = []
    dataval = []
    rawdata = []
    address = []
    numInstructs = 0

    def run(self):
        instructions = []
        instructions = SetUp.import_data_file()
        # for i in instructions:
        # print(i)

        outputFilename = SetUp.get_output_filename()

        print("raw output filename is ", outputFilename)

        # print(hex(MASKs.bMask))
        # print(bin(MASKs.bMask))
        # print(f'{MASKs.bMask:032b}')

        # create an address list with appropriate length
        for i in range(len(instructions)):
            self.address.append(96 + (i * 4))

        opcode = []

        # create an opcode list by selecting the left 11 bits
        for z in instructions:
            opcode.append(int(z, base=2) >> 21)

        for i in range(len(opcode)):
            self.numInstructs = self.numInstructs + 1
            #       REGISTER OPCODES
            if opcode[i] == 1112:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ADD")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1624:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("SUB")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1690:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("LSR")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))
            elif opcode[i] == 1691:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("LSL")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))
            elif opcode[i] == 1692:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ASR")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))
            elif opcode[i] == 1104:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("AND")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1360:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ORR")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1872:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("EOR")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))

            #       IMMEDIATE OPCODES

            elif opcode[i] == 1160 or opcode[i] == 1161:
                self.instrSpaced.append(SetUp.bin2StringSpacedI(instructions[i]))
                self.opcodeStr.append("ADDI")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg3.append(
                    SetUp.imm_bit_to_32_bit_converter((int(instructions[i], base=2) & MASKs.imMask) >> 10, 12))
                self.arg1Str.append("\tR" + str(self.arg2[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg3[i]))
            elif opcode[i] == 1672 or opcode[i] == 1673:
                self.instrSpaced.append(SetUp.bin2StringSpacedI(instructions[i]))
                self.opcodeStr.append("SUBI")
                self.arg1.append((int(instructions[i], base=2) & MASKs.rdMask))
                self.arg2.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKs.imMask) >> 10)
                self.arg1Str.append("\tR" + str(self.arg1[i]))
                self.arg2Str.append(", R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg3[i]))
            #       BRANCH OPCODES
            elif 160 <= opcode[i] <= 191:
                self.instrSpaced.append(SetUp.bin2StringSpacedB(instructions[i]))
                self.opcodeStr.append("B")
                self.arg1.append(
                    SetUp.imm_bit_to_32_bit_converter((int(instructions[i], base=2) & MASKs.bMask), 26))
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("\t#" + str(self.arg1[i]))
                self.arg2Str.append("")
                self.arg3Str.append("")
            #       MEMORY OPCODES
            elif opcode[i] == 1984:
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("STUR")
                self.arg1.append((int(instructions[i], base=2) & MASKs.addrMask) >> 12)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", [R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]) + "]")
            elif opcode[i] == 1986:
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("LDUR")
                self.arg1.append((int(instructions[i], base=2) & MASKs.addrMask) >> 12)
                self.arg2.append((int(instructions[i], base=2) & MASKs.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", [R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]) + "]")
            #       CB INSTRUCTIONS
            elif 1440 <= opcode[i] <= 1447:
                self.instrSpaced.append(SetUp.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBZ")
                self.arg1.append(
                    SetUp.imm_bit_to_32_bit_converter(((int(instructions[i], base=2) & MASKs.addr2Mask) >> 5), 19))
                self.arg2.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg3.append(0)
                self.arg1Str.append("\tR" + str(self.arg2[i]))
                self.arg2Str.append(", #" + str(self.arg1[i]))
                self.arg3Str.append("")
            elif 1448 <= opcode[i] <= 1455:
                self.instrSpaced.append(SetUp.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBNZ")
                self.arg1.append(
                    SetUp.imm_bit_to_32_bit_converter(((int(instructions[i], base=2) & MASKs.addr2Mask) >> 5), 19))
                self.arg2.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg3.append(0)
                self.arg1Str.append("\tR" + str(self.arg2[i]))
                self.arg2Str.append(", #" + str(self.arg1[i]))
                self.arg3Str.append("")

            #       IM INSTRUCTIONS
            elif 1684 <= opcode[i] <= 1687:
                self.opcodeStr.append("MOVZ")
                self.instrSpaced.append(SetUp.bin2StringSpacedIM(instructions[i]))
                self.arg1.append((int(instructions[i], base=2) & MASKs.imsftMask) >> 21)
                self.arg2.append((int(instructions[i], base=2) & MASKs.imdataMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", " + str(self.arg2[i]) + ", LSL ")
                self.arg3Str.append(str(self.arg1[i]*16))
            elif 1940 <= opcode[i] <= 1943:
                self.opcodeStr.append("MOVK")
                self.instrSpaced.append(SetUp.bin2StringSpacedIM(instructions[i]))
                self.arg1.append((int(instructions[i], base=2) & MASKs.imsftMask) >> 21)
                self.arg2.append((int(instructions[i], base=2) & MASKs.imdataMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKs.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", " + str(self.arg2[i]) + ", LSL ")
                self.arg3Str.append(str(self.arg1[i]*16))

            # NOP INSTRUCTION

            elif instructions[i] == '00000000000000000000000000000000':  # this might still be wrong need to test more
                self.instrSpaced.append(SetUp.bin2StringSpaced(instructions[i]))
                self.opcodeStr.append("NOP")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")

            # Finding the BREAK instruction

            elif opcode[i] == 2038 and (int(instructions[i], base=2) & MASKs.specialMask) == 2031591:
                self.instrSpaced.append(SetUp.bin2StringSpaced(instructions[i]))
                self.opcodeStr.append("BREAK")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                print("breaking")
                break
            else:
                self.opcodeStr.append("unknown")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                print("i =: " + str(i))
                print("opcode =: " + str(opcode[i]))
                sys.exit("You have found an unknown instruction, investigate NOW")

            # Now read the memory lines .... .... ....
        for addri in range(self.numInstructs, len(opcode)):
            self.rawdata.append(str(instructions[addri]))
            self.dataval.append(SetUp.imm_32_bit_unsigned_to_32_bit_signed_converter(int(instructions[addri], base=2)))

        return{#"instructions": instructions,
        "opcode": opcode,
        "opcodeStr": self.opcodeStr,
        "arg1": self.arg1,
        "arg1Str": self.arg1Str,
        "arg2": self.arg2,
        "arg2Str": self.arg2Str,
        "arg3": self.arg3,
        "arg3Str": self.arg3Str,
        "dataval": self.dataval,
        "address": self.address,
        "numInstructs": self.numInstructs}
    def print(self):
        # write to a file
        outFile = open(SetUp.get_output_filename() + "_dis.txt", 'w')
        for i in range(self.numInstructs):
            outFile.write((self.instrSpaced[i] + '\t' + str(self.address[i]) + '\t' + self.opcodeStr[i]
                           + self.arg1Str[i] + self.arg2Str[i] + self.arg3Str[i] + '\n'))

        for i in range(len(self.dataval)):
            outFile.write(
                self.rawdata[i] + '\t' + str(self.address[self.numInstructs + i]) + '\t' + str(self.dataval[i]) + '\n')

        outFile.close()
