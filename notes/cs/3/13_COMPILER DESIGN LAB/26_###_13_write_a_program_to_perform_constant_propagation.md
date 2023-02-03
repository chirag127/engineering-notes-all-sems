### 13. Write a program to perform constant propagation.

Constant propagation is a compiler optimization technique that replaces expressions with their constant values, if known, to simplify the code and improve performance. To perform constant propagation, a program must:

1. Analyze the code to identify expressions that can be evaluated to a constant value.
2. Replace the expressions with their constant values.
3. Repeat the analysis and replacement process until no more expressions can be simplified.

The program should be able to handle expressions that contain variables and constants, as well as basic arithmetic operations such as addition, subtraction, multiplication, and division. It should also be able to handle control flow statements such as if-else and loops, and track changes to variables as the code is executed. The implementation can be done in various programming languages such as C, C++, or Python.
