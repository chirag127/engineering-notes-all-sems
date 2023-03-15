### Built-in Control Structures

Scala has only a few built-in control structures, which are used to control the flow of execution in a program. The only control structures are:

- `if` / `else`: A conditional expression that evaluates a condition and executes one branch or another depending on whether the condition is true or false.
- `while` / `do-while`: A loop that repeatedly executes a block of code as long as a condition is true.
- `for`: A loop that iterates over a collection or a range of values, optionally with filters and generators.
- `try` / `catch` / `finally`: A block of code that handles exceptions that may occur during the execution of the `try` block, and optionally executes some cleanup code in the `finally` block.
- `match`: A pattern matching expression that compares a value with a series of cases and executes the corresponding block of code for the first matching case.
- Function calls: A way to invoke a function or a method with some arguments and get a result.

The reason Scala has so few built-in control structures is that it has included function literals since its inception. Function literals are anonymous functions that can be passed as arguments to other functions or stored in variables. They allow the creation of higher-order functions, which are functions that take other functions as parameters or return them as results. Higher-order functions can be used to implement many common control structures, such as `map`, `filter`, `reduce`, `foreach`, etc.