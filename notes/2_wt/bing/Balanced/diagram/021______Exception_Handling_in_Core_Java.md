Exception handling in core Java is a mechanism to handle and deal with the runtime errors so that the normal flow of the application can be maintained . An exception is an abnormal condition that arises in a code sequence at runtime or at compile time. Exceptions can be classified into two types: checked and unchecked. Checked exceptions are those that are checked by the compiler at compile time and must be handled or declared by the programmer. Unchecked exceptions are those that are not checked by the compiler and are thrown at runtime.

To handle exceptions in core Java, we can use the following constructs:

- **throws**: This is a keyword that is used to declare that a method may throw one or more exceptions. It is written after the method signature and before the method body. For example:

```java
public void readFile(String fileName) throws FileNotFoundException {
  // method body
}
```

- **try-catch**: This is a block of code that tries to execute a statement that may throw an exception and catches the exception if it occurs. The try block contains the risky code and the catch block contains the code to handle the exception. There can be multiple catch blocks for different types of exceptions. For example:

```java
try {
  // risky code
} catch (FileNotFoundException e) {
  // handle FileNotFoundException
} catch (IOException e) {
  // handle IOException
}
```

- **finally**: This is a block of code that is always executed after the try-catch block, regardless of whether an exception occurs or not. It is used to perform some cleanup or finalization tasks. For example:

```java
try {
  // risky code
} catch (Exception e) {
  // handle Exception
} finally {
  // cleanup code
}
```

- **throw**: This is a keyword that is used to manually throw an exception from a method or a block of code. It is followed by an instance of an exception class. For example:

```java
public void divide(int a, int b) {
  if (b == 0) {
    throw new ArithmeticException("Cannot divide by zero");
  }
  // rest of the code
}
```

A detailed ASCII diagram for exception handling in core Java is shown below:

#### Exception Handling in Core Java

```
+---------------------+      +---------------------+
|     try block       |      |     catch block     |
|                     |      |                     |
|  +--------------+   |      |  +--------------+   |
|  | risky code   |   |      |  | handle       |   |
|  | that may     |   |      |  | exception    |   |
|  | throw an     |   |      |  | of type E    |   |
|  | exception    |   |      |  +--------------+   |
|  +--------------+   |      |                     |
|                     |      |                     |
+---------------------+      +---------------------+
          |                            |
          |                            |
          |                            |
          |                            |
          |                            |
          |                            |
          |                            |
          |                            |
          |                            |
          |                            |
          |                            |
          |                            |
          |                            |
          |                            |
          |                            |
          |                            |
          +----------------------------+
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |
                       |

```
