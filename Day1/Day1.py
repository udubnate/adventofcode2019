import math

def CalcFuel(mass):
    fuel = math.floor(mass / 3) - 2
    print(fuel)
    return fuel

def SumCalcFuel(mass):
    fuel = math.floor(mass / 3) - 2
    if (fuel < 0):
        return 0
    else:
        return SumCalcFuel(mass) + fuel


# UnitTest
arr = [12, 14, 1969, 100756]
sum = 0

for item in arr:
    sum += CalcFuel(item)
print(sum)

# Input from File and Sum
inputsum = 0.0
with open('Data.txt') as f:
    for line in f:
        inputsum += CalcFuel(int(line))
        print(inputsum)
