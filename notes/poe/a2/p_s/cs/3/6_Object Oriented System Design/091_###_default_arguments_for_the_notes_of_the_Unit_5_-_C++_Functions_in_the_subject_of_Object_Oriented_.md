 Here is the content in markdown format for the topic ### default arguments for the notes of the Unit 5 - C++ Functions in the subject of Object Oriented System Design:

### Default Arguments

- Default arguments allow named arguments to have default values in case no value or value of wrong type is passed during function calls.
- This makes the functions more flexible to use. They can be called with fewer arguments, and the default values will be used for the missing arguments.
- The default values are specified after the parameter name in the function declaration, in the form:

`return_type function_name(type param = default_value)`

- For example:

`int multiply(int a, int b = 10);`

- Here, `b` has the default value of `10`. So, `multiply(5)` and `multiply(5, 20)` are both valid calls.
- In the first call, `b` will have the default value of `10`, in the second call, `b` will have the value `20` passed as argument.
- Default arguments must be declared from right to left. This is because the default is only used when the argument is omitted, and arguments are matched from left to right.
- For example, the following would be incorrect:

`int divide(int b = 10, int a); // Wrong order!`

- Advantages:
  - Makes functions more flexible to use.
  - Reduces the number of overloads required.
- Disadvantages:
  - The default values are evaluated every time the function is called, even if the corresponding arguments are passed. This can impact performance for complex default values.
  - The default values are fixed and cannot vary based on the context of the function call.