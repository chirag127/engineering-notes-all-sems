Hello, I am Sydney, your AI assistant. I can help you run some python programs on Pi. 

To print a name 'n' times, where name and n are read from standard input, you can follow these steps:

- Connect your Pi to a monitor, keyboard, and mouse. Make sure it is powered on and has an internet connection.
- Open a terminal window by clicking on the icon in the top left corner of the screen.
- Type `python3` and press Enter to start the Python interpreter.
- Type the following code in the Python interpreter:

```python
# Read the name and n from standard input
name = input("Enter a name: ")
n = int(input("Enter a number: "))

# Print the name n times using a for loop
for i in range(n):
    print(name)
```

- Press Enter after typing the code. You should see the name printed n times on the screen.
- To exit the Python interpreter, type `exit()` and press Enter.