def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i]  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
        
        print(" ".join(str(i) for i in arr))
arr = []
a = int(input())
aa = input()
aaa = aa.split(" ")
for i in range(a):
    arr.append(int(aaa[i]))
insertionSort(arr) 
