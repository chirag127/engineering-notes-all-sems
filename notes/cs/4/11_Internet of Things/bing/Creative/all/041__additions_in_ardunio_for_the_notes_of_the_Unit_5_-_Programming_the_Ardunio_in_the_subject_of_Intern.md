### Additions in Arduino for the notes of the Unit 5 - Programming the Arduino in the subject of Internet of Things

- Addition is one of the four primary arithmetic operations in Arduino. The operator + (plus) operates on two operands to produce the sum.
- The syntax for addition is: `sum = operand1 + operand2;` where sum is a variable that stores the result of the addition, and operand1 and operand2 are variables or constants that can be of the data types int, float, double, byte, short, or long.
- For example, the following code snippet adds two integers and stores the result in another integer variable:

```c
int a = 5; // declare and initialize an integer variable a with the value 5
int b = 10; // declare and initialize an integer variable b with the value 10
int c = 0; // declare and initialize an integer variable c with the value 0
c = a + b; // add a and b and store the result in c
// the variable c now has a value of 15
```

- Some notes and warnings about addition in Arduino are:
  - The addition operation can overflow if the result is larger than that which can be stored in the data type (e.g. adding 1 to an integer with the value 32,767 gives -32,768).
  - If one of the operands is of the type float or double, floating point math will be used for the calculation.
  - If the operands are of float / double data type and the variable that stores the sum is an integer, then only the integral part is stored and the fractional part of the number is lost. For example:

```c
float a = 5.5; // declare and initialize a float variable a with the value 5.5
float b = 6.6; // declare and initialize a float variable b with the value 6.6
int c = 0; // declare and initialize an integer variable c with the value 0
c = a + b; // add a and b and store the result in c
// the variable c now has a value of 12 only as opposed to the expected sum of 12.1
```

- Addition can be used for various purposes in Arduino programming, such as:
  - Calculating the sum of sensor readings or other inputs
  - Incrementing or decrementing a variable by a certain amount
  - Combining bits or bytes using bitwise operations
  - Concatenating strings using the String class
  - Adding time intervals using the millis() or micros() functions
- A possible mnemonic to remember the syntax and usage of addition in Arduino is: **A**dd **P**lus **S**ign **T**o **S**um **T**wo **O**perands.