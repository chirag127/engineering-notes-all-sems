 Here is the content in markdown format on the topic #### functions and closures in Scala:

#### Functions and Closures in Scala

Functions in Scala are first-class citizens, which means that functions can be passed as parameters to other functions, returned as values from functions, and assigned to variables.

- Functions can be defined using the `def` keyword followed by the function name, parameters (if any), return type (if specified), and function body enclosed in curly braces.
- For example:
```scala
def square(x: Int): Int = {
  x * x
}
```
- Functions can be assigned to variables and passed as arguments to other functions. For example:
```scala
val funcVariable = square _   // assigning function to variable
funcVariable(5)  // calling variable which refers to function

List(1, 2, 3).map(square)   // passing function as parameter
```

Closures are functions that refer to independent (non-local) variables. In Scala, closures are created every time you refer to a non-local variable.
For example:
```scala
def makeAdder(a: Int) = {
  def add(b: Int) = a + b
  add
}

val add5 = makeAdder(5) // creates a closure
add5(2)  // returns 7
```
The `add` function here is a closure. It refers to the variable `a` which is defined outside its body.

Advantages:
- Removes repetition and makes the code DRY (Don't Repeat Yourself)
- Increases reusability
- Used in functional programming patterns

Disadvantages:
- Can make the code hard to read and understand
- Risk of unintended side effects if not used properly

Applications:
- Map, reduce, filter functions
- Currying
- Partial applications
- Lazy evaluations
- Recursion

Hope this helps! Let me know if you would like me to elaborate on any of the points or add more details.