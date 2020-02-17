
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(i+1, len(arr)): #have to iterate through the array (looping through elements ono right hand side of current index)
            if arr[j] < arr[smallest_index]: #if current position is less than the smallest index
                smallest_index = j #smallest index is the current position

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] #swap element at current index with the smallest element found in above loop

    return arr
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

   


def bubble_sort( arr ):
    swapped = True 

    while swapped: #while swapped is True
        swapped = False #set it to false at first(also no infinite loop)

        for i in range(0, len(arr)-1): #loop through array

            if arr[i] > arr[i + 1]: #if the current element is greater than one next to it
            
                arr[i], arr[i+1] = arr[i+1], arr[i] #swap them
                swapped = True #swapping has happened, so true

    return arr
print(bubble_sort(arr1))



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr