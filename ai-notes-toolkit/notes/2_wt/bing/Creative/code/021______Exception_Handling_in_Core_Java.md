#### Exception Handling in Core Java

Exception handling is a mechanism to handle runtime errors and abnormal conditions that may occur during the execution of a program. Exception handling allows the program to continue its normal flow or terminate gracefully, without crashing or producing incorrect results.

The basic syntax of exception handling in core Java is:

```java
try {
  // code that may throw an exception
} catch (ExceptionType e) {
  // code to handle the exception
} finally {
  // code that will always execute, regardless of whether an exception is thrown or not
}
```

The `try` block contains the code that may throw an exception. The `catch` block contains the code to handle the specific type of exception that is caught by the parameter `e`. The `finally` block contains the code that will always execute, such as closing resources or releasing locks. The `finally` block is optional, but recommended.

There are two types of exceptions in Java: checked and unchecked. Checked exceptions are those that are declared in the `throws` clause of a method, and must be handled or propagated by the caller. Unchecked exceptions are those that are not declared in the `throws` clause, and are usually caused by programming errors or unexpected situations. Unchecked exceptions are subclasses of `RuntimeException` or `Error`.

An example of a checked exception is `IOException`, which may occur when performing input/output operations. An example of an unchecked exception is `NullPointerException`, which may occur when accessing a null reference.

To handle multiple types of exceptions, we can use multiple `catch` blocks, each with a different parameter type. The order of the `catch` blocks matters, as the first one that matches the thrown exception will be executed. We can also use a single `catch` block with a generic parameter type `Exception`, which can handle any type of exception. However, this is not recommended, as it may hide the specific cause of the error and make debugging harder.

To propagate an exception to the caller, we can use the `throw` keyword, followed by an exception object. We can also use the `throws` keyword in the method signature, followed by the types of exceptions that the method may throw. This informs the caller that the method may throw these exceptions, and they must be handled or propagated further.

An example of exception handling in core Java is:

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ExceptionDemo {

  public static void main(String[] args) {
    try {
      // create a file object
      File file = new File("test.txt");
      // create a scanner object to read the file
      Scanner scanner = new Scanner(file);
      // read the first line of the file
      String line = scanner.nextLine();
      // print the line
      System.out.println(line);
      // close the scanner
      scanner.close();
    } catch (FileNotFoundException e) {
      // handle the file not found exception
      System.out.println("The file does not exist.");
    } catch (Exception e) {
      // handle any other exception
      System.out.println("An error occurred.");
      // print the stack trace of the exception
      e.printStackTrace();
    } finally {
      // code that will always execute
      System.out.println("End of program.");
    }
  }
}
```