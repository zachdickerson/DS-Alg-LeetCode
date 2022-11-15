# # Hacker Rank - interview prep problem #4

'''
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

Example
scores = [12,24,10,24]

Scores are in the same order as the games played. She tabulates her results as follows:

                                     Count
    Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1
Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

Function Description

Complete the breakingRecords function in the editor below.

breakingRecords has the following parameter(s):

int scores[n]: points scored per game
Returns

int[2]: An array with the numbers of times she broke her records. Index 0 is for breaking most points records, and index 1 is for breaking least points records.
Input Format

The first line contains an integer , the number of games.
The second line contains  space-separated integers describing the respective values of .
score0, score1,....,scoren-1

Constraints
1 <= n <= 1000
0 <= socire[i] <= 10^8

'''

def breakingRecords(arr):

    new_array = []
    high_broken = 0
    low_broken = 0
    current_high = arr[0]
    current_low = arr[0]

    for element in arr:
        if current_high < element:
            current_high = element
            high_broken += 1
        elif current_low > element:
            current_low = element
            low_broken +=1

    new_array.append(high_broken)
    new_array.append(low_broken)
    return new_array
    # print(f' this is our array {arr}')
    # print(current_high)
    # print(current_low)
    # print(high_broken)
    # print(low_broken)
            

print(breakingRecords([12,24,10,24]))
print('Program is successful per HACKER RANK')