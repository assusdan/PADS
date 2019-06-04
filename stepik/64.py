count = 0
def merge_sort(arr):
    global count
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R): 
            if L[i] <= R[j]: 
                #print("first")
                arr[k] = L[i] 
                i+=1
            else: 
                #print("second "+str(len(L)) + " " + str(i))
                count += len(L) - i
                arr[k] = R[j] 
                j+=1
            k+=1
          
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

input()
data = list(map(int, input().split()))
merge_sort(data)
print(count)
