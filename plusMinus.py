# Hacker Rank - interview prep problem #1

'''
Given a int array, calculate the ratio of it's elements 
that are positive, negative, and zero. Print the value
of each fraction on a new line 6 places past decimal.

arr = [1,1,0,-1,-1]
n = 5

2/5 = 0.400000 (positives)
2/5 = 0.400000 (negatives)
1/5 = 0.200000 (zeros)

Constraints 

0 < n <= 100
-100 <= arr[i] <= 100

'''
import math

def plusMinus(arr):

    n = len(arr)
    positive = 0
    negative = 0
    zeros = 0

    for element in arr:
        if element > 0:
            positive += 1
        elif element < 0:
            negative += 1
        else:
            zeros += 1

    my_pos = (positive/n)
    my_neg = round((negative/n), 6)
    my_zeros = round((zeros/n), 6)
    print("{0:.6f}".format(my_pos))
    print("{0:.6f}".format(my_neg))
    print("{0:.6f}".format(my_zeros))

    return ''

print(plusMinus([1,1,0,-1,-1]))
print('Program is successful per HACKER RANK')