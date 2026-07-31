### 13. Write a program to perform constant propagation.

Constant propagation is a technique used in compiler optimization that replaces the variable with its constant value, which is known at compile time. This can help reduce the number of instructions executed, thereby improving the performance of the program.

Here are the steps to write a program to perform constant propagation:

1. Parse the input program: The input program needs to be parsed to extract information about the variables and their values. This can be done using a parser or by manually reading the program code.

2. Create a symbol table: A symbol table needs to be created to store information about the variables and their values. The symbol table can be implemented as a hash table or a dictionary.

3. Perform constant folding: Constant folding is the process of evaluating constant expressions at compile time. This can be done by replacing the expression with its constant value. For example, the expression "2+3" can be replaced with "5".

4. Perform constant propagation: Constant propagation is the process of replacing the variable with its constant value. This can be done by looking up the value of the variable in the symbol table and replacing the variable with its value. For example, if the variable "x" has a value of 5, then the expression "x+3" can be replaced with "8".

5. Output the optimized program: The optimized program can be output to a file or displayed on the screen.

In conclusion, constant propagation is a useful technique for improving the performance of programs. By replacing variables with their constant values, the number of instructions executed can be reduced, resulting in faster execution times. Implementing constant propagation in a program can be done by following the steps outlined above.