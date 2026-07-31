#### a) Read your name and print Hello message with name

- To read your name and print a hello message with it, you need to use an input function and a print function in Python.
- The input function allows you to get a string from the user and store it in a variable. The print function allows you to display a string on the screen.
- For example, you can write the following code:

```python
name = input("Enter your name: ") # This will prompt the user to enter their name and store it in the variable name
print("Hello, " + name) # This will print Hello, followed by the value of the variable name
```

- If you run this code and enter John as your name, the output will be:

```
Enter your name: John
Hello, John
```

- You can also use formatted strings to print the hello message with the name. Formatted strings are strings that have placeholders for variables that are replaced by their values when the string is printed. You can create a formatted string by using an f before the string and enclosing the variable name in curly braces. For example, you can write the following code:

```python
name = input("Enter your name: ") # This will prompt the user to enter their name and store it in the variable name
print(f"Hello, {name}") # This will print Hello, followed by the value of the variable name
```

- If you run this code and enter Jane as your name, the output will be:

```
Enter your name: Jane
Hello, Jane
```

- This is how you can read your name and print a hello message with it in Python.