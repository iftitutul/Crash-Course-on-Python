# https://www.hackerrank.com/challenges/whats-your-name/problem

def print_full_name(a, b):
    length = len(a) + len(b)
    if (length >= 10):
       print("Hello " + a + " " + b + "! You just delved into python.")
    else:
       print("full name length less than 10 letters")


first_name = input()
last_name = input()
print_full_name(first_name, last_name)
