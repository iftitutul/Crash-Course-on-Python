# https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    #    leap = False
    if (year % 4 == 0):
       return True
    elif (year % 400 == 0):
       print("leap year")
       return True
    elif (year % 100 == 0):
       print("it's not leap year")
       return False
    return False


year = int(input())
print(is_leap(year))
