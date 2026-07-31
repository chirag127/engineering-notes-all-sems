#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input

When it comes to programming on a Raspberry Pi, Python is a popular choice due to its simplicity and versatility. In this section, we will learn how to write a Python program to print a name 'n' times, where the name and 'n' are read from standard input.

Here are the steps to follow:

1. Open a terminal on your Raspberry Pi by clicking on the terminal icon in the taskbar or by pressing Ctrl + Alt + T.

2. Once the terminal is open, type the following command to open the Python interpreter:

   ```
   python3
   ```

3. Press Enter to start the Python interpreter.

4. Now, let's write the Python program to print a name 'n' times. Type the following code:

   ```
   name = input("Enter your name: ")
   n = int(input("Enter the number of times you want to print your name: "))
   for i in range(n):
       print(name)
   ```

   This program prompts the user to enter their name and the number of times they want to print their name. It then uses a for loop to print the name 'n' times.

5. Press Enter to run the program.

6. Test the program by entering your name and a number. The program should print your name 'n' times.

   For example, if you enter "John" and "3", the program should output:

   ```
   John
   John
   John
   ```

That's it! You have successfully written a Python program to print a name 'n' times on a Raspberry Pi. This program can be easily customized to print any string 'n' times, making it a useful tool for various programming tasks.