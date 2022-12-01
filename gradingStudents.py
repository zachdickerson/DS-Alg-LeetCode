'''
2) Every student receives a grade in the inclusive
range from 0 to 100

1) Any grad less than 40 is a failing grade

Sam is a professor and would like to round students grades
according to these rules

- if the difference between the grade and the next
  multiple of 5 is less than 3, round grade up to the 
  next multiple of 5.

- if the value of grade is less than 38, no rounding occurs
  as the result will still be a failing grade


    Examples

    - grade = 84 round to 85 (85 - 84 is less than 3)
    - grade = 29 do not round (result is less than 40)
    - grade = 57 do not round (60-57 is 3 or higher)

Given the initial value of grade for each of Sam's n students
write.

'''


def gradingStudents(grades):
    
    new_list = []
    
    for element in grades:
        if element >= 38:
            if element % 5 == 4:
                element += 1
                new_list.append(element)
            elif element % 5 == 3:
                element += 2
                new_list.append(element)
            else:
                new_list.append(element)
        else:
            new_list.append(element)
            
    return new_list



print(gradingStudents([4, 73, 67, 38, 33]))



# def rof(x):
#     if x%5==4:
#         x+=1
#     elif x%5==3:
#         x+=2
#     print(x)

# print(rof(43))