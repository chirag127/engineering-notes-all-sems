 Here is the content in markdown format on the topic #### built-in control structures in Scala:

#### Built-in Control Structures in Scala

Scala provides the following built-in control structures:

1. **If-else**: Scala has if-else expression which takes the form:
if (condition) expression1 else expression2
The expression1 is evaluated if the condition is true, otherwise expression2 is evaluated.
For example:
if (x > 0) "Positive" else "Non-positive"

2. **For loops**: Scala has for loops to iterate over anything that has an iterator. The basic form is:
for (elem <- iterable) expression
For example:
for (x <- 1 to 10) print(x)  // Prints 1 to 10

Mnemonic: Think of <- as "gets" to remember the syntax.

3. **While loops**: While loops repeatedly execute a block of code as long as a specified condition is true. The syntax is:
while (condition) expression
For example:
var i = 0
while (i < 5) {
  print(i)
  i += 1
}  // Prints 0 to 4

4. **Try/catch/finally**: Scala has try/catch/finally expressions to handle exceptions. The basic syntax is:
try expression1 catch {
    case ex: Exception1 => expression2
    case ex: Exception2 => expression3
    ...
} finally expression4
The try block is executed, if an exception is thrown, the appropriate catch block is executed, and finally block is always executed.
For example:
try {
  val x = io.Source.fromFile("file.txt").mkString
} catch {
  case ex: IOException => print("Error reading file: ")
} finally {
  io.Source.fromFile("file.txt").close()
}

The mnemonics and learning tricks for the built-in control structures in Scala are:

- Think of if-else as choosing between two options or paths.
- For loops are like repeated gets from an iterator.
- While loops are like repeating a block of code while a condition is true.
- Try/catch/finally is like attempting to do something, handling errors, and then always executing finally.

The advantages of Scala's built-in control structures are brevity, clarity, and flexibility. The main disadvantage is the syntax may seem unfamiliar or strange to programmers coming from other languages.

[Detailed examples and applications can be added here if required.]