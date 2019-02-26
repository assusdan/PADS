f = open("input.txt", "r")
o = open("output.txt", "w")
f.readline()

# [] because of openedu's strange indexes starting with 1
guys = enumerate(map(float, []+f.readline().split(' ')))

def partition(arr, low, high): 
    i = low - 1 
    pivot = arr[high] 
    for j in range(low , high): 
        # If current element is smaller than or 
        # equal to pivot 
        if arr[j][1] <= pivot[1]: 
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return i + 1 
  
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

# [1:] because of openedu's strange indexes starting with 1
guys = list(guys)[1:]

quickSort(guys, 0, len(guys)-1)

o.write(str(guys[0][0])+" "+str(guys[int((len(guys)-1)/2)][0])+" "+str(guys[len(guys)-1][0]))