# Creation
word = "Hello World"
print word

# Accessing characters from the strings
letter = word[0]
print letter

#Length
print len(word)

#Finding 
word = "Hello World"
print word.count("l")
print word.count("H")
print word.index("World")

#Counting
s = "Count, the number     of spaces"
print s.count(' ')

#Slicing
word = "Hello World"
print word[0]
print word[0:1]
print word[0:3]
print word[:3]
print word[-3:]
print word[3:]
print word[:-3]

#Split Strings
word = "Hello World"
print word.split(" ")

#Startwith / Endswith
word = "Hello World"
print word.startswith("H")
print word.startswith("W")
print word.endswith("d")
print word.endswith("W")

#Repeat Strings
print "."*10

#Replacing
word = "Hello World"
print word.replace("Hello", "Goodbye")

#Changing Upper and Lower Case Strings
string = "Hello World"
print string.upper()
print string.lower()
print string.title()
print string.capitalize()
print string.swapcase()

#Reversing
string = "Hello World"
print ('').join(reversed(string))

#Strip
word = "  Hello World  "
print word.strip()
print word.lstrip()
print word.rstrip()

#Concatination
print "Hello" + "World"
print "Hello" + "World" + "!"

#Join
word = "Hello World"
print (":").join(word)

#Testing
word = "Hello World"
print word.isalnum() # checks whether all char are alphanumeric
print word.isalpha() # checks wheteher all char are alphabetic
print word.isdigit() # test if string contains digit
print word.istitle() # test if string contains title words
print word.isupper() # test if string contains upper case
print word.islower() # test if string contains lower case
print word.isspace() # test if string contains spaces

