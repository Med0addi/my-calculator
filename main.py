# Define the functions for each operation
def sum(a, b):
    return a + b

def realDivi(a, b):
    return a / b

# Display the menu and get user input
print("Select an operation:")
print("1. Add")
print("2. Divide")

choice = input("Enter choice (1/2): ")

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

else:
    print("Invalid input")

