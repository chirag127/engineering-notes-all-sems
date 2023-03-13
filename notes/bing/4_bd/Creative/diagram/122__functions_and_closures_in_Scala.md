A function is a piece of code that takes some input and produces some output. A closure is a special kind of function that can access variables that are defined outside of its scope. For example, in Scala, we can define a function that adds a constant value to its argument:

```scala
def addConstant(x: Int) = x + 10
```

This function is not a closure, because it does not use any free variables. A free variable is a variable that is not defined in the function or passed as a parameter. Now, suppose we want to make the constant value configurable. We can use a closure to achieve this:

```scala
val constant = 10 // a free variable
val addConstant = (x: Int) => x + constant // a closure
```

This function is a closure, because it uses the variable `constant` that is defined outside of its scope. The closure captures the value of `constant` and uses it in its body. The value of the closure depends on the value of the free variable.

#### Functions and closures in Scala

The following diagram illustrates the basic architecture of a function and a closure in Scala:

```
+-----------------+     +-----------------+
| Function        |     | Closure         |
|                 |     |                 |
| +-------------+ |     | +-------------+ |
| | Parameters  | |     | | Parameters  | |
| +-------------+ |     | +-------------+ |
|                 |     |                 |
| +-------------+ |     | +-------------+ |
| | Body        | |     | | Body        | |
| +-------------+ |     | +-------------+ |
|                 |     |                 |
| +-------------+ |     | +-------------+ |
| | Return value| |     | | Return value| |
| +-------------+ |     | +-------------+ |
+-----------------+     +-----------------+
                        |                 |
                        | +-------------+ |
                        | | Free        | |
                        | | variables   | |
                        | +-------------+ |
                        +-----------------+
```

A function has parameters, a body, and a return value. A closure has the same components, but also has access to free variables that are defined outside of its scope. The closure can read and write the free variables, and the value of the closure may change if the free variables change.