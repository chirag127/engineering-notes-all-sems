#### Built-in control structures in Scala

- Scala has only a handful of built-in control structures: **if, while, for, try, match, and function calls**  .
- The reason Scala has so few is that it has included **function literals** since its inception .
- A function literal is a function that is not defined by a name, but by its parameters and body, such as `(a:Int, b:Int) => a + b`.
- Function literals can be assigned to variables, passed as arguments, or returned as results.
- Scala also has some unique constructs, such as **match expressions** and **for expressions** .
- A match expression is a powerful way to pattern match on values, types, or conditions, such as `x match { case 1 => "one"; case 2 => "two"; case _ => "other" }`.
- A for expression is a concise way to iterate over collections, filter elements, or generate new collections, such as `for (i <- 1 to 10 if i % 2 == 0) yield i * i`.
- Scala's control structures are closer to the functional style, meaning they are expressions that return values, rather than statements that perform side effects .
- This makes Scala code more concise, readable, and expressive .