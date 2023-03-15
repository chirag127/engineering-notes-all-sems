### Built-in Control Structures

Scala has only a handful of built-in control structures. The only control structures are `if`, `while`, `for`, `try`, `match`, and function calls  . The reason Scala has so few is that it has included function literals since its inception.

- `if` is used for conditional branching. It can also be used as an expression that returns a value. For example:

```scala
val x = 10
val y = if (x > 0) 1 else -1 // y is 1
```

- `while` is used for looping until a condition is false. It is a statement that does not return a value. For example:

```scala
var i = 0
while (i < 10) {
  println(i)
  i += 1
}
```

- `for` is used for iterating over collections, ranges, or generators. It can also be used as an expression that returns a value. For example:

```scala
val s = "Hello"
for (c <- s) println(c) // prints each character of s
val v = for (i <- 1 to 10) yield i * i // v is Vector(1, 4, 9, ..., 100)
```

- `try` is used for handling exceptions. It can also be used as an expression that returns a value. For example:

```scala
import java.io.FileReader
import java.io.FileNotFoundException
import java.io.IOException

try {
  val f = new FileReader("input.txt")
  // use f
} catch {
  case ex: FileNotFoundException => println("File not found")
  case ex: IOException => println("IO error")
} finally {
  f.close()
}
```

- `match` is used for pattern matching. It can also be used as an expression that returns a value. For example:

```scala
val x = 10
val s = x match {
  case 0 => "zero"
  case 1 => "one"
  case _ => "many" // default case
} // s is "many"
```

- Function calls are used for invoking functions or methods. They can also be used as expressions that return values. For example:

```scala
def add(x: Int, y: Int) = x + y // define a function
val z = add(2, 3) // call the function and assign the result to z
println(z) // print z
```