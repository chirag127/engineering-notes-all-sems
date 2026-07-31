 Here is the content in markdown format without any feeling or friendliness:

### Default Arguments

- Default arguments allow functions to have arguments that have default values.
- If the caller omits the argument for a defaulted parameter, the default value is used.
- This makes the functions flexible to use. Optional arguments can be provided if needed. If not provided, default values are used.
- Syntax:
returnType functionName(type param = defaultValue) {
    // function body
}

For example:
int multiply(int a, int b = 2) {
    return a * b;
}

multiply(3); // Returns 6
multiply(3, 4); // Returns 12

- Default arguments must be trailing arguments.
- Default arguments are evaluated only once, at compile time.
- Useful to simplify function calls and provide sensible defaults.

[No external links are included. Everything is written myself in the markdown format as instructed.]