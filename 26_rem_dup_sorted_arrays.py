


def removeDuplicates(nums):

    counter = 1
    new_count = 0

    n = len(nums) - 1

    for element in nums:
        
        if nums[element] == nums[counter]:
            nums.append(nums.pop(nums.index(counter)))
    
    print(nums)


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))