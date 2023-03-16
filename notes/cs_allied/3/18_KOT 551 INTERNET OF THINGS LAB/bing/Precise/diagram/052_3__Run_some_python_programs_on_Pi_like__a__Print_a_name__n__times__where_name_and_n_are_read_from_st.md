# Running Python Programs on Raspberry Pi

One of the many uses of a Raspberry Pi is to run Python programs. Here is an example of a simple Python program that can be run on a Raspberry Pi:

## Example: Printing a Name 'n' Times

This program takes a name and a number 'n' as input from the user and prints the name 'n' times.

```python
name = input("Enter a name: ")
n = int(input("Enter a number: "))

for i in range(n):
    print(name)
```

To run this program on a Raspberry Pi, follow these steps:

1. Open a terminal window on the Raspberry Pi.
2. Use a text editor to create a new file with the above Python code. Save the file with a `.py` extension, for example `print_name.py`.
3. In the terminal, navigate to the directory where the file was saved.
4. Run the program by typing `python3 print_name.py` and pressing enter.
5. Follow the prompts to enter a name and a number.
6. The program will print the name the specified number of times.

This is just one example of a Python program that can be run on a Raspberry Pi. There are many other possibilities and applications for using Python on a Raspberry Pi.