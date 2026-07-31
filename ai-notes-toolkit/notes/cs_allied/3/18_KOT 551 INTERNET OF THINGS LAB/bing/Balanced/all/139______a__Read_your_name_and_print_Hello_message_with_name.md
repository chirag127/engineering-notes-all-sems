#### a) Read your name and print Hello message with name

- To read your name, you need to use an input function that takes a string as an argument and returns the user's input as a string.
- For example, in Python, you can use the input() function to read your name from the keyboard and store it in a variable called name:

```python
name = input("Enter your name: ")
```

- To print a Hello message with your name, you need to use a print function that takes a string as an argument and displays it on the screen.
- For example, in Python, you can use the print() function to print a Hello message with your name by concatenating the strings "Hello" and name with a comma or a plus sign:

```python
print("Hello", name) # using comma
print("Hello" + name) # using plus sign
```

- Here is a complete example of a Python program that reads your name and prints a Hello message with your name:

```python
name = input("Enter your name: ") # read name from keyboard
print("Hello", name) # print Hello message with name
```

- If you run this program and enter your name as Sydney, the output will be:

```python
Enter your name: Sydney
Hello Sydney
```