#### Functions and Closures in Scala

- In Scala, functions are first-class values, meaning they can be assigned to variables, passed as arguments to other functions, and returned as values from other functions.
- A function literal is an expression that defines an anonymous function. It is written using the `=>` symbol, with the parameters on the left and the function body on the right.
- A closure is a function that references variables from its enclosing scope. The function and the referenced variables together form a closure.
- Closures allow you to create functions that have behavior that depends on data that is not passed as a parameter.
- In Scala, closures are automatically created when a function literal references a variable from its enclosing scope.
- Closures are useful for creating functions that need to maintain state between invocations, such as in functional programming patterns like currying and partial application.
- Scala also provides support for higher-order functions, which are functions that take other functions as arguments or return them as results. Higher-order functions are commonly used in functional programming to create more modular and reusable code.
