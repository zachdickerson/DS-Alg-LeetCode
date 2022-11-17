def divisibleSumPairs(arr):
    n = len(arr)
    k = 5  # this is our integer divider
    counter = 0
    new_list = []

    for row in range(n-1, 0, -1):
        for column in range(0,row):
            new_list.append([arr[row], arr[column]])

    for element in new_list:
        summed = (sum(element))
        if (summed % k) == 0:
            counter +=1
    
    return counter