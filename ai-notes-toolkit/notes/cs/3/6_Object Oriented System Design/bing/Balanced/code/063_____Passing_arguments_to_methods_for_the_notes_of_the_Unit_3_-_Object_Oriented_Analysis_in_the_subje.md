### Passing arguments to methods

- A method is a block of code that performs a specific task and can be invoked by other parts of a program.
- A method can have zero or more parameters, which are variables that receive the values of the arguments passed to the method when it is called.
- An argument is a value that is passed to a method when it is invoked. The argument can be a literal value, a variable, or an expression.
- The number and type of arguments passed to a method must match the number and type of parameters declared in the method header, unless the method uses variable-length arguments (varargs).
- There are two ways of passing arguments to methods in Java: pass-by-value and pass-by-reference.
- Pass-by-value means that a copy of the argument value is passed to the method, and any changes made to the parameter within the method do not affect the original argument.
- Pass-by-reference means that a reference to the argument object is passed to the method, and any changes made to the parameter within the method do affect the original argument.
- Primitive types (such as int, double, char, boolean) are always passed by value in Java, while reference types (such as arrays, strings, objects) are always passed by reference in Java.
- Example of pass-by-value:

```java
public class PassByValueDemo {
  public static void main(String[] args) {
    int x = 10; // declare and initialize a variable x
    System.out.println("Before calling the method, x = " + x); // print the value of x
    change(x); // call the method change with x as an argument
    System.out.println("After calling the method, x = " + x); // print the value of x again
  }

  public static void change(int n) { // declare a method with a parameter n
    n = 20; // assign a new value to n
    System.out.println("Inside the method, n = " + n); // print the value of n
  }
}
```

Output:

```
Before calling the method, x = 10
Inside the method, n = 20
After calling the method, x = 10
```

Explanation:

- The value of x is copied and passed to the method change as n.
- The method change assigns a new value to n, but this does not affect the value of x in the main method.
- The value of x remains unchanged after the method call.

- Example of pass-by-reference:

```java
public class PassByReferenceDemo {
  public static void main(String[] args) {
    int[] array = {1, 2, 3}; // declare and initialize an array
    System.out.println("Before calling the method, array[0] = " + array[0]); // print the first element of the array
    change(array); // call the method change with the array as an argument
    System.out.println("After calling the method, array[0] = " + array[0]); // print the first element of the array again
  }

  public static void change(int[] arr) { // declare a method with an array parameter
    arr[0] = 10; // assign a new value to the first element of the array
    System.out.println("Inside the method, arr[0] = " + arr[0]); // print the first element of the array
  }
}
```

Output:

```
Before calling the method, array[0] = 1
Inside the method, arr[0] = 10
After calling the method, array[0] = 10
```

Explanation:

- The reference to the array object is passed to the method change as arr.
- The method change modifies the first element of the array, but this affects the original array object in the main method.
- The value of array[0] changes after the method call.