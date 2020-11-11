import sys
import disassembler
import simulator

# for i in range(len(sys.argv)):
#    if(sys.argv[i]) == '-i' and i < (len(sys.argv) - 1):
#        inputFileName = sys.argv[i + 1]
#        print(inputFileName)
#    elif sys.argv[i] == '-o' and i < (len(sys.argv) - 1):
#        outputFileName = sys.argv[i + 1]

mydis = disassembler.Disassembler()
output = {}
output = mydis.run()
mydis.print()

mysim = simulator.Simulator(**output)
mysim.run()

# advice from Dr. Lakomski: comment out everything except print so my print
#               and my run config are working
#      if you put a breakpoint between outputFilename = SetUp.get_output_filename()
#      pink commented lines can be uncommented
