#### Exception Handling in Core Java

Exception handling is a mechanism in Java that allows the program to handle runtime errors and maintain the normal flow of the program. It is achieved using the `try`, `catch`, `finally`, and `throw` keywords.

1. **try**: The `try` block contains the code that might throw an exception. If an exception occurs, the code inside the `try` block is skipped and the control is transferred to the `catch` block.

2. **catch**: The `catch` block is used to handle the exception thrown by the `try` block. It must be placed immediately after the `try` block. The `catch` block takes an exception object as a parameter and contains the code to handle the exception.

3. **finally**: The `finally` block is used to execute code that must be executed regardless of whether an exception is thrown or not. It is placed after the `try` and `catch` blocks and is always executed.

4. **throw**: The `throw` keyword is used to throw an exception manually. It is used inside a method to indicate that an exceptional condition has occurred and the method cannot handle it.

Java provides several built-in exception classes, such as `ArithmeticException`, `NullPointerException`, `ArrayIndexOutOfBoundsException`, etc. These classes are subclasses of the `Throwable` class, which is the superclass of all exception classes in Java.

It is also possible to create custom exception classes by extending the `Exception` class or one of its subclasses. This allows the programmer to create more specific exception types that can be handled in a more fine-grained manner.

In summary, exception handling in Java allows the programmer to handle runtime errors in a controlled manner and maintain the normal flow of the program. It is achieved using the `try`, `catch`, `finally`, and `throw` keywords and can be customized by creating custom exception classes.