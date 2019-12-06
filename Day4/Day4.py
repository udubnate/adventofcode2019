numrange = "12343-12346"


def parse(numrange):
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
                neverdecrease = True
            else:
                neverdecrease = False

            print("debug: current: " + str(fullstring[c]) + " next: " + str(fullstring[c + 1]))
        print(str(i) + " adjacent check : " + str(adjacent))
        print(str(i) + " neverdecrease check : " + str(neverdecrease))


parse(numrange)