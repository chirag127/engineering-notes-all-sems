### Passing arguments to methods

- Arguments are the values that are passed to a method when it is invoked.
- Parameters are the variables that are declared in the method signature to receive the arguments.
- In Java, arguments are always passed by value, which means a copy of the argument is passed to the method and the original value is not affected by the method.
- There are two types of arguments in Java: primitive values and reference values.
- Primitive values are the basic data types, such as int, double, char, boolean, etc. When a primitive value is passed as an argument, the method receives a copy of the value and can modify it without affecting the original value.
- Reference values are the values that refer to objects, such as arrays, strings, classes, etc. When a reference value is passed as an argument, the method receives a copy of the reference, which points to the same object as the original reference. The method can modify the object's state through the reference, but cannot change the reference itself to point to a different object.
- Example of passing primitive values:

```java
public class PassByValueExample {
  public static void main(String[] args) {
    int x = 10; // declare and initialize a primitive value
    System.out.println("Before calling the method, x is " + x); // print the original value
    increment(x); // pass x as an argument to the method
    System.out.println("After calling the method, x is " + x); // print the value after the method call
  }

  public static void increment(int n) { // declare a parameter of type int
    n++; // increment the parameter by 1
    System.out.println("Inside the method, n is " + n); // print the parameter value
  }
}
```

Output:

```
Before calling the method, x is 10
Inside the method, n is 11
After calling the method, x is 10
```

- Example of passing reference values:

```java
public class PassByReferenceExample {
  public static void main(String[] args) {
    int[] arr = {1, 2, 3}; // declare and initialize an array object
    System.out.println("Before calling the method, arr[0] is " + arr[0]); // print the first element of the array
    multiply(arr); // pass arr as an argument to the method
    System.out.println("After calling the method, arr[0] is " + arr[0]); // print the first element of the array after the method call
  }

  public static void multiply(int[] a) { // declare a parameter of type int[]
    a[0] = a[0] * 10; // multiply the first element of the array by 10
    System.out.println("Inside the method, a[0] is " + a[0]); // print the first element of the array
  }
}
```

Output:

```
Before calling the method, arr[0] is 1
Inside the method, a[0] is 10
After calling the method, arr[0] is 10
```

- References:
  -  Passing Arguments to Methods in Java - Computer Notes
  -  Pass-By-Value as a Parameter Passing Mechanism in Java
  -  Java Method Parameters - W3Schools
  -  Passing Information to a Method or a Constructor (The Java™ Tutorials)
  -  Parameter Passing Techniques in Java with Examples