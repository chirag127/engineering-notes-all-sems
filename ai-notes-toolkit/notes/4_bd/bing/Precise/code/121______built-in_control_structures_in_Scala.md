#### Built-in Control Structures in Scala

Scala has several built-in control structures that allow you to control the flow of your program. These include:

1. **If-else statements**: These allow you to execute different code blocks depending on whether a condition is true or false.

```scala
if (x > 0) {
  println("x is positive")
} else {
  println("x is not positive")
}
```

2. **While loops**: These allow you to repeatedly execute a code block while a condition is true.

```scala
while (x > 0) {
  println(x)
  x -= 1
}
```

3. **For loops**: These allow you to iterate over a collection of elements.

```scala
for (x <- 1 to 10) {
  println(x)
}
```

4. **Match expressions**: These allow you to pattern match on values and execute different code blocks depending on the value.

```scala
x match {
  case 1 => println("x is 1")
  case 2 => println("x is 2")
  case _ => println("x is something else")
}
```

These are some of the built-in control structures in Scala that you can use to control the flow of your program. They are similar to control structures in other programming languages, but with some syntactic differences.