#!/usr/bin/env python3.6
for left in range(7):
   for right in range (left, 7):
      print ("[" + str(left) + "|" + str(right) + "]", end=" ")
   print()

# In this code, we're using a new parameter that we passed to the print function. This parameter is called End. Normally, once print has taken the content we passed and written it to the screen, then it writes a special character that creates a new line called the newline character. If we want print to write something else instead of the newline character, we use the end parameter, like we see in this example.
