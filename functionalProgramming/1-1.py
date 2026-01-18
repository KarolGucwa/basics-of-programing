# Calculates arithmetic mean of two integer numbers
def mean(x, y):
    return (x + y) / 2

# takes two numbers from keyboard
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# calculates arithmetic mean and prints result
result = mean(n1, n2)
print(f"The arithmetic mean of {n1} and {n2} is {result}")
