### Passing arguments to methods

- A method is a block of code that performs a specific task and can be invoked by other parts of a program.
- A method can have zero or more parameters, which are variables that receive the values of the arguments passed to the method when it is called.
- An argument is a value that is passed to a method when it is invoked.
- There are two ways of passing arguments to methods in Java: by value and by reference.
- Passing by value means that a copy of the argument value is passed to the method, and any changes made to the parameter inside the method do not affect the original argument.
- Passing by reference means that the reference (or address) of the argument object is passed to the method, and any changes made to the parameter inside the method affect the original argument object.
- Primitive types (such as int, double, char, boolean) are always passed by value in Java, while reference types (such as arrays, strings, objects) are always passed by reference in Java.
- Example of passing by value:

```java
public class PassByValue {
  public static void main(String[] args) {
    int x = 10; // declare and initialize a variable x
    System.out.println("Before calling the method, x = " + x); // print the value of x
    change(x); // call the method change with x as an argument
    System.out.println("After calling the method, x = " + x); // print the value of x again
  }

  public static void change(int n) { // declare a method change with a parameter n
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

- The value of x (10) is copied and passed to the method change, where it is assigned to the parameter n.
- The value of n is changed to 20 inside the method, but this does not affect the value of x outside the method, because x and n are different variables in different memory locations.
- Therefore, the value of x remains 10 after the method call.

- Example of passing by reference:

```java
public class PassByReference {
  public static void main(String[] args) {
    int[] arr = {1, 2, 3}; // declare and initialize an array arr
    System.out.println("Before calling the method, arr = " + Arrays.toString(arr)); // print the array arr
    change(arr); // call the method change with arr as an argument
    System.out.println("After calling the method, arr = " + Arrays.toString(arr)); // print the array arr again
  }

  public static void change(int[] a) { // declare a method change with a parameter a
    a[0] = 10; // assign a new value to the first element of a
    System.out.println("Inside the method, a = " + Arrays.toString(a)); // print the array a
  }
}
```

Output:

```
Before calling the method, arr = [1, 2, 3]
Inside the method, a = [10, 2, 3]
After calling the method, arr = [10, 2, 3]
```

Explanation:

- The reference (or address) of the array arr is passed to the method change, where it is assigned to the parameter a.
- The parameter a and the argument arr refer to the same array object in memory, so any changes made to the elements of a inside the method affect the elements of arr outside the method.
- Therefore, the value of the first element of arr is changed to 10 after the method call.