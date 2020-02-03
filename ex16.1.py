#import argument variable from system :)
from sys import argv
script, filename= argv

#erase or not?  press keys to do action
print(f"We're going to erase{filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
#file opens but what is 'w' does this mean write???????? NITE HELP
target = open(filename, 'w')

#truncate = empty file :)
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
#insert what you want to put
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#lines are written with line breaks combined so less code than ex16 :)
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
print("And finally, we close it.")
target.close()
