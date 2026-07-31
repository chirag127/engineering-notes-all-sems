# Read your name and print Hello message with name

- This is a simple program that takes the user's name as an input and prints a greeting message with the name.
- To write this program, we need to use the following steps:

  1. Declare a variable to store the user's name. A variable is a name that refers to a value in memory. We can use any valid identifier as a variable name, such as `name`, `user_name`, `my_name`, etc. For example, `name = ""` creates a variable called `name` and assigns it an empty string value.
  2. Use the `input()` function to get the user's name from the keyboard. The `input()` function takes an optional argument that is a prompt or message to display to the user. For example, `name = input("Enter your name: ")` will display "Enter your name: " on the screen and wait for the user to type something and press enter. The typed value will be stored in the `name` variable as a string.
  3. Use the `print()` function to display the greeting message with the user's name. The `print()` function takes one or more arguments that are the values to print on the screen, separated by commas. We can use the `+` operator to concatenate or join two strings together. For example, `print("Hello, " + name)` will print "Hello, " followed by the value of the `name` variable.
- Here is an example of the complete program in Python:

```python
# Read your name and print Hello message with name

# Declare a variable to store the user's name
name = ""

# Use the input() function to get the user's name from the keyboard
name = input("Enter your name: ")

# Use the print() function to display the greeting message with the user's name
print("Hello, " + name)
```

- Here is an example of the output of the program:

```
Enter your name: Sydney
Hello, Sydney
```