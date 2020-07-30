#The is_positive function should return True if the number received is positive and False if it isn't. Can you fill in the gaps to make that happen?

#!/usr/bin/env python3.6
def is_positive(number):
  if number > 0:
    return True
  else:
    return False

print(is_positive(5))
print(is_positive(-5))

# return
def is_even(number):
   if (number) % 2 == 0:
      return True
   return False
# The trick is that when a return statement is executed, the function exits so that the code that follows doesn't get executed
print(is_even(3))
print(is_even(4))
