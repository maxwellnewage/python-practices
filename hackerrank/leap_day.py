"""
https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
"""


def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True

    return leap


print(is_leap(1990))
print(is_leap(2400))
