import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

numrange = "236491-713787"

def parse(numrange):
    count = 0
    r = numrange.split('-')
    for i in range(int(r[0]),int(r[1])+1):
        adjacent = hasAdjacent(i)
        decreasecheck = neverDecrease(i)
       # countTwoMatches = countAll(i)
        if adjacent and decreasecheck:
            count = count + 1
    return count

def hasAdjacent(input):
    adjacent = False
    inputstr = str(input)
    for i in range(len(inputstr)-1):
         if inputstr[i] == inputstr[i+1]:
            if countChar(inputstr, inputstr[i]) == 2:
                return True
    return False


def neverDecrease(input):
    adjacent = False
    inputstr = str(input)
    for i in range(len(inputstr)-1):
         if int(inputstr[i]) <= int(inputstr[i+1]):
            pass
         else:
             return False
    return True

def countChar(input, c):
    count = 0
    inputstr = str(input)
    for i in range(len(inputstr)):
        if inputstr[i] == c:
            count = count + 1
    return count

count = parse(numrange)
print("Total matches: " + str(count))
