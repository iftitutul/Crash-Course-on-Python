msg = "This is tutul"

new_msg = msg[0:8] + "T" + msg[9:]

print(new_msg)

word = "pats & dogs"
letter = word.index("s")

print (letter)

get_word = "cats" in word
print (get_word)

get_word = "pats" in word
print (get_word)

## Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious". 
word = "supercalifragilisticexpialidocious"
print(word.index("x"))
