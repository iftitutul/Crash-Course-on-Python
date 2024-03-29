# Want to try this out? Let's give it a go!

# Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x(not included). Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x(not included).

def square(n):
    return n*n


def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum


print(sum_squares(10))  # Should be 285
