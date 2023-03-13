

#### Built-in Control Structures in Scala

* Scala is a powerful programming language that provides several built-in control structures. These include: 
  * `if` statements
  * `for` loops
  * `while` loops
  * `match` expressions
  * `try` / `catch` blocks

* `if` statements are used to execute a block of code only if a certain condition is met. The condition is evaluated as a boolean expression. The syntax for an `if` statement is as follows:

```
if (boolean expression) {
  // code to execute if boolean expression is true
}
```

* `for` loops are used to iterate over a sequence of values. The syntax for a `for` loop is as follows:

```
for (element <- sequence) {
  // code to execute for each element in the sequence
}
```

* `while` loops are used to execute a block of code while a certain condition is met. The condition is evaluated as a boolean expression. The syntax for a `while` loop is as follows:

```
while (boolean expression) {
  // code to execute while boolean expression is true
}
```

* `match` expressions are used to match a value against a set of patterns. The syntax for a `match` expression is as follows:

```
value match {
  case pattern1 => // code to execute if value matches pattern1
  case pattern2 => // code to execute if value matches pattern2
  ...
  case _ => // code to execute if value does not match any of the patterns
}
```

* `try` / `catch` blocks are used to handle exceptions that may be thrown while executing a block of code. The syntax for a `try` / `catch` block is as follows:

```
try {
  // code that may throw an exception
} catch {
  case exception1 => // code to execute if exception1 is thrown
  case exception2 => // code to execute if exception2 is thrown
  ...
  case _ => // code to execute if any other exception is thrown
}
```

* Mnemonics and learning tricks for these built-in control structures in Scala include: 
  * `if`: "If I am true, then do this"
  * `for`: "For each element in the sequence, do this"
  * `while`: "While I am true, do this"
  * `match`: "Match this value against these patterns"
  * `try` / `catch`: "Try this, and catch any exceptions that may be thrown"