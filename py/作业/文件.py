first = input()
t = open('test.txt',mode='w')
t.write(first)
t.close()


mod = input()
a = input()

try:
    tt = open('test.txt', mode=mod)
    tt.write(a)
    tt.close()
except:
    pass


ttt = open('test.txt')
b = ttt.read()
print(b)
