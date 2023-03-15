#### Exception Handling in Core Java

- Exception handling in Java is a powerful mechanism to handle and deal with the runtime errors so that the normal flow of the application can be maintained .
- An exception is an abnormal condition that arises in a code sequence at runtime or at compile time. This abnormal condition occurs when a program violates the semantic constraints of the Java programming language.
- Exceptions that occur during the compile time are called checked exceptions. They are checked by the compiler and must be handled or declared in the code. For example, IOException, SQLException, etc.
- Exceptions that occur during the runtime are called unchecked exceptions. They are not checked by the compiler and are usually caused by logical errors or bugs in the code. For example, NullPointerException, ArithmeticException, etc.
- Java provides a try-catch-finally block to handle exceptions. The try block contains the code that may throw an exception. The catch block contains the code that handles the specific exception. The finally block contains the code that is always executed regardless of whether an exception occurs or not .
- The syntax of the try-catch-finally block is:

```java
try {
  // code that may throw an exception
} catch (ExceptionType e) {
  // code that handles the exception
} finally {
  // code that is always executed
}
```

- The catch block can have multiple clauses to handle different types of exceptions. The order of the catch clauses is important. The more specific exceptions should be caught first, followed by the more general ones .
- The syntax of the multiple catch block is:

```java
try {
  // code that may throw an exception
} catch (SpecificExceptionType1 e1) {
  // code that handles the specific exception type 1
} catch (SpecificExceptionType2 e2) {
  // code that handles the specific exception type 2
} catch (GeneralExceptionType e) {
  // code that handles the general exception type
} finally {
  // code that is always executed
}
```

- The throws keyword is used to declare that a method may throw an exception. The caller of the method must handle or declare the exception .
- The syntax of the throws keyword is:

```java
public void methodName() throws ExceptionType {
  // code that may throw an exception
}
```

- The throw keyword is used to explicitly throw an exception from a method or a block of code. The thrown exception must be an object of Throwable or its subclass .
- The syntax of the throw keyword is:

```java
throw new ExceptionType("message");
```

- A possible mnemonic to remember the difference between throw and throws is: throw is used to **t**hrow an exception, while throws is used to **t**ell that a method may throw an exception.
- Another possible mnemonic to remember the difference between checked and unchecked exceptions is: checked exceptions are **c**hecked by the **c**ompiler, while unchecked exceptions are **u**nchecked by the **u**ser.