# 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input

- To run a python program on Pi, you need to have a Raspberry Pi device, a power supply, a micro SD card, a keyboard, a mouse, and a monitor. You also need to install the Raspberry Pi OS on the SD card and insert it into the Pi.
- To write a python program, you need to have a text editor or an IDE (Integrated Development Environment) that supports python syntax. You can use the default editor called Thonny, which comes with the Raspberry Pi OS, or you can install other editors like VS Code, PyCharm, etc.
- To save a python program, you need to give it a name with the .py extension, such as hello.py, and save it in a folder of your choice. You can use the File Manager to create and navigate folders on the Pi.
- To run a python program, you need to open a terminal window and type the command `python3 filename.py`, where filename is the name of your program. For example, to run hello.py, you would type `python3 hello.py`. You can also run a python program from Thonny by clicking the Run button.
- To print a name 'n' times, where name and n are read from standard input, you need to use the input() function to get the user input and store it in variables. Then you need to use a for loop to repeat the print() function 'n' times. For example, the following program will print the name 'Alice' 5 times:

```python
# get the name from the user
name = input("Enter a name: ")

# get the number of times to print from the user
n = int(input("Enter a number: "))

# use a for loop to print the name n times
for i in range(n):
  print(name)
```

- The output of the program will look like this:

```
Enter a name: Alice
Enter a number: 5
Alice
Alice
Alice
Alice
Alice
```