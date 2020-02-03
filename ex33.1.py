
def variable(x,y):
    i = 0
    numbers = []
    while i<x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i =  i + y
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers:  ")
    for num in numbers:
        print(num)

print("enter x")
hello = int(input())
print("enter y")
yes = int(input())

variable(hello, yes)
