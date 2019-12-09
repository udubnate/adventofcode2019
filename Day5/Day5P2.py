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


opcode = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'
opcodearr = opcode.split(',')

# noun and verb and output
c = opcodearr[0]


def addOpCode(paramA, paramB, out, array):

    array[out] = str(paramA + paramB)


def multOpCode(paramA, paramB, out, array):

    array[out] =  str(paramA * paramB)


def storeCode(valA, input, array):
    array[valA] = input


def outputCode(valA, array):
    print(array[valA])

def getmodevalue(ref, mode, array):
    if int(mode) == 1:
        param = int(ref)
    else:
        param = int(array[ref])
    return param

def jumpiftrue(paramA, paramB, cursor):
    if (paramA != 0):
        cursor = paramB
    return cursor


def jumpiffalse(paramA, paramB, cursor):
    if (paramA == 0):
        cursor = paramB
    return cursor

def lessthanCode(paramA, paramB, out, array):
    if paramA < paramB:
        array[out] = 1
    else:
        array[out] = 0

def equalsCode(paramA, paramB, out, array):
    if paramA == paramB:
        array[out] = 1
    else:
        array[out] = 0


def IntCodeProcessor(array, input):
    x = 0
    while x < len(array):

        # account for position/immediate modes
        currentop = array[x]
        currentop = currentop.rjust(5, '0')
        DE = int(currentop[3:5])
        C = int(currentop[2])
        B = int(currentop[1])
        A = int(currentop[0])

        if DE == 1:
            paramA = getmodevalue(int(array[x + 1]), C, array)
            paramB = getmodevalue(int(array[x + 2]), B, array)

            addOpCode(paramA, paramB, int(array[x + 3]), array)
            # get next opcode
            x += 4
        elif DE == 2:
            paramA = getmodevalue(int(array[x + 1]), C, array)
            paramB = getmodevalue(int(array[x + 2]), B, array)

            multOpCode(paramA, paramB, int(array[x + 3]), array)
            # get next opcode
            x += 4
        elif DE == 3:
            storeCode(int(array[x + 1]), input, array)
            x += 2
        elif DE == 4:
            outputCode(int(array[x + 1]), array)
            x += 2
        elif DE == 5:
            paramA = getmodevalue(int(array[x + 1]), C, array)
            paramB = getmodevalue(int(array[x + 2]), B, array)

            x = jumpiftrue(paramA, paramB, x)
        elif DE == 6:
            paramA = getmodevalue(int(array[x + 1]), C, array)
            paramB = getmodevalue(int(array[x + 2]), B, array)

            x = jumpiffalse(paramA, paramB, x)
        elif DE == 7:
            paramA = getmodevalue(int(array[x + 1]), C, array)
            paramB = getmodevalue(int(array[x + 2]), B, array)

            lessthanCode(paramA, paramB, int(array[x + 3]), array)
            x += 4
        elif DE == 8:
            paramA = getmodevalue(int(array[x + 1]), C, array)
            paramB = getmodevalue(int(array[x + 2]), B, array)

            equalsCode(paramA, paramB,int(array[x + 3]), array)
            x += 4
        elif DE == 99:
            break


input = 234
print(opcodearr)
IntCodeProcessor(opcodearr, input)
print(opcodearr)