# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  for i in range(0, len(arr)):
    if arr[i] == target:
      return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  while low <= high:
    mid = (low + high)
    guess = arr[mid]

    if guess == target: #if guess is correct
      return mid

    if guess > target: #if guess is too large
      high = mid - 1
    
    else:
      low = mid + 1 #if guess is too small

  return -1 # not found

my_list = [1,3,5,7,9]
print(linear_search(my_list, 1))


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
