


x = input().split(" ")
n = int(x[0])
m = int(x[1])
page = list(map(int, input( ).split()))
t = {}
sum = 0
 
for p in page:
    for k in t:
        t[k] += 1
    if p in t:
        t[p] = 0
    else:
        sum += 1
        if (len(t) == n):
            ma = max(t.items(), key=lambda e: e[1])
            t.pop(ma[0])
            t[p] = 0
        else:
            t[p] = 0
 
print(sum)
t1 = sorted(t)

print(" ".join(str(i) for i in t1))
