import queue

opcode = '1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,2,10,23,27,1,27,6,31,1,13,31,35,1,13,35,39,1,39,10,43,2,43,13,47,1,47,9,51,2,51,13,55,1,5,55,59,2,59,9,63,1,13,63,67,2,13,67,71,1,71,5,75,2,75,13,79,1,79,6,83,1,83,5,87,2,87,6,91,1,5,91,95,1,95,13,99,2,99,6,103,1,5,103,107,1,107,9,111,2,6,111,115,1,5,115,119,1,119,2,123,1,6,123,0,99,2,14,0,0'
opcodearr = opcode.split(',')

#noun and verb and output
c = opcodearr[0]

def addOpCode(refA, refB, out, array):
    array[out] = int(array[refA]) + int(array[refB])

def multOpCode(refA, refB, out, array):
    array[out] = int(array[refA]) * int(array[refB])

def IntCodeProcessor(array):

    for x in range(0, len(array), 4):
        if int(array[x]) == 1:
            addOpCode(int(array[x + 1]), int(array[x + 2]), int(array[x + 3]), array)
        elif int(array[x]) == 2:
            multOpCode(int(array[x + 1]), int(array[x + 2]), int(array[x + 3]), array)
        elif int(array[x]) == 99:
            break

for i in range(99):
    for j in range(99):
        #print("Testing i:" + str(i) + " Testing j:" + str(j))
        testarray = opcodearr.copy()
        testarray[1] = i
        testarray[2] = j
        IntCodeProcessor(testarray)
        if int(testarray[0]) == 19690720:
            print(i,j)

