#### Exception Handling in Core Java

Exception Handling is a mechanism that helps to handle the runtime errors in a program. It is an important concept in Core Java as it ensures that a program runs smoothly without any errors. Exception handling involves detecting and responding to errors at runtime.

In Java, an exception is an event that disrupts the normal flow of the program. Whenever an exception occurs, the program halts and the control is transferred to the nearest exception handler. Exception handling in Java is done using the try-catch block. The try block contains the code that may throw an exception, and the catch block handles the exception if it is thrown.

The syntax for the try-catch block is as follows:

```
try {
   // code that may throw an exception
}
catch (ExceptionType exceptionObjectName) {
   // code to handle the exception
}
finally {
   // code that is executed whether an exception is thrown or not
}
```

Some of the commonly used Exception Handling keywords in Java are:

- try: The try block contains the code that may throw an exception.
- catch: The catch block handles the exception if it is thrown.
- finally: The finally block contains the code that is executed whether an exception is thrown or not.
- throw: The throw keyword is used to manually throw an exception.
- throws: The throws keyword is used to declare the exception that a method may throw.

Advantages of Exception Handling in Java:

- It helps in maintaining the normal flow of the program by handling the errors at runtime.
- It provides a clear and concise way to handle the errors in a program.
- It separates the error handling code from the normal program flow, making the code more readable and maintainable.

Disadvantages of Exception Handling in Java:

- Exception handling can sometimes lead to performance issues as it involves overhead in terms of time and memory.
- It can sometimes make the code more complex and difficult to understand.

Mnemonics and Learning Tricks:

- Remember the keywords try, catch, and finally as TCF (Try Catch Finally).
- Think of catch as a safety net that catches the exception and prevents the program from crashing.
- Remember that the finally block always executes, whether an exception is thrown or not.