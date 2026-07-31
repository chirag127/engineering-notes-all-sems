# Functions and Closures in Scala

- Functions are reusable blocks of code that take some inputs and produce some outputs.
- Functions can be defined using the `def` keyword, followed by the function name, parameters, return type, and body.
- For example, `def add(x: Int, y: Int): Int = x + y` defines a function named `add` that takes two integers as parameters and returns their sum as an integer.
- Functions can also be defined as anonymous functions, or function literals, using the `=>` syntax.
- For example, `(x: Int, y: Int) => x + y` is an anonymous function that takes two integers as parameters and returns their sum as an integer.
- Anonymous functions can be assigned to variables or passed as arguments to other functions.
- For example, `val add = (x: Int, y: Int) => x + y` assigns the anonymous function to a variable named `add`.
- Closures are functions that use one or more free variables, which are variables that are not defined as parameters or inside the function body.
- The return value of a closure depends on the value of the free variables, which are defined outside the closure function.
- For example, `val multiplier = (i: Int) => i * factor` is a closure that uses a free variable named `factor`, which is defined outside the closure function.
- Closures can access and modify the free variables, even if they are declared as `val`.
- For example, `var factor = 3; val multiplier = (i: Int) => i * factor; factor = 10; multiplier(5)` will return `50`, because the closure modifies the value of `factor`.
- Closures are useful for creating higher-order functions, which are functions that take other functions as parameters or return other functions as results.
- For example, `def apply(f: Int => Int, x: Int) = f(x)` is a higher-order function that takes a function `f` and an integer `x` as parameters and returns the result of applying `f` to `x`.
- Closures can be passed as arguments to higher-order functions, or returned as results from higher-order functions.
- For example, `def makeMultiplier(factor: Int) = (i: Int) => i * factor` is a higher-order function that takes an integer `factor` as a parameter and returns a closure that multiplies its input by `factor`.