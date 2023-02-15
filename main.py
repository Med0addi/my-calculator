# Define the functions for each operation
def sum(a, b):
    return a + b

def realDivi(a, b):
    return a / b

def sub(a, b):
    return a - b

def pow(a, b):
    return a ** b

# Display the menu and get user input
print("Select an operation:")
print("1. Add")
print("2. Divide")
print("3. Subtract")
print("4. Power")

choice = input("Enter choice (1/2/3/4): ")

# Get user input for operands
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the selected operation and display the result
if choice == '1':
    result = sum(num1, num2)
    print(num1, "+", num2, "=", result)

elif choice == '2':
    result = realDivi(num1, num2)
    print(num1, "/", num2, "=", result)

elif choice == '3':
    result = sub(num1, num2)
    print(num1, "-", num2, "=", result)

elif choice == '4':
    result = pow(num1, num2)
    print(num1, "^", num2, "=", result)

else:
    print("Invalid input")

