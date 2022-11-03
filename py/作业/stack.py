class Stack:
    len = 0
    stack = []

    def __init__(self, lenth, number):
        self.len = int(lenth)
        for i in range(lenth):
            self.stack.append(number[i])

    def pop(self, number):
        if len(self.stack)<number:
            number = len(self.stack)
        for i in range(number):
            outlist.append(self.stack.pop())

    def push(self, le, number):
        for i in range(le):
            self.stack.append(number[i])


lens = int(input())
getNumber = list(map(int, input().split()))
test = Stack(lens, getNumber)
getNumbers = list(input().split())
order = getNumbers.pop(0)

outlist = []
if order == 'pop':
    test.pop(int(getNumbers[0]))
elif order == 'push':
    test.push(len(getNumbers), getNumbers)

getNumbers = list(input().split())
order = getNumbers.pop(0)
if order == 'pop':
    test.pop(int(getNumbers[0]))
elif order == 'push':
    test.push(len(getNumbers), getNumbers)

if len(test.stack) == 0:
    print("len = 0")
else:
    print("len = " + str(len(test.stack)) + ", data = " + " ".join(str(st) for (st) in test.stack))

if len(outlist) == 0:
    print("len = 0")
else:
    print("len = " + str(len(outlist)) + ", data = " + " ".join(str(st) for (st) in outlist))