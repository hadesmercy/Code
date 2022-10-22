def VerifySquenceOfBST( sequence):
    # write code here
    if sequence == []:
        return False
    
    length = len(sequence)
    root = sequence[-1]
    
    for i in range(length):
        if sequence[i] > root:
            break
    for j in range(i, length):
        if sequence[j] < root:
            return False
        
    left = True
    if i > 0:
        left = VerifySquenceOfBST(sequence[:i])
    right = True
    if j < length - 1:
        right = VerifySquenceOfBST(sequence[i:length-1])
    return left and right
aa = input().split()
a = list(map(int, input().split()))
print(type(a[0]),type(aa[0]))
if VerifySquenceOfBST(a) == True:
    print("true")
else:
    print("false")

