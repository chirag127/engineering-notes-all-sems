 Here are the notes on Functions and Closures for Unit 10 - Scala in Big Data:

### Functions

- A function is a block of code that performs a specific task.
- In Scala, functions are first-class citizens, which means they can be passed as arguments to other functions, returned as values from functions, and assigned to variables.
- The basic structure of a Scala function is:

<return_type> <function_name>(<parameters>): <body>

- The return type is optional and if not specified, the function will return a Unit type (similar to void in Java/C++).
- Parameters can have default values and can be specified with val or var.
- The body contains the function logic/implementation.
- Example:
 def greet(name: String): String = "Hello " + name

- Functions can be recursive, take other functions as arguments, return functions, etc.
- Anonymous functions can be defined inline using =>. For ex: (x: Int) => x + 1
- Advantages: Reusability, Abstraction, Modularization

### Closures

- A closure is a function that retains the references to the variables of its surrounding scope even when it is executed elsewhere.
- This allows the function to access those variables even when the scope in which they were defined no longer exists.
- Example:
val factor = 10
def multiplyByFactor(x: Int) = x * factor

- Here, multiplyByFactor is a closure that retains the reference to the factor variable.
- Closures are useful to create callbacks, handle asynchronous tasks, create enumerator objects, etc.
- The variables captured in a closure must be declared as val or var (and not defined using let) else it will lead to errors.