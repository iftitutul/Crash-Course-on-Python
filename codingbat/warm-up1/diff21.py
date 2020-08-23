# https://codingbat.com/prob/p197466

def diff21(n):
   diff = 21 - n
   if n < 21:
      return abs(diff)
   else:
      return abs(diff) *2


print (diff21 (19))
print (diff21 (10))
print (diff21 (21))
print (diff21 (50))
print (diff21 (22))
