# Default Arguments

- Default arguments are arguments that have a predefined value in the function declaration.
- Default arguments are used when the function is called without passing some or all of the arguments.
- Default arguments can simplify the function call and avoid unnecessary repetition of values.
- Default arguments are specified by assigning a value to the parameter in the function declaration, after the parameter type and name.
- Example: `void printMessage(string message = "Hello, world!")`
- In this example, the parameter `message` has a default value of `"Hello, world!"`. If the function is called without passing an argument, such as `printMessage()`, the default value will be used. If the function is called with an argument, such as `printMessage("Goodbye!")`, the argument value will override the default value.
- Default arguments can be specified for any number of parameters, but they must be the rightmost parameters in the function declaration.
- Example: `void printDetails(string name, int age = 18, string city = "New York")`
- In this example, the parameters `age` and `city` have default values of `18` and `"New York"`, respectively. The function can be called with one, two, or three arguments, such as `printDetails("Alice")`, `printDetails("Bob", 21)`, or `printDetails("Charlie", 25, "London")`. However, the function cannot be called with zero arguments, or with only the `city` argument, such as `printDetails("Paris")`, because the `name` parameter does not have a default value and must be specified.
- Default arguments are evaluated at compile time, not at run time. This means that the default values must be constant expressions, not variables or expressions that depend on the function call.
- Example: `void printTime(int hour = getHour(), int minute = getMinute())`
- In this example, the parameters `hour` and `minute` have default values of `getHour()` and `getMinute()`, respectively. These are function calls that return the current hour and minute. However, this is not a valid way to specify default arguments, because the default values are not constant expressions and may change depending on when the function is called. The compiler will generate an error for this function declaration.