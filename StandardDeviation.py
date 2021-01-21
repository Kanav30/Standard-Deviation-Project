import csv
import math

with open ('data.csv', newline= '')as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def Mean(data):
    X = len(data)
    total = 0
    for N in data:
        total += int(N)
    Mean = total/X
    return Mean

squareList = []
for number in data:
    Y = int(number) - Mean(data)
    Y = Y**2
    squareList.append(Y)

sum = 0
for M in squareList:
    sum = sum + M

result = sum/(len(data)-1)
standardDeviation = math.sqrt(result)
print(standardDeviation)