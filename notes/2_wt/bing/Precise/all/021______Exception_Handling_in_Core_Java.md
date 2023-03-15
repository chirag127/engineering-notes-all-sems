#### Exception Handling in Core Java

Exception handling is a mechanism in Java to handle runtime errors and exceptional conditions that may occur during the execution of a program. It provides a way to handle these errors and exceptions gracefully, without abruptly terminating the program.

- **Try-Catch-Finally Block:** The basic mechanism for handling exceptions in Java is the try-catch-finally block. The code that may throw an exception is placed inside the try block. If an exception is thrown, it is caught by the catch block, where the appropriate action can be taken. The finally block is optional and contains code that is always executed, whether an exception is thrown or not.

- **Types of Exceptions:** There are two types of exceptions in Java: checked and unchecked exceptions. Checked exceptions are exceptions that are checked by the compiler at compile-time. These exceptions must be explicitly handled in the code, either by using a try-catch block or by declaring the exception in the method signature using the throws keyword. Unchecked exceptions, on the other hand, are not checked by the compiler and do not need to be explicitly handled in the code.

- **Throwing Exceptions:** Exceptions can be thrown explicitly in the code using the throw keyword. This is useful when you want to signal an exceptional condition in your code and pass control to the exception handling mechanism.

- **Creating Custom Exceptions:** You can create your own custom exceptions by extending the Exception class or one of its subclasses. This is useful when you want to create exceptions that are specific to your application.

- **Advantages of Exception Handling:** Exception handling provides several advantages, including improved readability and maintainability of the code, the ability to handle errors and exceptional conditions gracefully, and the ability to recover from errors and continue the execution of the program.

- **Disadvantages of Exception Handling:** Exception handling can also have some disadvantages, including increased complexity of the code and the potential for performance overhead.

Here is an example of a simple try-catch block in Java:

```java
try {
    // code that may throw an exception
    int result = 10 / 0;
} catch (ArithmeticException e) {
    // handle the exception
    System.out.println("An error occurred: " + e.getMessage());
}
```

In this example, the code inside the try block may throw an `ArithmeticException` if the denominator is zero. This exception is caught by the catch block, where the appropriate action is taken.

A mnemonic to remember the order of the try-catch-finally block is **T-C-F** (Try-Catch-Finally). Another mnemonic to remember the difference between checked and unchecked exceptions is **C-U** (Checked-Unchecked).