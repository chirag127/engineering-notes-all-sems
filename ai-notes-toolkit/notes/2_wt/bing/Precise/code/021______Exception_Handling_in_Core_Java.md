#### Exception Handling in Core Java
Exception handling is a mechanism in Java to handle runtime errors and exceptional conditions. It is achieved using the `try`, `catch`, and `finally` blocks.

Here is an example of how to use exception handling in Core Java:

```java
public class ExceptionExample {
    public static void main(String[] args) {
        try {
            int a = 5;
            int b = 0;
            int c = a / b;
            System.out.println("Result: " + c);
        } catch (ArithmeticException e) {
            System.out.println("Error: Cannot divide by zero");
        } finally {
            System.out.println("This code will always be executed");
        }
    }
}
```

In the above example, we are trying to divide a number by zero, which will throw an `ArithmeticException`. The `catch` block catches this exception and handles it by printing an error message. The `finally` block is executed regardless of whether an exception is thrown or not.