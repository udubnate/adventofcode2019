import logging
logger = logging.getLogger()
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

numrange = "236491-713787"

def parse(numrange):
    count = 0
    r = numrange.split('-')
    for i in range(int(r[0]),int(r[1])+1):
        valid = True
        adjacent = False
        neverdecrease = True
        for c in range(len(str(i))):
            fullstring = str(i)
            #adjacent check
            if c == len(fullstring)-1:
                continue
            elif fullstring[c] == fullstring[c+1]:
                adjacent = True
            if int(fullstring[c]) <= int(fullstring[c+1]):
                pass
            else:
                neverdecrease = False

            logger.debug("debug: current: " + str(fullstring[c]) + " next: " + str(fullstring[c + 1]))
        logger.debug(str(i) + " adjacent check : " + str(adjacent))
        logger.debug(str(i) + " neverdecrease check : " + str(neverdecrease))
        if adjacent and neverdecrease:
            count = count + 1
    return count

count = parse(numrange)
print("Total matches: " + str(count))