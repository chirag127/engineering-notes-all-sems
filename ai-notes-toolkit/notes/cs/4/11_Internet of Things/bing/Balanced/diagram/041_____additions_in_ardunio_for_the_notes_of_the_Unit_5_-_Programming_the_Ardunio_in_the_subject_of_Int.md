# Additions in Arduino

- Addition is one of the four primary arithmetic operations. The operator + (plus) operates on two operands to produce the sum.
- To add two or more numbers, we use the addition (+) operator. The following example shows how to add two numbers:

```c
int a = 2; // define and assign a variable a
int b = 3; // define and assign a variable b
int sum; // define a variable sum
sum = a + b; // assign the result of a + b to sum
Serial.println(sum); // print the value of sum to the serial monitor
```

- The output of the above code will be 5.
- We can also use the compound addition operator (+=) to perform addition on a variable with another constant or variable. The following example shows how to use the compound addition operator:

```c
int x = 2; // define and assign a variable x
x += 1; // add 1 to x and assign the result to x
Serial.println(x); // print the value of x to the serial monitor
```

- The output of the above code will be 3.
- The addition operator can also be used to concatenate strings. The following example shows how to concatenate two strings using the addition operator:

```c
String name = "John"; // define and assign a string variable name
String greeting = "Hello, " + name; // concatenate "Hello, " and name using the addition operator
Serial.println(greeting); // print the value of greeting to the serial monitor
```

- The output of the above code will be Hello, John.