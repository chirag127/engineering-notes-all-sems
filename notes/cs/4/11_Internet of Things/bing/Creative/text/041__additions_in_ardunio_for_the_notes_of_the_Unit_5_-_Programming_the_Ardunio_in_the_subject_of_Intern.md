### Additions in Arduino

- Addition is one of the four primary arithmetic operations. The operator + (plus) operates on two operands to produce the sum.
- To add numbers on the Arduino, we use the addition operator (+). The example below shows how to add two numbers together.

```c
int a = 2;
int b = 7;
int sum;
sum = a + b; // the variable 'sum' gets a value of 9 after this statement is executed
```

- We can also add two constant values and store the result in a variable as shown below.

```c
int sum;
sum = 2 + 10; // the variable 'sum' stores a value of 12
```

- Constant values and variables can also be added together and the result stored in a variable as shown here.

```c
int a = 3;
int sum;
sum = a + 24; // the variable 'sum' stores a value of 27
```

- The addition operation can overflow if the result is larger than that which can be stored in the data type (e.g. adding 1 to an integer with the value 32,767 gives -32,768).
- If one of the numbers (operands) are of the type float or of type double, floating point math will be used for the calculation.
- If the operands are of float / double data type and the variable that stores the sum is an integer, then only the integral part is stored and the fractional part of the number is lost.

```c
float a = 5.5;
float b = 6.6;
int c = 0;
c = a + b; // the variable 'c' stores a value of 12 only as opposed to the expected sum of 12.1
```

- There is also a compound addition operator (+=) that performs addition on a variable with another constant or variable and assigns the result to the same variable.

```c
int a = 5;
a += 3; // equivalent to a = a + 3; the variable 'a' stores a value of 8
```