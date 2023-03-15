#### Function Oriented Design in Software Design

Function Oriented Design is a method to software design where the model is decomposed into a set of interacting units or modules where each unit or module has a clearly defined function  . Thus, the system is designed from a functional viewpoint.

A generic procedure for function oriented design is as follows:

- Start with a high level description of what the software/program does.
- Identify the major functions and data flows in the system using a data flow diagram (DFD).
- Refine the DFD by decomposing each function into sub-functions and data into data dictionaries.
- Assign the sub-functions to modules and define the interfaces and control mechanisms among them.
- Design the internal structure and algorithm of each module using structured design techniques.

An example of function oriented design for a simple calculator program is given below:

```python
# A simple calculator program that performs basic arithmetic operations

# Define the main function that takes the user input and calls the appropriate sub-function
def main():
    # Display the menu of operations
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Take the user choice
    choice = int(input("Enter your choice: "))

    # Validate the choice
    if choice < 1 or choice > 5:
        print("Invalid choice. Please try again.")
        main()
    elif choice == 5:
        print("Thank you for using the calculator. Goodbye.")
        exit()
    else:
        # Take the operands
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Call the corresponding sub-function based on the choice
        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)

        # Display the result
        print("The result is: ", result)

        # Ask the user if they want to continue
        answer = input("Do you want to continue? (y/n): ")
        if answer.lower() == "y":
            main()
        else:
            print("Thank you for using the calculator. Goodbye.")
            exit()

# Define the sub-function for addition
def add(x, y):
    return x + y

# Define the sub-function for subtraction
def subtract(x, y):
    return x - y

# Define the sub-function for multiplication
def multiply(x, y):
    return x * y

# Define the sub-function for division
def divide(x, y):
    # Check for zero division error
    if y == 0:
        print("Error: Cannot divide by zero.")
        main()
    else:
        return x / y

# Call the main function
main()
```