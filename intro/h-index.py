def calculateHIndex(arr):
    index = 0
    #check empty list
    if not arr:
        index = -1
    #python sort is O(nlogn) worst case, n is the number of elements in arr
    arr.sort()
    length = len(arr)
    for i in range(length):
         if arr[i] > index and arr[i] <= (length - i):
             index = arr[i]
         print(index)
    return index

print(calculateHIndex([1,4,1,4,2,1,3,5,6]))
