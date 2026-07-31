### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input

Here are some points to help you run a Python program on Pi to print a name 'n' number of times, where name and n are read from standard input:

- First, open the terminal on your Pi and navigate to the directory where you want to save your Python program.
- Create a new Python file using the command `nano print_name.py` (you can use any text editor of your choice).
- In the new file, type the following code:

```python
name = input("Enter your name: ")
n = int(input("Enter the number of times you want to print your name: "))

for i in range(n):
    print(name)
```

- Save the file using the command `Ctrl + X`, then `Y` and finally `Enter`.
- To run the program, type `python3 print_name.py` in the terminal.
- The program will prompt you to enter your name and the number of times you want to print it.
- Once you enter the values, the program will print your name the specified number of times.

Congratulations! You have successfully run a Python program on your Pi that prints a name 'n' number of times. Keep practicing with more Python programs to hone your programming skills on the Pi.