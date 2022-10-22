a = int(input())
d = {'hello':'1'}
d.clear()
for i in range(a):
    s1 = input()
    b = s1 . split(" ")
    d[b[1]] = b[0]
    
s2 = input()
while(s2 != "dog"):
    if(d.get(s2)):
        print(d[s2])
    else:
        print("dog")
    s2 = input() 


