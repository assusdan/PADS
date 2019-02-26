f = open("input.txt", "r")
o = open("output.txt", "w")
f.readline() # we don't need N

log = [1] # the first element is always the first

def insertionSort(arr, log): 
    for i in range(1, len(arr)): 
        current_value = arr[i] 

        # reverse from i-1 to 0 to find the right place
        j = i
        while j > 0 and current_value < arr[j-1] : 
                arr[j] = arr[j-1] 
                j -= 1
        log.append(j + 1) # + 1 'cause openedu's arrays start from 1 (0_o)
        arr[j] = current_value 


arr = list(map(int, f.readline().split(' ')))

insertionSort(arr, log)

o.write(str.join(" ",  list(map(str, log))))
o.write("\n")
o.write(str.join(" ",  list(map(str, arr))))