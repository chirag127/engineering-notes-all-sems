# Additions in Arduino

- Addition is one of the four primary arithmetic operations in Arduino.
- The operator + (plus) operates on two operands to produce the sum.
- The syntax for addition is: `sum = operand1 + operand2;`
- The operands can be variables or constants of any numeric data type, such as int, float, double, byte, short, or long.
- The sum variable must be of the same or larger data type as the operands, otherwise the result may be truncated or incorrect.
- For example, to add two numbers on the Arduino, we can write:

```c
int a = 2; // declare and initialize a variable of type int
int b = 7; // declare and initialize another variable of type int
int sum; // declare a variable of type int to store the sum
sum = a + b; // perform the addition and assign the result to sum
```

- Arduino also provides a shorthand notation for addition, using the compound assignment operator +=.
- The syntax for compound addition is: `variable += value;`
- This is equivalent to: `variable = variable + value;`
- The variable and the value must be of the same or compatible data types, otherwise the result may be truncated or incorrect.
- For example, to increment a variable by one on the Arduino, we can write:

```c
int x = 10; // declare and initialize a variable of type int
x += 1; // add one to x and assign the result to x
```

- Addition can be used to perform various calculations and operations on the Arduino, such as adding sensor readings, calculating averages, generating PWM signals, etc.
- Addition can also be used to concatenate strings, which are sequences of characters enclosed in double quotes.
- The syntax for string concatenation is: `string1 + string2;`
- The result is a new string that contains the characters of string1 followed by the characters of string2.
- For example, to concatenate two strings on the Arduino, we can write:

```c
String name = "Sydney"; // declare and initialize a variable of type String
String greeting = "Hello, " + name; // concatenate "Hello, " and name and assign the result to greeting
```