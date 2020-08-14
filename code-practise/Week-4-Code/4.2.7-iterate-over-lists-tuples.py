animals = ["donkey", "monkey", "elephant", "ass"]
chars = 0

for animal in animals:
   chars += len(animal)

print ("Total characters: {} , Average character: {}".format(chars, chars/len(animals)))