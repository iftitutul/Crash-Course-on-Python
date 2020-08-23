# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we are on vacation. Return True if we sleep in.

# sleep_in(False, False) Output: True
# sleep_in(True, False) Output: False
# sleep_in(False, True) Output: True 

# https://codingbat.com/prob/p173401


def sleep_in (weekday, vacation):
   if not weekday or vacation:
      return True
   else:
      return False

print (sleep_in(False, False))
print (sleep_in(True, False))
print (sleep_in(False, True))
