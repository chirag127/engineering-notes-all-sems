#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

To run a Python program on a Raspberry Pi, you will need to have Python installed on the device. Most Raspberry Pi models come with Python pre-installed, but you can check if it is installed by opening a terminal and typing `python3 --version`. If Python is not installed, you can install it by running `sudo apt-get install python3`.

Here is an example of a Python program that will print a name 'n' times, where the name and n are read from standard input:

```python
name = input("Enter a name: ")
n = int(input("Enter the number of times to print the name: "))

for i in range(n):
    print(name)
```

To run this program on a Raspberry Pi, you can save it to a file with a `.py` extension, such as `print_name.py`, and then run it from the terminal by navigating to the directory where the file is saved and typing `python3 print_name.py`.

This will prompt you to enter a name and the number of times to print it, and then it will print the name the specified number of times. For example, if you enter "Alice" as the name and "3" as the number of times to print it, the program will output:

```
Alice
Alice
Alice
```