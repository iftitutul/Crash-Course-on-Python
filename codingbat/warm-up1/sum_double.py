# https://codingbat.com/prob/p141905

def sum_double(a, b):
    if (a == b):
        sum = (a + b) * 2
        return sum
    else:
        sum = a + b
        return sum


print (sum_double(1, 2))
print (sum_double(3, 2))
print (sum_double(2, 2))
