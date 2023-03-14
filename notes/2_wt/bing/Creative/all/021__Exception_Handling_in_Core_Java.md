#### Exception Handling in Core Java

- Exception handling is a mechanism to handle runtime errors and maintain the normal flow of the application.
- An exception is an event that disrupts the normal flow of the program and is an object that is thrown at runtime.
- Exceptions can be classified into three types: checked, unchecked, and error.
- Checked exceptions are those that are checked by the compiler at compile-time and must be handled or declared by the programmer. For example, IOException, SQLException, etc.
- Unchecked exceptions are those that are not checked by the compiler at compile-time and are usually caused by logical errors or bugs in the code. For example, ArithmeticException, NullPointerException, ArrayIndexOutOfBoundsException, etc.
- Errors are those that are not handled by the programmer and are usually caused by system failures or resource limitations. For example, OutOfMemoryError, StackOverflowError, etc.
- The Throwable class is the root class of the exception hierarchy and has two subclasses: Exception and Error.
- To handle exceptions, Java provides the try-catch-finally block and the throw and throws keywords.
- The try block contains the code that may throw an exception and must be followed by either a catch block or a finally block or both.
- The catch block contains the code that handles the specific type of exception thrown by the try block. There can be multiple catch blocks for different types of exceptions.
- The finally block contains the code that is always executed regardless of whether an exception is thrown or not. It is used to release resources or perform cleanup tasks.
- The throw keyword is used to explicitly throw an exception from a method or a block of code.
- The throws keyword is used to declare that a method may throw one or more exceptions. It is specified after the method signature and before the method body.
- A simple example of exception handling in Java is:

```java
public class ExceptionExample {
    public static void main(String[] args) {
        try {
            int a = 10;
            int b = 0;
            int c = a / b; // this may throw ArithmeticException
            System.out.println("The result is " + c);
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero");
        } finally {
            System.out.println("This is always executed");
        }
    }
}
```

- The output of the above code is:

```
Cannot divide by zero
This is always executed
```

- Some mnemonics and learning tricks for exception handling in Java are:

  - **T**ry **C**atch **F**inally: remember the order of the blocks in exception handling
  - **T**hrow **T**hrows: remember the difference between the two keywords
  - **C**hecked **U**nchecked **E**rror: remember the three types of exceptions
  - **T**hrowable **E**xception **E**rror: remember the hierarchy of the exception classes
  - **R**untime **E**xception: remember that unchecked exceptions are also called runtime exceptions