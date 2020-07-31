# Fill in the blanks to calculate the area of a triangle of base 5, height 3 and output the result. Reminder: the area of a triangle is (base*height)/2.

'''
#!/usr/bin/env python3.6
base = 5
height = 3
area = (base * height)/2

print(area)
'''

def area_traingle (base,height):
    return (base*height)/2

area_a = area_traingle(5,4)
area_b = area_traingle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))