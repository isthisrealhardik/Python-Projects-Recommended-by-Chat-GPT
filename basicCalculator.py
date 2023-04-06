# A Basic Calculator
# which can do addition, subtraction, multiplication and division
# of however digits you'd like
# returns the answer

howMany = int(input("How many numbers you'd like to operate on?"))
numberList = []

for i in range(0, howMany): 
    value = int(input(f'enter your {i+1}st number: ' if  i+1 == 1 else f'enter your {i+1}th number: '))
    numberList.append(value)

operation = input("what operation you'd like to perform on your numbers (add, sub, mul, div): ")

def calculate(numArr, op):
    result = 0
    lenOfnumArr = range(0, len(numArr))
    if (op == 'add'):
        for i in lenOfnumArr:
            result += numArr[i]
    if (op == 'sub'):
        for i in lenOfnumArr:
            result -= numArr[i]
    if (op == 'mul'):
        result = 1
        for i in lenOfnumArr:
            result *= numArr[i]
    if (op == 'div'):
        result = 1
        for i in lenOfnumArr:
            result /= numArr[i]
    return result

print(calculate(numberList, operation))