# # Hacker Rank - interview prep problem #2

'''
Given five positive integers, find the minimum and 
maximum values that can be calculated by summing 
exactly four of the five integers. Then print the 
respective minimum and maximum values as a single 
line of two space-separated long integers.

arr = [1,3,5,7,9]

miniSum = 1+3+5+7 = 16
and
maxSum = 3+5+7+9 = 24

return 16 24

Constraints
1 <= arr[i] <= 10^9
'''

def miniMaxSum(arr):

    our_Maximum = 0
    m = sorted(arr)


    for element in m: 
        our_Maximum += element

    miniSum = our_Maximum - m[-1]
    maxSum = our_Maximum - m[0]

    
    return f'{miniSum} {maxSum}'

    

print(miniMaxSum([1,3,5,7,9]))
print(miniMaxSum([7,69,2,221,8974]))

print(miniMaxSum([7,69,2,221,8974]))
print('Program is successful per HACKER RANK')