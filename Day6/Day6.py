# Solution heavily influenced by https://github.com/mevdschee/AdventOfCode2019/blob/master/day06/part1.py#L2
# Thanks mevdschee!
#

# build some sort of tree data structure - looks like dict worked
# count branches

parents = {}
# #File operations
with open('Data.txt') as f:
    for line in f:
        parent,child = line.strip().split(")")
        parents[child] = parent

sum = 0
for node in parents:
    while node in parents:
        #print(node, parents[node])
        node = parents[node]
        sum +=1
print(sum)
