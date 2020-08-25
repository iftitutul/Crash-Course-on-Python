##
file_counts = {"jpg": 10, "txt": 14, "csv": 20, "py": 23}
for extension in file_counts:
    print(extension)
    #print (extension, file_counts [extension])

##
file_counts = {"jpg": 10, "txt": 14, "csv": 20, "py": 23}
for ext,files in file_counts.items():
       print ("There are {} files on {} extension".format(files,ext))

## 
print (file_counts.keys())
print (file_counts.values())

## 
for value in file_counts.values():
       print(value)

""" Example:
Now, it's your turn! Have a go at iterating over a dictionary!
Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary."""

cool_beasts = {"octopuses": "tentacles", "dolphins": "fins", "rhinos": "horns"}
for name,value in cool_beasts.items():
    print("{} have {}".format(name, value))

## 
def count_letters(text):
       result = {}
       for letter in text:
              if letter not in result:
                     result[letter] = 0
              result[letter] += 1
       return result

print (count_letters("aaaa"))
print(count_letters("tenant"))
print(count_letters("This is python"))
