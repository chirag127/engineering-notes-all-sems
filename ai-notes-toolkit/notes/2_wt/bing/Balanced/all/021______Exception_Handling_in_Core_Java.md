#### Exception Handling in Core Java

- Exception handling in Java is a mechanism to handle and deal with the runtime errors so that the normal flow of the program can be maintained .
- An exception is an abnormal condition that arises in a code sequence at runtime or at compile time. It can be caused by various reasons, such as invalid input, file not found, network failure, etc.
- Java provides a way to handle exceptions using the following keywords: `try`, `catch`, `finally`, `throw`, and `throws` .
- The basic syntax of exception handling in Java is:

```java
try {
  // code that may throw an exception
} catch (ExceptionType e) {
  // code to handle the exception
} finally {
  // code to execute always, regardless of exception
}
```

- The `try` block contains the code that may throw an exception. If an exception occurs, the control is transferred to the `catch` block that matches the type of the exception. The `catch` block contains the code to handle the exception. The `finally` block contains the code that always executes, regardless of whether an exception occurs or not. The `finally` block is optional and can be used to release resources or perform cleanup tasks .
- The `throw` keyword is used to explicitly throw an exception from a method or a block of code. The `throws` keyword is used to declare that a method may throw one or more exceptions. The `throws` keyword is required for checked exceptions, which are exceptions that must be handled or declared by the method .
- The syntax of using `throw` and `throws` keywords is:

```java
void method() throws ExceptionType {
  // code that may throw an exception
  if (condition) {
    throw new ExceptionType("message");
  }
}
```

- Java exceptions are classified into two types: checked and unchecked exceptions. Checked exceptions are exceptions that are checked by the compiler at compile time and must be handled or declared by the method. Unchecked exceptions are exceptions that are not checked by the compiler and are usually caused by logic errors or bugs in the code .
- Some examples of checked exceptions are: `IOException`, `FileNotFoundException`, `ClassNotFoundException`, etc. Some examples of unchecked exceptions are: `ArithmeticException`, `NullPointerException`, `ArrayIndexOutOfBoundsException`, etc.
- A mnemonic to remember the difference between checked and unchecked exceptions is: **C**hecked exceptions are **C**ompiled, **U**nchecked exceptions are **U**nexpected.
- A good practice for exception handling in Java is to use specific exception types rather than the generic `Exception` class, to provide meaningful messages when throwing or catching exceptions, to use multiple `catch` blocks to handle different types of exceptions, and to avoid catching or throwing `Throwable` or `Error` classes, which are reserved for serious system errors.