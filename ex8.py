formatter= "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format("try your", "Own text here", "Maybe a poem",  "Or a song about fear"))

#it is a function to turn formatter variable into other strings
#formatter.format is
#1. take the defined formatter
#2. call it's format function or telling it to do the command named format
#3. format for the four arguments for the four {} in the variable
# :) 
