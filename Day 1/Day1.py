def getInputs(fileName):

    file = open(fileName, 'r')
    lines = file.readlines()
    file.close()

    return lines

def getSummedValues(values):
    summedValues = []
    currentSum = 0
    for value in values:        
        strippedValue = value.strip()
        if strippedValue == "":
            summedValues.append(currentSum)
            currentSum = 0
        else:
            currentSum += int(strippedValue)
    return summedValues

inputs = getInputs("Day 1/RealInput.txt")
summedValues = getSummedValues(inputs)
summedValues.sort(reverse=True)
print(summedValues[0])
print(sum(summedValues[:3]))