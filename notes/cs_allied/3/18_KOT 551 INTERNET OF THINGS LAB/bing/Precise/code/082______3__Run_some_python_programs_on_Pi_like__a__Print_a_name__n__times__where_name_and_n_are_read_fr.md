#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

To run a Python program on a Raspberry Pi, you need to have Python installed on the Pi. Most Raspberry Pi operating systems come with Python pre-installed, but if not, you can install it using the following command:

```
sudo apt-get install python3
```

Once Python is installed, you can write a Python program to print a name 'n' times, where name and n are read from standard input. Here is an example program that does this:

```python
name = input("Enter a name: ")
n = int(input("Enter the number of times to print the name: "))

for i in range(n):
    print(name)
```

This program first prompts the user to enter a name and the number of times to print the name. The `input()` function is used to read the user's input, and the `int()` function is used to convert the string input to an integer. The program then uses a `for` loop to print the name the specified number of times.

To run this program on the Raspberry Pi, save it to a file with a `.py` extension, such as `print_name.py`, and then run it using the `python3` command:

```
python3 print_name.py
```

This will execute the program and prompt the user to enter the required inputs. Once the inputs are provided, the program will print the name the specified number of times.