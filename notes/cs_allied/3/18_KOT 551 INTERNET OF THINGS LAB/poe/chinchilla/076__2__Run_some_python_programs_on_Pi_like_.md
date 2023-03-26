#### 2. Run some python programs on Pi like:

Raspberry Pi is a powerful single-board computer that can be used for a variety of purposes. One of the most popular uses of Raspberry Pi is for running Python programs. Python is a popular programming language that is widely used for web development, data analysis, and artificial intelligence applications.

If you are new to Raspberry Pi and Python, here are some basic steps to get started with running Python programs on your Raspberry Pi:

1. Install Python on your Raspberry Pi:
   - Raspberry Pi comes with a pre-installed version of Python, but you may want to install the latest version of Python for your projects. You can do this by running the following command in your terminal: `sudo apt-get install python3`.

2. Create a Python program:
   - Once you have installed Python on your Raspberry Pi, you can start writing Python programs. You can use any text editor, such as Nano or Vim, to create a Python program. Here's an example of a simple Python program that prints "Hello, World!":

   ```
   # This is a Python program that prints "Hello, World!"
   print("Hello, World!")
   ```

3. Save the Python program:
   - Save the Python program with a .py extension, such as `hello_world.py`.

4. Run the Python program:
   - To run the Python program, open your terminal and navigate to the directory where the program is saved. Then, run the following command: `python3 hello_world.py`. The output should be "Hello, World!".

5. Use Python libraries:
   - Python has a vast library of modules that can be used to perform various tasks. You can install these modules on your Raspberry Pi using the `pip` package manager. Here's an example of how to install the `numpy` module:

   ```
   sudo apt-get install python3-pip
   pip3 install numpy
   ```

6. Import Python libraries:
   - Once you have installed a Python library, you can import it into your Python program using the `import` statement. Here's an example of how to import the `numpy` module:

   ```
   import numpy as np
   ```

   - Now, you can use the functions and classes provided by the `numpy` module in your Python program.

7. Run Python programs on boot:
   - If you want to run a Python program on boot, you can add it to the `/etc/rc.local` file. Here's an example of how to add a Python program called `my_program.py`:

   ```
   sudo nano /etc/rc.local
   ```
   
   - Add the following line before the `exit 0` line:

   ```
   python3 /path/to/my_program.py &
   ```

   - Save the file and exit. Now, the Python program will run on boot.

In conclusion, running Python programs on Raspberry Pi is a great way to learn programming and build cool projects. By following the above steps, you can start running your own Python programs on your Raspberry Pi.