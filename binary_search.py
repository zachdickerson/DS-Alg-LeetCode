'''
Binary Searching Algorithm

Given a sorted Array[] of n elements, 
write a function to search a given element
x in array[] and return the index of that
element.

Works only if the algorithm is sorted*
to ensure all algorithms are sorted,
for now python sorted() will work

It is a seraching algorith used in a sorted
Array by repeatedly dividing the search interval
in half. The idea of binary search is to use
the information that the array is sorted and 
reduce the time complexity to O(Log n)

input = [10,50,30,70,80,60,20,90,40], target = 20
output = index 5

input = [10,50,30,70,80,60,20,90,40], target = 35
output = 'target not in list'

'''

def binary_search(my_Array, target):

    sorted_Array = sorted(my_Array)
    low = 0
    high = len(my_Array)-1
    
    while low <= high:
 
        mid_point = low + (high - low) // 2
 
        # Check if x is present at mid
        if sorted_Array[mid_point] == target:
            return f'Element is at position {mid_point}'
 
        # If x is greater, ignore left half
        elif sorted_Array[mid_point] < target:
            low = mid_point + 1
 
        # If x is smaller, ignore right half
        else:
            high = mid_point - 1
 
    # If we reach here, then the element
    # was not present
    return -1



print(binary_search([10,50,30,70,80,60,20,90,40], 80))
