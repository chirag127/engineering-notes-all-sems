# Read your name and print Hello message with name

- This is a simple program that takes the user's name as an input and prints a greeting message with the name.
- To write this program, we need to use some basic concepts of programming, such as variables, data types, input and output functions, and string concatenation.
- A variable is a name that refers to a value stored in the memory. We can assign a value to a variable using the equal sign (=).
- A data type is a category of values that have certain properties and operations. For example, a string is a data type that represents a sequence of characters, such as "Hello" or "Sydney".
- An input function is a function that allows the user to enter some data and returns it as a value. For example, the input() function in Python takes a string as an argument and displays it as a prompt, then waits for the user to type something and press enter, and returns the user's input as a string.
- An output function is a function that displays some data on the screen or another device. For example, the print() function in Python takes one or more arguments and prints them to the standard output, which is usually the console or the terminal.
- String concatenation is an operation that joins two or more strings together to form a new string. For example, the + operator in Python can be used to concatenate strings, such as "Hello" + "World" = "HelloWorld".
- To read the user's name and print a hello message with the name, we can follow these steps:
  - Declare a variable called name and assign it the value returned by the input() function with the argument "What is your name? ".
  - Declare a variable called message and assign it the value of the string "Hello " concatenated with the value of the name variable.
  - Call the print() function with the message variable as the argument to display the greeting message on the screen.
- Here is an example of the program written in Python:

```python
# Read the user's name and store it in a variable
name = input("What is your name? ")

# Create a greeting message by concatenating "Hello " and the name
message = "Hello " + name

# Print the message on the screen
print(message)
```

- Here is an example of the output of the program when the user enters "Sydney" as the name:

```text
What is your name? Sydney
Hello Sydney
```