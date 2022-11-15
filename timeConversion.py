# # Hacker Rank - interview prep problem #3

'''
Given a time in -hour AM/PM format, 
convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Input is a string

s = '12:01:00PM'
return '12:01:00'

s = '12:01:00AM'
return '00:01:00'

s = '07:05:45PM'
return '19:05:45'
'''

def timeConversion(s):

    time_changes = {
        '01':'13','02':'14',
        '03':'15','04':'16',
        '05':'17','06':'18',
        '07':'19','08':'20',
        '09':'21','10':'22',
        '11':'23', '12':'00'
    }

    if s[-2] == 'P' and s[0:2] != '12':
        x = s.replace(s[0:2], time_changes[s[0:2]])
    elif s[-2] == 'A' and s[0:2] == '12':
        x = s.replace(s[0:2], time_changes[s[0:2]])
    else:
        x = s

    return x[0:8]

print(timeConversion('12:05:45AM'))
print(timeConversion('00:01:00AM'))
print(timeConversion('01:05:45AM'))
print(timeConversion('02:05:45AM'))
print(timeConversion('03:05:45AM'))
print(timeConversion('04:05:45AM'))
print(timeConversion('05:05:45AM'))
print(timeConversion('06:05:45AM'))
print(timeConversion('07:05:45AM'))
print(timeConversion('08:05:45AM'))
print(timeConversion('09:05:45AM'))
print(timeConversion('10:05:45AM'))
print(timeConversion('11:05:45AM'))
print(timeConversion('12:05:45PM'))
print(timeConversion('01:05:45PM'))
print(timeConversion('02:05:45PM'))
print(timeConversion('03:05:45PM'))
print(timeConversion('04:05:45PM'))
print(timeConversion('05:05:45PM'))
print(timeConversion('06:05:45PM'))
print(timeConversion('07:05:45PM'))
print(timeConversion('08:05:45PM'))
print(timeConversion('09:05:45PM'))
print(timeConversion('10:05:45PM'))
print(timeConversion('11:05:45PM'))
print('Program is successful per HACKER RANK')

