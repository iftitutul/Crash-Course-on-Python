# Complete the body of the format_name function. This function receives the first_name and last_name parameters and then returns a properly formatted string.
# Specifically:
# If both the last_name and the first_name parameters are supplied, the function should return like so:

'''
print(format_name("Ella", "Fitzgerald"))
Name: Fitzgerald, Ella

# If only one name parameter is supplied (either the first name or the last name) , the function should return like so:

print(format_name("Adele", ""))
Name: Adele

#or

print(format_name("", "Einstein"))
Name: Einstein

# Finally, if both names are blank, the function should return the empty string:
print(format_name("", ""))
'''

# Implement below:

def format_name(first_name, last_name):
	# code goes here
   if (first_name == "") and (last_name != ""):
	   return ("Name: " + last_name)
   elif (first_name != "") and (last_name == ""):
	   return ("Name: " + first_name)
   elif (first_name != "") and (last_name != ""):
      return ("Name: " + last_name + ", " + first_name)
   else:
	   return ("Empty string")

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
