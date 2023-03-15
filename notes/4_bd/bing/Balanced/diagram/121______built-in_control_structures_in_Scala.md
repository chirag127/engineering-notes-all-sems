#### Built-in control structures in Scala

- Scala has only a few built-in control structures, such as `if`, `while`, `for`, `try`, `match`, and function calls  .
- The reason Scala has so few is that it has included function literals since its inception . A function literal is a function that is not defined by a name, but by its parameters and body, such as `(a:Int, b:Int) => a + b`.
- Scala's control structures are closer to the functional style, which means they are expressions that return a value, rather than statements that perform side effects  .
- For example, the `if` control structure can be used as an expression that returns a value based on a condition, such as `val max = if (a > b) a else b`.
- Similarly, the `for` control structure can be used as an expression that returns a collection based on a generator and optional filters, such as `val evens = for (i <- 1 to 10 if i % 2 == 0) yield i`.
- The `try` control structure can be used as an expression that returns a value or throws an exception based on a block of code, such as `val result = try { someOperation() } catch { case e: Exception => handleError(e) }`.
- The `match` control structure can be used as an expression that returns a value based on a pattern matching, such as `val response = status match { case 200 => "OK" case 404 => "Not Found" case _ => "Error" }`.
- Function calls are also expressions that return a value based on the arguments and the function body, such as `val sum = add(1, 2)`.
- The only exception to the rule of expressions is the `while` control structure, which is a statement that performs a loop based on a condition and a block of code, such as `while (n > 0) { println(n); n -= 1 }`. However, the `while` loop is rarely used in Scala, as it is more idiomatic to use recursion or higher-order functions instead .