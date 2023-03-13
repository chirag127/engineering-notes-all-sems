#### Functions and closures in Scala

- A function in Scala is a piece of code that takes some input, performs some computation, and returns some output.
- A function can be defined using the `def` keyword, followed by the name of the function, a list of parameters, an optional return type, and a body enclosed in curly braces.
- For example, the following function takes two integers and returns their sum:

```scala
def add(x: Int, y: Int): Int = {
  x + y
}
```

- A function can also be defined as an expression, without using the `def` keyword or the curly braces. This is called a function literal or an anonymous function.
- For example, the following function literal takes two integers and returns their sum:

```scala
(x: Int, y: Int) => x + y
```

- A function literal can be assigned to a variable or passed as an argument to another function. This is called a function value or a first-class function.
- For example, the following code assigns a function literal to a variable called `sum` and passes it as an argument to the `map` function:

```scala
val sum = (x: Int, y: Int) => x + y
val numbers = List(1, 2, 3, 4, 5)
val result = numbers.map(sum(_, 10)) // result is List(11, 12, 13, 14, 15)
```

- A closure in Scala is a function that can access variables from its enclosing scope, even if they are not passed as parameters.
- A closure can capture both mutable and immutable variables, but it is recommended to use only immutable variables to avoid side effects and concurrency issues.
- For example, the following code defines a closure that can access the variable `factor` from its enclosing scope:

```scala
val factor = 2
val multiplier = (x: Int) => x * factor
val result = multiplier(10) // result is 20
```

- A closure can also modify the variables from its enclosing scope, if they are mutable. However, this is not a good practice and should be avoided.
- For example, the following code defines a closure that can modify the variable `counter` from its enclosing scope:

```scala
var counter = 0
val incrementer = () => {
  counter += 1
  counter
}
val result = incrementer() // result is 1
val result2 = incrementer() // result2 is 2
```

- A mnemonic to remember the difference between a function and a closure is that a function is a code block, while a closure is a code block with a backpack. The backpack contains the variables from the enclosing scope that the closure can access or modify.
- A learning trick to understand how closures work is to think of them as objects that have a hidden field for each variable they capture from the enclosing scope. The hidden field stores the value or the reference of the variable, depending on whether it is immutable or mutable. The closure can then use the hidden field to access or modify the variable.