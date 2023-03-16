# Additions in Arduino

- Addition is one of the four primary arithmetic operations. The operator + (plus) operates on two operands to produce the sum .
- To add numbers on the Arduino, we use the addition operator (+). The example below shows how to add two numbers together.

```c
int a = 2; // declare and initialize a variable a with value 2
int b = 7; // declare and initialize a variable b with value 7
int sum; // declare a variable sum
sum = a + b; // assign the sum of a and b to the variable sum
```

- The addition operator can also be used to concatenate strings. For example, to join two strings together, we use the + operator.

```c
String firstName = "John"; // declare and initialize a string variable firstName with value "John"
String lastName = "Doe"; // declare and initialize a string variable lastName with value "Doe"
String fullName; // declare a string variable fullName
fullName = firstName + " " + lastName; // assign the concatenation of firstName, a space, and lastName to the variable fullName
```

- There is also a compound addition operator (+=) that performs addition on a variable with another constant or variable and assigns the result to the same variable . For example, to increment a variable by 1, we use the += operator.

```c
int counter = 0; // declare and initialize a variable counter with value 0
counter += 1; // increment counter by 1 and assign the result to counter
```

- The compound addition operator can also be used to append strings. For example, to add a character to the end of a string, we use the += operator.

```c
String message = "Hello"; // declare and initialize a string variable message with value "Hello"
message += "!"; // append a "!" character to the end of message and assign the result to message
```