# https://codingbat.com/prob/p124984

def makes10(a,b):
   sum = a + b
   if ( a == 10 or b ==10) or (sum == 10):
      return True
   else:
      return False

print (makes10(9,10))
print (makes10(9,9))
print (makes10(1,9))