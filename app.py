# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calling the function and displaying the result
result = add_numbers(num1, num2)
print("The sum of", num1, "and", num2, "is:", result)
