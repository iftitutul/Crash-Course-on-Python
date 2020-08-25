""" Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you have learned thus far, like a for loop or a list comprehension. """

filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for i in range (len(filenames)):
   oldnames = filenames[i]
   newnames = oldnames.replace('.hpp','.h')
   newfilenames.append(newnames)
print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

# below codes are also correct
""" newfilenames = []
for filename in filenames:
   if ".hpp" in filename:
      index = filename.index(".hpp")
      newfilename = filename[:index]+".h"
   else:
      newfilename = filename
   newfilenames.append(newfilename)
print (newfilenames) """