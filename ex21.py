def add(a, b):
    print(f"ADDING {a}+ {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"SUBTRACTING {a}/{b}")
    return a / b

print("Let's do some math with just functions!")

age=add(30,5)
height= subtract(78,4)
weight=multiply(90,2)
iq= divide(100,2)

print(f"Age:{age}, Height:{height}, Weight:{weight}, IQ: {iq}")

#a puzzle for the extra  credit, type it in anyway

print("here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand?")


#study drill #4

print("Let's make the program calculated 24+(30-(4*(100/25)))")

x=add(20,4)
y=subtract(50,20)
z=multiply(1,4)
w=divide(1000,10)

print(f"x:{x}, y:{y}, z:{z}, w:{w}")

what1= add(x, subtract(y, multiply(z, divide(w,4))))

print("That becomes:", what1)
