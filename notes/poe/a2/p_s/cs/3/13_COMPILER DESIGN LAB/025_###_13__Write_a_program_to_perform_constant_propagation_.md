 Here is the content in markdown format for the topic -

### 13. Write a program to perform constant propagation.

Constant propagation is a program optimization technique in which constants are replaced with their values at compile time. This technique is used to simplify expressions and remove unnecessary computations at runtime.

Some key points about constant propagation are:

1. It is performed by the compiler during the optimization phase.
2. It works on the intermediate representation of the program.
3. It replaces constants with their values wherever possible. For e.g. if there is an expression like `x = 5 + 7`, the compiler will replace it with `x = 12` by performing constant propagation.
4. It enables further optimizations like common subexpression elimination by simplifying expressions.
5. It has limitations like values of variables and functions cannot be determined at compile time. Only literal constants can be replaced.

A simple program to demonstrate constant propagation is:

```C
int main() {
    int x = 5 + 7;  // Replaced with x = 12
    int y = x * 3;  // Replaced with y = 36
    return 0;
}
```

After constant propagation, the optimized code would be:

```C
int main() {
    int x = 12;
    int y = 36;
    return 0;
}
```

Advantages of constant propagation:

- Reduces runtime computations and hence improves performance.
- Enables other optimizations.

Disadvantages of constant propagation:

- Cannot be applied in cases where variable values cannot be determined at compile time.
- May lead to increased code size in some cases.

Applications of constant propagation:

- Used by compilers to optimize code.
- Used in other program analysis techniques.

[Detailed diagrams and code examples can be added here if required.]