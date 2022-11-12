'''
This is the Linear Search Algorithm

It is a sequential serach algorithm that starts at one
end and goes through each elment of a list until disired 
element is found.

Time complexity is O(n)

input = [10,50,30,70,80,60,20,90,40], target = 20
output = index 5

input = [10,50,30,70,80,60,20,90,40], target = 35
output = 'target not in list'

'''

def linear_search(my_Array, target):

    if len(my_Array) == 0:
        return 'Array is empty'
    
    for element in range(0, len(my_Array)):

        if my_Array[element] == target:

            return f'{target}, is in the array at position {element}'

    return f'{target}, is not in the Array'


print(linear_search([10,50,30,70,80,60,20,90,40], 20))
print(linear_search([10,50,30,70,80,60,20,90,40], 35))
print(linear_search([], 20))


'''
After notes:

Use of counter becomes uncessary if the use of
length of array is used. 

'''
