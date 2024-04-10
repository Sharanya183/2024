import math
def square_root(number):
    if number < 0:
        return "Square root is not defined for negative numbers"
    else:
        return math.sqrt(number)

# Example usage:
number = float(input("Enter a number: "))
result = square_root(number)
print("Square root:", result)

