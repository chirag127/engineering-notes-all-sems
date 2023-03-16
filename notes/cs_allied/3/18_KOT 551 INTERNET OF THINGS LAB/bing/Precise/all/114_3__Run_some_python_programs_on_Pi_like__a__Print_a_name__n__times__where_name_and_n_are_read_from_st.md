# Running Python Programs on Raspberry Pi

One of the many things you can do with a Raspberry Pi is to run Python programs. Here is an example of a simple Python program that can be run on a Raspberry Pi:

## Example: Printing a Name 'n' Times

This program will print a name 'n' times, where the name and the value of 'n' are read from standard input.

```python
name = input("Enter a name: ")
n = int(input("Enter the number of times to print the name: "))

for i in range(n):
    print(name)
```

To run this program on a Raspberry Pi, follow these steps:

1. Open a terminal window on the Raspberry Pi.
2. Use a text editor to create a new file with the above Python code. Save the file with a `.py` extension, for example `print_name.py`.
3. In the terminal, navigate to the directory where you saved the file.
4. Type the command `python3 print_name.py` and press enter to run the program.
5. Follow the prompts to enter the name and the number of times to print it.

After entering the required information, the program will print the name the specified number of times.