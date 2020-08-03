# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False

    if (year % 4 == 0):
        leap = True
        if (year % 100 == 0):
            leap = False
            if (year % 400 == 0):
                leap = True
    return leap

#def is_leap(year):
#return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

year = int(input())
print(is_leap(year))
