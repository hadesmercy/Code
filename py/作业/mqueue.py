import queue
int(input())

my_queue = queue.Queue(100)
number = list(map(int,input().split()))
for i in range(len(number)):
    my_queue.put(number[i])


order = list(input().split())
if order[0] == 'out':
    del order[0]
    for i in range(int(order[0])):
        my_queue.get()
if order[0] == 'in':
    del order[0]
    order = list(map(int,order))
    for i in range(len(order)):
        my_queue.put(order[i])

order = list(input().split())
if order[0] == 'out':
    del order[0]
    for i in range(int(order[0])):
        my_queue.get()
if order[0] == 'in':
    del order[0]
    order = list(map(int,order))
    for i in range(len(order)):
        my_queue.put(order[i])

for i in range(my_queue.qsize()):
    print(my_queue.get())

