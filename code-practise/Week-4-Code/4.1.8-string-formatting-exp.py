## example 1
name = "tutul"
num = len(name) + 3
print ("hello {}, you num is: {}".format(name, num))

print("hello {name}, you num is: {no}".format(name="ifti", no=len(name)+2 ))

## example 2
price = 7.5
with_tax = price * 1.09
print(price,with_tax)
print("Base price is ${:.2f}. with tax: ${:.2f}".format(price,with_tax))

## example 3
def to_celcius(x):
   return (x-32)*5/9

for x in range (0,101,10):
  # print(x,to_celcius(x))
   print("{:>3}F | {:>6.2f}C".format(x, to_celcius(x)))
