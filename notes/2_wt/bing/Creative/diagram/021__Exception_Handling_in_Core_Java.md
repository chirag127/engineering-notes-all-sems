Exception handling in core Java is a mechanism to handle runtime errors so that the normal flow of the application can be maintained. Exceptions are events that disrupt the normal flow of the program and are objects that are thrown at runtime. Exceptions can be checked or unchecked, depending on whether they are checked at compile-time or runtime. Errors are also a type of unchecked exception that occur due to severe problems that are not in control of the programmer.

#### Exception Handling in Core Java

The following diagram illustrates the basic architecture of exception handling in core Java using ASCII characters:

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Throwable    |<---|    Error       |<---|  OutOfMemory   |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
       ^                      ^                      ^
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Exception    |<---| RuntimeException|<---|ArithmeticException
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
       ^                      ^                      ^
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|  IOException  |<---| NullPointerException|<---|ArrayIndexOutOfBoundsException
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```

The diagram shows the hierarchy of the exception classes in Java. The Throwable class is the root class of all exceptions and errors. The Exception class is a subclass of Throwable and represents the exceptions that can be handled by the programmer. The Error class is also a subclass of Throwable and represents the errors that are beyond the control of the programmer and usually indicate serious problems. The RuntimeException class is a subclass of Exception and represents the unchecked exceptions that are not checked at compile-time but are checked at runtime. The IOException class is a subclass of Exception and represents the checked exceptions that are related to input/output operations. The NullPointerException, ArithmeticException, and ArrayIndexOutOfBoundsException classes are subclasses of RuntimeException and represent some common unchecked exceptions that occur due to null references, arithmetic errors, and invalid array indices respectively. The OutOfMemory class is a subclass of Error and represents the error that occurs when the Java Virtual Machine runs out of memory.

The diagram also shows how the exception handling mechanism works in core Java. When an exception occurs, an object of the corresponding exception class is created and thrown by the JVM or by the method executing the code. The thrown exception object can be caught and handled by a try-catch block or a try-catch-finally block. The try block contains the code that may cause an exception. The catch block contains the code that handles the specific exception. The finally block contains the code that is always executed regardless of whether an exception occurs or not. The catch block can have multiple clauses to handle different types of exceptions. The catch block can also rethrow the exception to the caller method using the throw keyword. The caller method can either handle the exception or declare it using the throws keyword. The exception propagation mechanism allows the exception to be passed up the call stack until it is handled or reaches the main method. If the exception is not handled by any method, the program terminates abnormally and prints the stack trace of the exception. The stack trace shows the sequence of method calls that led to the exception and helps to locate the source of the error.