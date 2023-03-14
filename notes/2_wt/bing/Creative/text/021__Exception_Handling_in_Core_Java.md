#### Exception Handling in Core Java

- An exception is an abnormal or unexpected event that occurs during the execution of a program and disrupts its normal flow.
- Exception handling is a mechanism that allows a program to deal with exceptions gracefully and prevent the program from terminating abruptly.
- Exception handling in core Java involves four keywords: `try`, `catch`, `finally`, and `throw`.
- The `try` block contains the code that may cause an exception. The `catch` block contains the code that handles the specific exception that occurs in the `try` block. The `finally` block contains the code that is always executed regardless of whether an exception occurs or not. The `throw` keyword is used to explicitly throw an exception from a method or a block.
- There are two types of exceptions in Java: checked and unchecked. Checked exceptions are those that are checked by the compiler at compile-time and must be handled or declared by the programmer. Unchecked exceptions are those that are not checked by the compiler and are usually caused by logical errors or runtime conditions. Examples of checked exceptions are `IOException`, `SQLException`, `ClassNotFoundException`, etc. Examples of unchecked exceptions are `NullPointerException`, `ArithmeticException`, `ArrayIndexOutOfBoundsException`, etc.
- Java provides a hierarchy of exception classes that are derived from the `Throwable` class. The `Throwable` class has two direct subclasses: `Exception` and `Error`. The `Exception` class represents the exceptions that can be handled by the program. The `Error` class represents the errors that are beyond the control of the program and usually indicate serious problems with the system or the virtual machine. Examples of errors are `OutOfMemoryError`, `StackOverflowError`, `VirtualMachineError`, etc.
- To handle multiple exceptions in a single `catch` block, Java 7 introduced the feature of multi-catch, which allows specifying more than one exception type in a single `catch` clause separated by a vertical bar (`|`). For example:

```java
try {
  // some code that may cause exceptions
} catch (IOException | SQLException | ClassNotFoundException e) {
  // handle the exceptions
}
```

- To rethrow an exception with more specific information, Java 7 introduced the feature of precise rethrow, which allows rethrowing the same exception object that was caught without losing its type information. For example:

```java
try {
  // some code that may cause exceptions
} catch (Exception e) {
  // do some processing
  throw e; // rethrow the same exception object
}
```

- To suppress the exceptions that are thrown from the `finally` block, Java 7 introduced the feature of suppressed exceptions, which are added to the list of suppressed exceptions of the primary exception that was thrown from the `try` block. The suppressed exceptions can be accessed using the `getSuppressed()` method of the `Throwable` class. For example:

```java
try {
  // some code that may cause an exception
} catch (Exception e) {
  // handle the exception
} finally {
  try {
    // some code that may cause another exception
  } catch (Exception e) {
    // this exception is suppressed and added to the list of suppressed exceptions of the primary exception
  }
}
```