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


opcode = '3,0,4,0,99'
opcodearr = opcode.split(',')

# noun and verb and output
c = opcodearr[0]


def addOpCode(refA, refB, out, array):
    array[out] = int(array[refA]) + int(array[refB])


def multOpCode(refA, refB, out, array):
    array[out] = int(array[refA]) * int(array[refB])


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
        currentop.rjust(5, '0')
        DE = int(currentop[3:5])
        C = int(currentop[2])
        B = int(currentop[1])
        A = int(currentop[0])

        if int(array[x]) % 10 == 1:
            addOpCode(int(array[x + 1]), int(array[x + 2]), int(array[x + 3]), array)
            # get next opcode
            x += 4
        elif int(array[x]) % 10 == 2:
            multOpCode(int(array[x + 1]), int(array[x + 2]), int(array[x + 3]), array)
            # get next opcode
            x += 4
        elif int(array[x]) % 10 == 3:
            storeCode(int(array[x + 1]), input, array)
            x += 2
        elif int(array[x]) % 10 == 4:
            outputCode(int(array[x + 1]), array)
            x += 2
        elif int(array[x]) == 99:
            break


input = 25
IntCodeProcessor(opcodearr, input)
