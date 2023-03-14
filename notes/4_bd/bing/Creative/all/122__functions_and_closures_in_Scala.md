#### Functions and closures in Scala

- A function in Scala is a piece of code that takes some input, performs some computation, and returns some output.
- A function can be defined using the `def` keyword, followed by the name of the function, the parameters, the return type, and the body of the function.
- A function can also be defined as a value, using the `val` keyword, followed by the name of the function, the parameters, and the body of the function. This is called a function literal or an anonymous function.
- A function can be passed as an argument to another function, or returned as a result from another function. This is called a higher-order function.
- A closure in Scala is a special type of function that uses one or more free variables and the return value of the function is dependent on these variables.
- A free variable is a variable that is not defined within the function and not passed as a parameter of the function. A free variable is not bound to a function with a valid value.
- A closure captures the most recent state of the free variables and changes the value of the function accordingly.
- A closure can be pure or impure, depending on the type of the free variables. If the free variables are immutable (`val`), then the closure is pure and the value of the function does not change. If the free variables are mutable (`var`), then the closure is impure and the value of the function can change.

Example of a function:

```scala
// a function that calculates the area of a circle
def area(radius: Double): Double = {
  val pi = 3.14 // a local variable
  pi * radius * radius // the return value
}

// calling the function
area(5) // 78.5
```

Example of a function literal:

```scala
// a function literal that calculates the area of a circle
val area = (radius: Double) => {
  val pi = 3.14 // a local variable
  pi * radius * radius // the return value
}

// calling the function literal
area(5) // 78.5
```

Example of a higher-order function:

```scala
// a function that takes another function as a parameter and applies it to a list of numbers
def map(f: Int => Int, list: List[Int]): List[Int] = {
  list match {
    case Nil => Nil // base case
    case head :: tail => f(head) :: map(f, tail) // recursive case
  }
}

// a function that doubles a number
def double(x: Int): Int = x * 2

// calling the higher-order function
map(double, List(1, 2, 3, 4)) // List(2, 4, 6, 8)
```

Example of a pure closure:

```scala
// a free variable
val pi = 3.14

// a closure that calculates the area of a circle
val area = (radius: Double) => pi * radius * radius

// calling the closure
area(5) // 78.5

// changing the value of the free variable
val pi = 3.14159

// calling the closure again
area(5) // 78.53975
```

Example of an impure closure:

```scala
// a free variable
var pi = 3.14

// a closure that calculates the area of a circle
val area = (radius: Double) => pi * radius * radius

// calling the closure
area(5) // 78.5

// changing the value of the free variable
pi = 3.14159

// calling the closure again
area(5) // 78.53975
```

Mnemonics and learning tricks:

- A function is like a recipe that tells you how to make something.
- A function literal is like a recipe that you write on a piece of paper and pass around.
- A higher-order function is like a cookbook that contains recipes that use other recipes as ingredients.
- A closure is like a recipe that uses ingredients that are not in the recipe, but in the kitchen.
- A pure closure is like a recipe that uses ingredients that are always the same, no matter when or where you make it.
- An impure closure is like a recipe that uses ingredients that can change, depending on when or where you make it.