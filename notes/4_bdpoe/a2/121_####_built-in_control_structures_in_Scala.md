 Here is the content in markdown format on the topic #### built-in control structures in Scala:

#### Built-in control structures in Scala

Scala provides the following built-in control structures:

1. **Conditionals**- Scala has `if`/`else` expressions which evaluate a boolean expression and execute code based on whether it is `true` or `false`.
For e.g.-
```scala
if (x > 0) {
  println("x is positive")
} else {
  println("x is non-positive")
}
```

*Mnemonic*- Think of `if` as 'If this, then that'.

2. **Loops**- Scala has `for` loops, `while` loops and `do while` loops to repeat a block of code.
For e.g.-
```scala
for (i <- 1 to 10) {
  println(i) //prints 1 to 10
}

var i = 0
while (i < 10) {
  println(i)
  i += 1
} //prints 0 to 9

do {
  println(i)
  i += 1
} while (i < 10) //prints 0 to 9
```

*Mnemonic*- Think of loops as iterating over a block of code multiple times.

3. **Exceptions**- Scala has `try`/`catch`/`finally` expressions to handle errors/exceptions.
For e.g.-
```scala
try {
  //code that may throw an exception
} catch {
  case e: ArithmeticException => //handle ArithmeticException
  case e: IOException => //handle IOException
} finally {
  //cleanup code
}
```

*Advantages*- Allows graceful handling of errors and ensures important cleanup code is executed.

I have included some simple examples and mnemonics/learning tricks for the built-in control structures in Scala. Please let me know if you would like me to elaborate on any of the points or include additional details/examples.