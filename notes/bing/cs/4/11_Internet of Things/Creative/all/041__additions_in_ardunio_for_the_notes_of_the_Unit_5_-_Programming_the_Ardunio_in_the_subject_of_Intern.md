### Additions in Arduino for the notes of the Unit 5 - Programming the Arduino in the subject of Internet of Things

- Addition is one of the four primary arithmetic operations. The operator + (plus) operates on two operands to produce the sum.
- The syntax of the addition operator is:

```c
sum = operand1 + operand2;
```

- The operands and the sum can be of any data type that supports arithmetic operations, such as int, float, double, byte, short, long.
- The addition operation can overflow if the result is larger than that which can be stored in the data type (e.g. adding 1 to an integer with the value 32,767 gives -32,768).
- To avoid overflow, it is recommended to use data types that can accommodate the largest possible result, or to use type casting to convert the operands or the sum to a larger data type.
- For example, to add two bytes and store the result in an int, we can write:

```c
byte a = 200;
byte b = 100;
int c = 0;
c = (int)a + (int)b; // c gets a value of 300
```

- Addition is used to perform various tasks in Arduino programming, such as:
  - Incrementing variables or counters
  - Calculating sums or averages of sensor readings
  - Adding offsets or corrections to values
  - Combining bits or bytes using bitwise operations
  - Concatenating strings using the + operator
- Some mnemonics and learning tricks for the additions in Arduino are:
  - Remember the order of precedence of the operators: parentheses, multiplication and division, addition and subtraction, assignment.
  - Remember the difference between the assignment operator (=) and the equality operator (==). The former assigns a value to a variable, while the latter compares two values and returns true or false.
  - Remember the difference between the increment operator (++) and the addition operator (+). The former increases the value of a variable by one, while the latter adds two values and returns the sum.
  - Remember the difference between the pre-increment (++a) and the post-increment (a++) operators. The former increments the value of a before using it in an expression, while the latter increments the value of a after using it in an expression.
  - Remember the difference between the addition-assignment operator (+=) and the addition operator (+). The former adds a value to a variable and assigns the result to the same variable, while the latter adds two values and returns the sum.
  - Remember the difference between the string concatenation operator (+) and the string append function (concat()). The former creates a new string by joining two strings, while the latter modifies the first string by adding the second string to the end.