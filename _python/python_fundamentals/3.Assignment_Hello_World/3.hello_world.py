# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Ayah"
print("Hello",name)	# with a comma
print("Hello"+name)	# with a +

# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello",name)	# with a comma
print("Hello"+str(name))# with a +

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "Nodles"
fave_food2 = "Mandy"
print("I love to eat {} and {}".format(fave_food1,fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

#5.NINJA BONUS: Spend a few minutes playing around with other string methods to see what’s out there!
name1  = "ayah"
name2 = "AYAH"
print(name1.upper())
print(name2.lower())