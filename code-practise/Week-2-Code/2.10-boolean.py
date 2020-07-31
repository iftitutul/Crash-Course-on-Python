#! /usr/bin/env python3.6
print (10 > 1)
print (10 < 1)
print ("cat" == "dog")
print (1 != 2)

'''
print (1 < "1")
Traceback (most recent call last):
  File "/home/iftikhar/Doc/DevOps/Python/Google-Crash-Course-on-Python/code-practise/2.10-boolean.py", line 7, in <module>
    print (1 < "1")
TypeError: '<' not supported between instances of 'int' and 'str'
'''


print(1 == "1")
#it's clear to the computer that one is a number and the other is the string. For the computer it's obvious that they are completely different entities.


print("cat" + "Cat")

'''
"cat" is larger than "Cat"
Correct

You nailed it! In Python uppercase letters are alphabetically sorted before lowercase letters.
'''
print ("Yellow" > "Cyan" and "Brown" > "Magenta")
#Here we're comparing strings, and the bigger and smaller operators refer to alphabetical order. Yellow comes after cyan, but brown doesn't come after magenta. So this means that the first statement is true, but the second one isn't, which makes the result of the whole expression false.

print ( 25 > 50 or 1!=2)
#25 is definitely not bigger than 50, but 1 is different than 2. So in the end the whole expression is true

print ( not 42 == "Answer")
#If the expression is true, it becomes false. If it's false, it becomes true
