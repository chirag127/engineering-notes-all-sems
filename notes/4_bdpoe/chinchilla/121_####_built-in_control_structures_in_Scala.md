#### Built-in control structures in Scala

Scala is a modern programming language that provides a wide range of built-in control structures to help you handle the flow of your program. Control structures are used to control the execution of the program and determine which code should be executed and when. In this section, we will discuss the built-in control structures in Scala.

1. If-else statement:

The if-else statement is used to execute a block of code if a certain condition is true. If the condition is false, then another block of code can be executed. The syntax is as follows:

```
if (condition) {
  // code to be executed if condition is true
} else {
  // code to be executed if condition is false
}
```

Mnemonic: IF you meet the condition THEN execute the first block of code ELSE execute the second block of code.

2. For loop:

The for loop is used to execute a block of code repeatedly for a fixed number of times. It can be used with a range or with a collection. The syntax is as follows:

```
for (i <- 1 to 10) {
  // code to be executed for each iteration
}
```

Mnemonic: FOR each item in the collection/ range DO execute the block of code.

3. While loop:

The while loop is used to execute a block of code repeatedly as long as a certain condition is true. The syntax is as follows:

```
while (condition) {
  // code to be executed while condition is true
}
```

Mnemonic: WHILE the condition is true, DO execute the block of code.

4. Do-while loop:

The do-while loop is similar to the while loop, but it executes the block of code first and then checks the condition. The syntax is as follows:

```
do {
  // code to be executed at least once
} while (condition)
```

Mnemonic: DO execute the block of code first, THEN check the condition.

5. Match expression:

The match expression is used to match a value against a set of patterns and execute the corresponding block of code. The syntax is as follows:

```
val x = 5
x match {
  case 1 => println("One")
  case 2 => println("Two")
  case _ => println("Other")
}
```

Mnemonic: MATCH the value against the patterns and execute the corresponding block of code.

6. Try-catch expression:

The try-catch expression is used to handle exceptions that may occur in the program. The try block contains the code that may throw an exception, and the catch block contains the code that should be executed if an exception is thrown. The syntax is as follows:

```
try {
  // code that may throw an exception
} catch {
  case e: Exception => println(e)
}
```

Mnemonic: TRY to execute the code, and if an exception is thrown, CATCH it and execute the corresponding block of code.

In conclusion, the built-in control structures in Scala are powerful tools for controlling the flow of your program. By understanding these control structures and their syntax, you can write more efficient and effective programs.