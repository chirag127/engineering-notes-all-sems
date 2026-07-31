#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- To write a python program, you need to use a text editor such as nano, vim, or idle. You can launch a text editor by typing its name in the terminal, such as `nano` or `idle3`.
- To save a python program, you need to give it a name with a `.py` extension, such as `print_name.py`. You can save your program by pressing `Ctrl+O` in nano, or by choosing `File -> Save` in idle.
- To run a python program, you need to type `python3` followed by the name of your program, such as `python3 print_name.py`. You can run your program by pressing `Enter` in the terminal, or by choosing `Run -> Run Module` in idle.
- To print a name 'n' times, where name and n are read from standard input, you need to use the `input` function to get the user input, and the `print` function to display the output. You also need to use a `for` loop to repeat the printing 'n' times. Here is an example of a python program that does this:

```python
# print_name.py
# This program prints a name 'n' times, where name and n are read from standard input

# Get the name from the user
name = input("Enter a name: ")

# Get the number of times to print from the user
n = int(input("Enter a number: ")) # Convert the input to an integer

# Use a for loop to print the name 'n' times
for i in range(n):
    print(name)
```

- To test your program, you can run it and enter some values for the name and the number. For example, if you enter `Alice` and `5`, you should see the following output:

```python
Enter a name: Alice
Enter a number: 5
Alice
Alice
Alice
Alice
Alice
```