def add(num1, num2):
    return num1 + num2

def square(num):
    return num ** 2

# Demonstrate tuple unpacking
def before_and_after(num):
    return (num-1, num+1)

before, after = before_and_after(7)

print("Before:", before)
print("After:", after)

