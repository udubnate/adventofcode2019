numrange = "12343-12346"


def parse(numrange):
    r = numrange.split('-')
    for i in range(int(r[0]),int(r[1])+1):
        valid = True
        adjacent = False
        for c in range(len(str(i))):
            fullstring = str(i)
            #adjacent check
            if c == len(fullstring)-1:
                continue
            elif fullstring[c] == fullstring[c+1]:
                adjacent = True
                break
            print("debug: current: " + str(fullstring[c]) + " next: " + str(fullstring[c + 1]))
        print(str(i) + " adjacent check : " + str(adjacent))

parse(numrange)