def to_celcius(x):
   return (x-32)*5/9

for x in range(0,101,10):
   print (x, to_celcius(x))