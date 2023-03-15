 Here is the content in markdown format:

### Additions in Arduino for the notes of the Unit 5 - Programming the Arduino in the subject of Internet of Things

1. Libraries - Libraries provide additional functionality for using certain sensors/modules. For example, if using an LCD display, the LiquidCrystal library can be used which has functions to interface with the LCD. This saves you from having to write all the low-level code to control the LCD.

2. Data Types - Arduino supports certain data types like int, float, double, boolean, char, etc. which can be used to store values from sensors or in variables. For example, an int can store a whole number between -32768 to 32767 and is useful for sensor values like temperature. A float/double can store decimal values and is useful for computations.

3. Variables - Variables can be used to store values from sensors or intermediate values in computations. For example, a variable named temp can be used to store a temperature value from a temperature sensor. The variable can then be used in the code for decision making or other purposes.

4. Control Structures - Control structures like if-else statements, for loops, while loops, etc. can be used to control the flow of the program. For example, an if statement can be used to check if a temperature value is above a certain threshold and if so, trigger a cooling fan. Loops can be used to repeat a set of tasks multiple times.

5. Functions - Functions allow you to organize your code into reusable blocks. For example, you can create a function to read a sensor value and return the value. This function can then be called from multiple places in the code whenever the sensor value is needed. This makes the code modular, easier to read and debug.

![Arduino Programming Flowchart](https://www.circuitbasics.com/wp-content/uploads/2015/10/Arduino-Flowchart.png)

*Image showing the basic flow of an Arduino program*

**Advantages** - Makes the code modular, reusable, easier to read and debug.
**Disadvantages** - May introduce overhead if functions are very small.
**Applications** - Commonly used in Arduino programs to organize the code.