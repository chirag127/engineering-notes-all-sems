A closure in Scala is a function that can refer to variables that are defined outside the function's scope. The function can capture or "close over" those variables and use them in its body. For example, consider the following function:

```scala
def adder(x: Int) = (y: Int) => x + y
```

This function takes an integer x as a parameter and returns another function that takes an integer y as a parameter and returns the sum of x and y. The inner function is a closure because it can access the variable x that is defined in the outer function's scope. The value of x is bound to the closure when the outer function is called. For example:

```scala
val addOne = adder(1) // addOne is a closure that can add 1 to any integer
val addTwo = adder(2) // addTwo is a closure that can add 2 to any integer
addOne(3) // returns 4
addTwo(3) // returns 5
```

The following diagram illustrates the basic structure of a closure in Scala:

```
+-----------------+     +-----------------+
| Outer function  |     | Closure         |
|                 |     |                 |
| +-------------+ |     | +-------------+ |
| | Parameter x | |     | | Parameter y | |
| +-------------+ |     | +-------------+ |
|                 |     |                 |
| +-------------+ |     | +-------------+ |
| | Return      | |---->| | Return      | |
| | (y: Int) => | |     | | x + y       | |
| | x + y       | |     | +-------------+ |
| +-------------+ |     |                 |
+-----------------+     +-----------------+
```

The closure can be seen as a function object that has a reference to the variable x from the outer function's scope. The closure can be passed around as a value and invoked with different values of y. The closure will always use the same value of x that was bound to it when the outer function was called.