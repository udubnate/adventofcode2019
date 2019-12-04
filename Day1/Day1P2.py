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
        return SumCalcFuel(fuel) + fuel


print(SumCalcFuel(1969))

# Input from File and Sum
inputsum = 0.0
with open('Data.txt') as f:
    for line in f:
        inputsum += SumCalcFuel(int(line))
        print(inputsum)
