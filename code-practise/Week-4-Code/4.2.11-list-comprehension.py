### Exp 1
name = "bobita,  Razzak,Shabana, Joshim"
split_name = name.split(',')
print(split_name)
""" output = []
for name in split_name:
   updated_name = name.strip().title()
   output.append(updated_name)
 """

output = [names.strip().title() for names in name.split(',')]
print(output)

### Exp 2
""" multiples = []
for x in range(1,11):
   multiples.append(x*7) """

multiples = [x*7 for x in range(1,11)]
print (multiples)

### Exp 3
languages = ["Python", "Go", "C", "Java", "Perl", "Ruby", "Javascript"]
lenghts = [len(language) for language in languages]
print (lenghts) 

### Exp 4
z = [x for x in range (0,101) if  x %3 == 0]
print(z)
