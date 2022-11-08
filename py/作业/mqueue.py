class queuee:
    lens = 0
    stack = []
    
    def __init__(self, lenth):
        self.len = int(lenth)

    def put(self, number):
        
        self.stack.append(number)
        self.lens = self.lens + 1
    def get(self):
        if  self.lens == 0:
            return 
        temp = self.stack[0]
        del self.stack[0]
        self.lens -= 1
        return temp
    def qsize(self):
        return self.lens


si = int(input())

my_queue = queuee(si)
number = list(map(int,input().split()))
for i in range(len(number)):
    my_queue.put(number[i])
#初始化队列
the_out_num = []


order1 = input().split()
if order1[0] == 'out':
    del order1[0]
    tt = int(order1[0])
    if tt > my_queue.lens:
        tt = my_queue.lens
    for i in range(tt):
        the_out_num.append(my_queue.get())


if order1[0] == 'in':
    del order1[0]
    for i in range(len(order1)):
        my_queue.put(int(order1[i]))

order1 = input().split()
if order1[0] == 'out':
    del order1[0]
    tt = int(order1[0])
    if tt > my_queue.lens:
        tt = my_queue.lens
    for i in range(tt):
        the_out_num.append(my_queue.get())


if order1[0] == 'in':
    del order1[0]
    for i in range(len(order1)):
        my_queue.put(int(order1[i]))

b = []
for i in range(my_queue.qsize()):
    b.append(my_queue.get())
    

if len(b) == 0:
    print("len = 0")
else:
    print("len = " + str(len(b)) + ", data = " + " ".join(str(st) for (st) in b))

if len(the_out_num) == 0:
    print("len = 0")
else:
    print("len = " + str(len(the_out_num)) + ", data = " + " ".join(str(st) for (st) in the_out_num))