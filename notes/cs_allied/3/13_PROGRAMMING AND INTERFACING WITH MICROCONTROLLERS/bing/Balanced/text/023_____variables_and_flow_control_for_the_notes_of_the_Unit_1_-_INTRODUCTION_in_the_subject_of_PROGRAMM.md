### Variables and Flow Control

- A variable is a named memory location that can store a value of a specific data type, such as integer, float, char, string, etc.
- A variable has a name (also called an identifier) that follows certain rules, such as starting with a letter or underscore, not containing spaces or special symbols, etc.
- A variable can be declared by specifying its data type and name, optionally followed by an assignment operator (=) and an initial value. For example, `int x;` or `float y = 3.14;`
- A variable can be assigned a new value at any point in the program by using the assignment operator (=). For example, `x = 10;` or `y = y + 1;`
- A variable can be used in expressions, statements, and functions by referring to its name. For example, `z = x + y;` or `printf("%d\n", x);`
- A variable has a scope, which is the part of the program where it can be accessed. A variable declared inside a function is local to that function and cannot be accessed outside of it. A variable declared outside of any function is global and can be accessed by any function in the program.
- A variable has a lifetime, which is the duration of time for which it exists in memory. A local variable is created when its function is called and destroyed when its function returns. A global variable is created when the program starts and destroyed when the program ends.

- Flow control is the mechanism that determines the order of execution of statements in a program based on certain conditions or iterations.
- Flow control can be achieved by using conditional statements, such as if, else, switch, etc., that execute a block of code only if a certain condition is true or false.
- Flow control can also be achieved by using loop statements, such as for, while, do-while, etc., that execute a block of code repeatedly until a certain condition is met or not met.
- Flow control can also be achieved by using jump statements, such as break, continue, return, goto, etc., that alter the normal flow of execution by transferring control to another part of the program.
- Flow control can also be achieved by using function calls, which invoke a set of statements defined in another part of the program and return control to the caller after the function is executed.