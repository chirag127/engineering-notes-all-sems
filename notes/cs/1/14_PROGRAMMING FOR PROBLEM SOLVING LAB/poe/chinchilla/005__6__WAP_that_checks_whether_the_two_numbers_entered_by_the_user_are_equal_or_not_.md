## 6. WAP that checks whether the two numbers entered by the user are equal or not.

In this program, we will be taking two numbers as input from the user and checking whether they are equal or not. Here are the steps to follow:

1. Start the program by defining the main function.
2. Inside the main function, take two numbers as input from the user using the input() function. Store them in variables num1 and num2.
3. Use an if statement to check whether num1 is equal to num2.
4. If num1 is equal to num2, print a message to the user saying that the numbers are equal.
5. If num1 is not equal to num2, print a message to the user saying that the numbers are not equal.
6. End the program.

Here is the Python code for the above steps:

```
def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    if num1 == num2:
        print("The numbers are equal.")
    else:
        print("The numbers are not equal.")
        
if __name__ == "__main__":
    main()
```

Make sure to follow the above steps and syntax properly while writing the code. This program will help you understand how to take user input and use an if statement to check for equality between two numbers.