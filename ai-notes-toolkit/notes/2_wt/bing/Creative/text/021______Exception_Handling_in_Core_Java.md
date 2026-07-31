#### Exception Handling in Core Java

- An exception is an abnormal or unexpected event that occurs during the execution of a program and disrupts its normal flow.
- Exception handling is a mechanism that allows a program to deal with exceptions gracefully and prevent the program from terminating abruptly.
- Exception handling in core Java involves four keywords: try, catch, throw and finally.
- The try block contains the code that may cause an exception. The catch block contains the code that handles the specific exception. The finally block contains the code that is always executed regardless of whether an exception occurs or not.
- The throw keyword is used to explicitly throw an exception from a method or a block of code. The throws keyword is used to declare that a method may throw one or more exceptions.
- Java provides two types of exceptions: checked and unchecked. Checked exceptions are those that are checked by the compiler at compile-time and must be handled or declared by the programmer. Unchecked exceptions are those that are not checked by the compiler and are usually caused by runtime errors or logical errors.
- Some of the common checked exceptions are IOException, FileNotFoundException, ClassNotFoundException, etc. Some of the common unchecked exceptions are ArithmeticException, NullPointerException, ArrayIndexOutOfBoundsException, etc.
- Java also provides a hierarchy of exception classes that inherit from the java.lang.Throwable class. The Throwable class has two subclasses: java.lang.Exception and java.lang.Error. The Exception class is the superclass of all checked and unchecked exceptions. The Error class is the superclass of all errors that are usually fatal and should not be handled by the program.