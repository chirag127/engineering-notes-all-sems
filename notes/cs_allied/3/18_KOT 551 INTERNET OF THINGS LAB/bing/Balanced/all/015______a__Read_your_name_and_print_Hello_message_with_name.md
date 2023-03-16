#### a) Read your name and print Hello message with name

- To read your name and print a Hello message with it, you need to use an input function and a print function in your code.
- An input function allows you to enter some data from the keyboard and store it in a variable. For example, `name = input("Enter your name: ")` will prompt you to enter your name and assign it to the variable `name`.
- A print function allows you to display some data on the screen. For example, `print("Hello, world!")` will print the string "Hello, world!" on the screen.
- To print a Hello message with your name, you need to concatenate the string "Hello, " with the variable `name` and a punctuation mark. For example, `print("Hello, " + name + "!")` will print the string "Hello, " followed by the value of `name` and a "!" on the screen.
- Here is an example of a complete code that reads your name and prints a Hello message with it:

```python
# Read your name and print Hello message with name
name = input("Enter your name: ") # Prompt the user to enter their name and store it in the variable name
print("Hello, " + name + "!") # Print the string "Hello, " followed by the value of name and a "!" on the screen
```

- If you run this code, you will see something like this:

```
Enter your name: Sydney
Hello, Sydney!
```