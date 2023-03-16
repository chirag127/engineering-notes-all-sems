#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

To run a Python program on a Raspberry Pi, you will need to have Python installed on your device. Most Raspberry Pi operating systems come with Python pre-installed, but if you need to install it, you can do so by running the following command in the terminal:

```
sudo apt-get install python3
```

Once you have Python installed, you can write a program to print a name 'n' times, where the name and 'n' are read from standard input. Here is an example of such a program:

```python
name = input("Enter a name: ")
n = int(input("Enter the number of times to print the name: "))

for i in range(n):
    print(name)
```

This program prompts the user to enter a name and the number of times to print it. The `input()` function is used to read the user's input, and the `int()` function is used to convert the input for 'n' into an integer. The program then uses a `for` loop to print the name 'n' times.

To run this program on your Raspberry Pi, save it to a file with a `.py` extension, such as `print_name.py`. Then, open a terminal and navigate to the directory where you saved the file. Finally, run the program by entering the command `python3 print_name.py`.