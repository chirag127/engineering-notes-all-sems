### Running Python Programs on Raspberry Pi

Here are the steps to run a Python program on a Raspberry Pi:

1. Open the terminal on your Raspberry Pi.
2. Navigate to the directory where your Python program is saved using the `cd` command.
3. Use the command `python program_name.py` to run your program.

Now, let's try running a Python program on Raspberry Pi that prints a name 'n' times, where name and n are read from standard input.

1. Open the terminal on your Raspberry Pi.
2. Create a new file using the command `nano name_printer.py`.
3. Type the following code into the file:

```
name = input("Enter a name: ")
n = int(input("Enter a number: "))

for i in range(n):
    print(name)
```

4. Save the file using `Ctrl+X`, `Y`, and `Enter`.
5. Run the program using the command `python name_printer.py`.
6. Enter a name and a number when prompted.
7. The program will now print the name 'n' times.

Congratulations! You have just successfully run a Python program on Raspberry Pi. You can now try writing and running more programs on your own.