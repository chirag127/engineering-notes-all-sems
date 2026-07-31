### Control Structures
Control structures are statements that determine the flow of execution of a program. They can be classified into three types: sequential, selection and iteration.

- Sequential control structures are the simplest ones. They execute statements one after another in the order they appear in the program. For example:

```cpp
// A sequential control structure
int x = 10; // Assign 10 to x
int y = 20; // Assign 20 to y
int z = x + y; // Add x and y and assign the result to z
cout << z << endl; // Print z to the standard output
```

- Selection control structures allow the program to choose between two or more alternative paths based on some condition. They can be implemented using `if`, `if-else`, `switch` or `?:` operators. For example:

```cpp
// A selection control structure using if-else
int x = 10; // Assign 10 to x
if (x % 2 == 0) // Check if x is even
{
    cout << "x is even" << endl; // Print x is even
}
else // Otherwise
{
    cout << "x is odd" << endl; // Print x is odd
}
```

- Iteration control structures allow the program to repeat a block of statements until some condition is met. They can be implemented using `while`, `do-while`, `for` or `range-based for` loops. For example:

```cpp
// An iteration control structure using while
int x = 10; // Assign 10 to x
while (x > 0) // Repeat until x is zero or negative
{
    cout << x << endl; // Print x
    x--; // Decrement x by 1
}
```

Control structures can be nested, meaning that one control structure can be placed inside another. For example:

```cpp
// A nested control structure
for (int i = 1; i <= 5; i++) // Outer loop
{
    for (int j = 1; j <= i; j++) // Inner loop
    {
        cout << "*"; // Print a star
    }
    cout << endl; // Print a new line
}
// The output will be:
// *
// **
// ***
// ****
// *****
```