import queue

# Some notes from my learnings on how this system should work
# normal mode:
# mode 0
# position mode - cause parameters to be interpreted as positions
# ie. parameter is 50, value is stored in address 50
# mode 1
# immediate mode - parameter is interpreted as value
# ie. parameter is 50, value is simply 50
# stored in the opcode
# opcode is the right most two digit, example 1002 is 02 is the opcode
#
# example code
# 1002
# multiply
# 0 - position mode for first parameter
# 1 - immediate mode for second parameter


opcode = '3,225,1,225,6,6,1100,1,238,225,104,0,1101,34,7,225,101,17,169,224,1001,224,-92,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1102,46,28,225,1102,66,83,225,2,174,143,224,1001,224,-3280,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,19,83,224,101,-102,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1001,114,17,224,1001,224,-63,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,60,46,225,1101,7,44,225,1002,40,64,224,1001,224,-1792,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,80,27,225,1,118,44,224,101,-127,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1102,75,82,225,1101,40,41,225,1102,22,61,224,1001,224,-1342,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,102,73,14,224,1001,224,-511,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,344,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,374,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,389,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,404,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,419,1001,223,1,223,1107,677,677,224,102,2,223,223,1006,224,434,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,449,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,464,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,479,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,494,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,509,1001,223,1,223,7,677,226,224,1002,223,2,223,1006,224,524,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,539,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,569,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,599,1001,223,1,223,7,226,226,224,102,2,223,223,1006,224,614,1001,223,1,223,8,226,226,224,1002,223,2,223,1006,224,629,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,644,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,659,101,1,223,223,107,226,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226'
opcodearr = opcode.split(',')

# noun and verb and output
c = opcodearr[0]


def addOpCode(refA, refB, out, array, C, B):
    # dealing with position versus immediate mode
    if C == 1:
        paramA = refA
    else:
        paramA = int(array[refA])
    if B == 1:
        paramB = refB
    else:
        paramB = int(array[refB])

    array[out] = str(paramA + paramB)


def multOpCode(refA, refB, out, array, C, B):
    # dealing with position versus immediate mode
    if C == 1:
        paramA = refA
    else:
        paramA = int(array[refA])
    if B == 1:
        paramB = refB
    else:
        paramB = int(array[refB])

    array[out] =  str(paramA * paramB)


def storeCode(valA, input, array):
    array[valA] = input


def outputCode(valA, array):
    print(array[valA])


def IntCodeProcessor(array, input):
    x = 0
    while x < len(array):

        # account for position/immediate modes
        currentop = array[x]
        arrlen = len(currentop)
        currentop = currentop.rjust(5, '0')
        DE = int(currentop[3:5])
        C = int(currentop[2])
        B = int(currentop[1])
        A = int(currentop[0])

        if DE == 1:
            addOpCode(int(array[x + 1]), int(array[x + 2]), int(array[x + 3]), array, C, B)
            # get next opcode
            x += 4
        elif DE == 2:
            multOpCode(int(array[x + 1]), int(array[x + 2]), int(array[x + 3]), array, C, B)
            # get next opcode
            x += 4
        elif DE == 3:
            storeCode(int(array[x + 1]), input, array)
            x += 2
        elif DE == 4:
            outputCode(int(array[x + 1]), array)
            x += 2
        elif DE == 99:
            break


input = 1
print(opcodearr)
IntCodeProcessor(opcodearr, input)
print(opcodearr)