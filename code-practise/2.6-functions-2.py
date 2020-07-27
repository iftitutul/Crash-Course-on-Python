# Do you think you can flesh out your own function? I think you can! Lets give it a go. 
# Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

#!/usr/bin/env python3.6
def print_seconds(hours, minutes, seconds):
    total_seconds = (hours*3600) + (minutes*60) + seconds
    print(total_seconds)
  # print(hours*3600 + minutes*60 + seconds)
print_seconds(1, 2, 3)
