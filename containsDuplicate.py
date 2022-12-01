'''
Given an integer array nums, return true 
if any value appears at least twice in the 
array, and return false if every element is 
distinct.


Example 1
input = [1,2,3,1]
output true

Example 2
input = [1,2,3,4]
output = false

Example 3
input = [1,1,1,3,3,4,3,2,4,2]
output = true
'''


def containsDup(nums):

    my_dict = {}

    for element in nums:
        if element in my_dict: 
            return True
        else: 
            my_dict[element] = 1
            
    return False



print(containsDup([1,2,3,4]))