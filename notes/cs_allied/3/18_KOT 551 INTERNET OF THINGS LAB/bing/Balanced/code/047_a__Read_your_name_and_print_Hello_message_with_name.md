# Read your name and print Hello message with name

- This is a simple program that takes the user's name as an input and prints a greeting message with the name.
- To write this program, we need to use the following steps:

  1. Declare a variable to store the user's name. A variable is a name that refers to a value in memory. We can use any valid identifier as a variable name, such as `name`, `user_name`, `my_name`, etc. For example, `name = ""` creates a variable named `name` and assigns it an empty string value.
  2. Use the `input()` function to get the user's name from the keyboard. The `input()` function takes an optional argument that is a prompt or message to display to the user. For example, `name = input("Enter your name: ")` will display "Enter your name: " on the screen and wait for the user to type something and press enter. The typed value will be stored in the `name` variable as a string.
  3. Use the `print()` function to display the greeting message with the user's name. The `print()` function takes one or more arguments that are the values to print on the screen, separated by commas. We can use string concatenation (+) or string formatting (f-strings) to combine the user's name with a fixed message. For example, `print("Hello, " + name)` or `print(f"Hello, {name}")` will print "Hello, " followed by the user's name. We can also add a newline character (\n) at the end of the message to move the cursor to the next line.

- Here is an example of the complete program in Python:

```python
# Declare a variable to store the user's name
name = ""

# Get the user's name from the keyboard
name = input("Enter your name: ")

# Print the greeting message with the user's name
print("Hello, " + name + "\n")
```

- Here is an example of the output of the program:

```
Enter your name: Sydney
Hello, Sydney
```