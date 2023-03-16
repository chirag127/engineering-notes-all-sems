# 2. Run some python programs on Pi like:

- Python is a popular programming language that can be used to create various applications on the Raspberry Pi, such as games, web servers, robots, etc.
- To run a python program on the Pi, you need to have python installed on your system. You can check if you have python by typing `python --version` in the terminal. If you see a version number, such as `Python 3.7.3`, then you have python installed. If not, you can install it by typing `sudo apt install python3` in the terminal.
- To write a python program, you can use any text editor, such as nano, vim, or IDLE. To open a text editor, you can type its name in the terminal, such as `nano hello.py`. This will create a new file called `hello.py` and open it in the nano editor. You can then type your python code in the editor, such as `print("Hello, world!")`. To save and exit the editor, you can press `Ctrl+X`, then `Y`, then `Enter`.
- To run a python program, you can type `python3 hello.py` in the terminal, where `hello.py` is the name of your file. This will execute your python code and display the output in the terminal, such as `Hello, world!`.
- You can also run a python program in interactive mode, which allows you to type and execute python commands one by one. To enter interactive mode, you can type `python3` in the terminal, without specifying a file name. You will see a prompt, such as `>>>`, where you can type your python commands, such as `print("Hello, world!")`. To exit interactive mode, you can type `exit()` or press `Ctrl+D`.
- Some examples of python programs that you can run on the Pi are:

  - A simple calculator that can perform basic arithmetic operations, such as `+`, `-`, `*`, `/`, and `**`. You can use the `input()` function to get the user's input, and the `eval()` function to evaluate the expression. For example:

    ```python
    # A simple calculator
    print("Enter an expression to calculate:")
    expression = input()
    result = eval(expression)
    print("The result is:", result)
    ```

  - A dice simulator that can generate a random number between 1 and 6, simulating the roll of a dice. You can use the `random` module to generate random numbers, and the `while` loop to repeat the program until the user wants to quit. For example:

    ```python
    # A dice simulator
    import random
    print("Welcome to the dice simulator!")
    while True:
        print("Press Enter to roll the dice, or Q to quit:")
        choice = input()
        if choice.lower() == "q":
            break
        else:
            dice = random.randint(1, 6)
            print("You rolled a", dice)
    print("Thank you for playing!")
    ```

  - A LED blinker that can turn on and off a LED connected to the Pi's GPIO pins. You can use the `gpiozero` module to control the GPIO pins, and the `time` module to create delays. For example:

    ```python
    # A LED blinker
    from gpiozero import LED
    import time
    # Create a LED object connected to GPIO pin 17
    led = LED(17)
    print("Press Ctrl+C to stop the program")
    try:
        while True:
            # Turn on the LED
            led.on()
            # Wait for 1 second
            time.sleep(1)
            # Turn off the LED
            led.off()
            # Wait for 1 second
            time.sleep(1)
    except KeyboardInterrupt:
        # Turn off the LED and exit the program
        led.off()
        print("Program stopped")
    ```