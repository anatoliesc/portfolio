import sys
class SetUp:
    ###Contains supporting funcs that are mostly class based###

    def __init__(self):
        pass

    @classmethod
    def get_input_filename(cls):
        # gets input file name from the cmd line and ret the name
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-i' and i < (len(sys.argv) - 1):
                inputFileName = sys.argv[i + 1]

        return inputFileName

    @classmethod
    def get_output_filename(cls):
        # gets output file name from cmd line and ret the name
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-o' and i < (len(sys.argv) - 1):
                outputFileName = sys.argv[i + 1]

        return outputFileName

    @classmethod
    def import_data_file(cls):
        # gets file name from cmd line and downloads input file & rets the list
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-i' and i < (len(sys.argv) - 1):
                inputFileName = sys.argv[i + 1]

        try:
            instructions = [line.rstrip() for line in open(inputFileName, 'r')]
        except IOError:
            print("could not open input file, is path correct?")

        return instructions

    @classmethod
    def imm_bit_to_32_bit_converter(cls, num, bitsize):
        """Converts binaries of various lengths to a standards 32 bit length
        and returns the converter number."""
        if bitsize < 32:
            negBitMask = 0x800  # figure out if 12 bit num is neg
            negBitMask2 = 0x2000000
            negBitMask3 = 0x40000
            extendMask = 0xFFFFF000
            extendMask2 = 0xFC000000
            extendMask3 = 0xFFF80000
            if bitsize == 12:
                if (negBitMask & num) > 0:
                    num = num | extendMask
                    num = num ^ 0xFFFFFFFF
                    num = num + 1
                    num = num * -1
            elif bitsize == 26:
                if (negBitMask2 & num) > 0:
                    num = num | extendMask2
                    num = num ^ 0xFFFFFFFF
                    num = num + 1
                    num = num * -1
            elif bitsize == 19:
                if (negBitMask3 & num) > 0:
                    num = num | extendMask3
                    num = num ^ 0xFFFFFFFF
                    num = num + 1
                    num = num * -1
        else:
            print("You are using an invalid bit length!")
        return num

    @classmethod
    def immSignedToTwosConverter(cls, num):
        num = ~ num
        num = (num + 0x1)

    @classmethod
    def bin2StringSpaced(cls, s):
        spacedStr = s[0:8] + " " + s[8:11] + " " + s[11:16] + " " + s[16:21] + " " + s[21:26] + " " + s[26:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedD(cls, s):
        spacedStr = s[0:11] + " " + s[11:20] + " " + s[20:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedIM(cls, s):
        spacedStr = s[0:9] + " " + s[9:11] + " " + s[11:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedCB(cls, s):
        spacedStr = s[0:8] + " " + s[8:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedI(cls, s):
        spacedStr = s[0:10] + " " + s[10:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedR(cls, s):
        spacedStr = s[0:11] + " " + s[11:16] + " " + s[16:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedB(cls, s):
        spacedStr = s[0:6] + " " + s[6:32]
        return spacedStr

    @classmethod
    def imm_32_bit_unsigned_to_32_bit_signed_converter(cls, num):
        """converts 32 bit signed, handles neg nums, returns num"""
        if (num & 0x80000000) > 0:  # check for neg.
            num = num ^ 0xFFFFFFFF  # turn binary into hex, cut off sign bit
            num = num + 1
            num = num * -1  # turn num into a negative
        return num  # eventually convert this to decimal for display"""


@classmethod
def decimalToBinary(cls, num):
    """This function converts decimal number to binary & prints it"""
    if num > 1:
        cls.decimalToBinary(num // 2)
    print(num % 2, end='')

    @classmethod
    def binaryToDecimal(cls, binary):
        print("\n")
        print(int(binary, 2))
