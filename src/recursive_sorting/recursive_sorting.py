# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    a = 0 #counter for arrayA
    b = 0 #counter for arrayB
    m = 0 #counter for mergedarray

    while a < len(arrA) and b < len(arrB): #comparing a and b to determine which one gets added to merge first
        if arrA[a] < arrB[b]: #if num for array a is less than num for array b
            merged_arr[m] = arrA[a] #then you add that position of a becomes m
            m = m + 1 #increase the counter for the mergearray
            a = a + 1 #as well increase for a but b stays the same since it wasn't merged
        
        else: #opposite of the above happens (b is less than a)
            merged_arr[m] = arrB[b]
            m = m + 1 #keep increasing counter for merge list
            b = b + 1 #b gets incremented because it needs to move on

     #once one array ends then we'll merge the rest of the other to the merged list because we can assume that it's going to be greater and it's already sorted
    while a < len(arrA): #if there are leftover numbers from arraya merge the rest to mergearray
         merged_arr[m] = arrA[a]
         m = m + 1
         a = a + 1

    while b < len(arrB): #if there are leftover numbers from arrayb merge the rest to mergearray
        merged_arr[m] = arrB[b]
        m = m + 1
        b = b + 1

    return merged_arr

testA = [2,3,5,7]
testB = [0,1,4,9]
print(merge(testA, testB))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1 : 
        
        split = len(arr)//2
    
        #call merge sort on lhs
        left = merge_sort(arr[:split])
        #call merge sort on rhs
        right = merge_sort(arr[split:])
        #merge sorted pieces
        arr = merge(left, right)

    return arr
    
testC = [2,3,7,1,8]
print(merge_sort(testC))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
