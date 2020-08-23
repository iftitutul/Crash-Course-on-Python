# https://codingbat.com/prob/p124676

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

""" 
def near_hundred(n):
   value1 = 100 - n
   value2 = 200 - n

   if (n < 300):
      if (abs(value1) <= 10):
         return True
      elif (abs(value2) <= 10):
         return True
      else:
         return False
   else:
      return 0 
"""


print (near_hundred(93))
print (near_hundred(90))
print (near_hundred(89))
print (near_hundred(190))
