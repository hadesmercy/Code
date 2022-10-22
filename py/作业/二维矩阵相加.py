m,n  = map(int,input().split())
a = input()
b = eval(a)
aa = input()
bb = eval(aa)
c =list(bb)
for i in range(m):
    for j in range(n):
        c[i][j]= b[i][j] + bb[i][j]
def my_print(obj):
    print (str(obj).replace(' ', ''))

my_print(c)