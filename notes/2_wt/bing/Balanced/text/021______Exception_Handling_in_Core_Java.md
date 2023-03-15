#### Exception Handling in Core Java

- An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.
- Exception handling is a mechanism that allows a program to deal with exceptional situations gracefully, without terminating abruptly.
- In Java, an exception is an object that represents the error or the abnormal condition. It contains information about the type, cause, and location of the error.
- Java provides a built-in hierarchy of exception classes, derived from the java.lang.Throwable class. The two direct subclasses of Throwable are java.lang.Exception and java.lang.Error.
- Exceptions that are subclasses of Exception are called checked exceptions. They represent recoverable errors and must be handled by the programmer, either by using a try-catch block or by declaring them in the method signature using the throws keyword.
- Exceptions that are subclasses of Error are called unchecked exceptions. They represent unrecoverable errors and are not required to be handled by the programmer. They are usually caused by the JVM or the hardware and can be ignored by the program.
- A try-catch block is a block of code that contains a set of statements that may throw an exception, and one or more catch blocks that handle the specific types of exceptions that may occur.
- A try block must be followed by either at least one catch block or a finally block. A finally block is a block of code that is always executed, regardless of whether an exception occurs or not. It is used to perform cleanup tasks such as closing resources or releasing locks.
- A catch block must specify the type of exception it can handle, using the parameter of the catch clause. The parameter is an object of the exception class or its subclass. The catch block can access the information of the exception object using methods such as getMessage(), getCause(), and getStackTrace().
- A catch block can rethrow the exception to the caller using the throw keyword, or throw a new exception using the new keyword. A throw statement must be followed by an object of the Throwable class or its subclass.
- A try-catch block can be nested within another try-catch block. The inner try-catch block can handle the exceptions that occur within its scope, and the outer try-catch block can handle the exceptions that are not handled by the inner try-catch block or that are rethrown by it.
- A try-catch block can also be used with the resources, such as files, streams, sockets, etc. that implement the java.lang.AutoCloseable interface. This is called the try-with-resources statement. It ensures that the resources are automatically closed at the end of the try block, even if an exception occurs. The syntax of the try-with-resources statement is:

```java
try(resource1; resource2; ...){
  // statements that may throw exceptions
}catch(ExceptionType e){
  // handle the exception
}finally{
  // optional finally block
}
```
- A method can declare the exceptions that it may throw using the throws keyword in its signature. This indicates that the method does not handle the exceptions, but passes them to the caller. The caller must handle the exceptions using a try-catch block or declare them in its own signature. The syntax of the throws clause is:

```java
modifier returnType methodName(parameters) throws ExceptionType1, ExceptionType2, ...{
  // method body
}
```
- A method can also create and throw a custom exception class, by extending the java.lang.Exception class or its subclass. The custom exception class must have a constructor that invokes the constructor of the superclass, using the super keyword. The custom exception class can also have its own fields and methods to provide additional information about the error. The syntax of the custom exception class is:

```java
public class CustomException extends Exception{
  // fields
  public CustomException(){
    super();
  }
  public CustomException(String message){
    super(message);
  }
  // methods
}
```