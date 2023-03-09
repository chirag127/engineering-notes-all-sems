### 13. Write a program to perform constant propagation.

Constant propagation is a technique used in compilers to optimize code by replacing variables that have a constant value with the actual value of the constant. This technique helps reduce the number of computations that need to be performed, resulting in faster code execution. Here we will discuss how to write a program to perform constant propagation.

#### Steps to perform constant propagation:
1. Parse the input program to identify the variables and their values.
2. For each variable that has a constant value, replace all occurrences of the variable with the constant value.
3. Repeat step 2 for all variables that have a constant value until no more replacements can be made.
4. Output the optimized program.

#### Example:
Consider the following input program:

```
x = 5
y = 6
z = x + y
print(z)
```

After performing constant propagation, the optimized program would be:

```
print(11)
```

#### Advantages of constant propagation:
- Reduces the number of computations that need to be performed.
- Improves code performance and execution speed.
- Makes the code easier to read and understand.

#### Disadvantages of constant propagation:
- May require additional processing time to identify and replace constant variables.
- May produce incorrect results if the value of a variable changes during program execution.

#### Applications of constant propagation:
- Used in compilers to optimize code.
- Used in software engineering to improve program performance.
- Used in embedded systems to reduce memory usage.

In conclusion, constant propagation is an important technique used in compilers and software engineering to optimize code and improve program performance. By understanding how to write a program to perform constant propagation, you can improve your programming skills and create more efficient code.