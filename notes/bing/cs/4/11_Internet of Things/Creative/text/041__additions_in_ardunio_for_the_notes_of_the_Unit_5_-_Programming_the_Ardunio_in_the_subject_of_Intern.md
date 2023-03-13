### Additions in Arduino

- Addition is one of the four primary arithmetic operations. The operator + (plus) operates on two operands to produce the sum .
- To add numbers on the Arduino, we use the addition operator (+). The example below shows how to add two numbers together.

```c
int a = 2; // declare and initialize a variable named a with the value 2
int b = 7; // declare and initialize a variable named b with the value 7
int sum; // declare a variable named sum
sum = a + b; // assign the value of a + b to the variable sum
```

- The addition operator can also be used to concatenate strings. The example below shows how to join two strings together.

```c
String firstName = "John"; // declare and initialize a string variable named firstName with the value "John"
String lastName = "Doe"; // declare and initialize a string variable named lastName with the value "Doe"
String fullName; // declare a string variable named fullName
fullName = firstName + " " + lastName; // assign the value of firstName + " " + lastName to the variable fullName
```

- There is also a compound addition operator (+=) that performs addition on a variable with another constant or variable and assigns the result to the same variable. The example below shows how to use the compound addition operator.

```c
int x = 5; // declare and initialize a variable named x with the value 5
x += 3; // add 3 to x and assign the result to x
// x now has the value 8
```