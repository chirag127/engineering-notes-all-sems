#### Built-in control structures in Scala

- Scala has only a few built-in control structures, such as `if`, `while`, `for`, `try`, `match`, and function calls  .
- The reason Scala has so few is that it has included function literals since its inception . A function literal is a function that is not defined by a name, but by its parameters and body, such as `(a:Int, b:Int) => a + b`.
- Scala's control structures are closer to the functional style, which means they are expressions that return a value, rather than statements that perform side effects  .
- Some of the unique features of Scala's control structures are:
  - `if` expressions can be used as ternary operators, such as `val max = if (a > b) a else b` .
  - `for` loops can be used with ranges, collections, or generators, such as `for (i <- 1 to 10) println(i)` or `for (x <- xs if x % 2 == 0) yield x * 2` .
  - `match` expressions can be used for pattern matching, such as `x match { case 0 => "zero"; case 1 => "one"; case _ => "other" }` .
  - `try` expressions can be used for exception handling, such as `try { doSomething() } catch { case e: Exception => handle(e) } finally { cleanUp() }` .
- Scala's control structures are designed to be concise, expressive, and consistent  .