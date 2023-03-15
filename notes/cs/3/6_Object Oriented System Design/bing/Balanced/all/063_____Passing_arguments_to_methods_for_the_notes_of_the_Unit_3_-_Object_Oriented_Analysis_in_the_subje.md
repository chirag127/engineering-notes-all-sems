# Passing arguments to methods

- A method is a block of code that performs a specific task and can be invoked by other parts of a program.
- A method can have zero or more parameters, which are variables that hold the values passed to the method by the caller.
- A method can also have zero or more arguments, which are the actual values that are passed to the method when it is invoked.
- There are two ways of passing arguments to methods in Java: by value and by reference.
- Passing by value means that a copy of the argument value is passed to the method, and any changes made to the parameter inside the method do not affect the original argument.
- Passing by reference means that the reference (or address) of the argument object is passed to the method, and any changes made to the parameter inside the method do affect the original argument object.
- Primitive types (such as int, double, char, boolean) are always passed by value in Java, while reference types (such as arrays, strings, objects) are always passed by reference in Java.
- Example of passing by value:

```java
public class PassByValue {
  public static void main(String[] args) {
    int x = 10; // x is a primitive type
    System.out.println("Before calling changeValue: x = " + x);
    changeValue(x); // pass x by value
    System.out.println("After calling changeValue: x = " + x);
  }

  public static void changeValue(int n) { // n is a parameter
    n = 20; // change the value of n
    System.out.println("Inside changeValue: n = " + n);
  }
}
```

Output:

```
Before calling changeValue: x = 10
Inside changeValue: n = 20
After calling changeValue: x = 10
```

- Example of passing by reference:

```java
public class PassByReference {
  public static void main(String[] args) {
    int[] arr = {1, 2, 3}; // arr is a reference type
    System.out.println("Before calling changeArray: arr = " + Arrays.toString(arr));
    changeArray(arr); // pass arr by reference
    System.out.println("After calling changeArray: arr = " + Arrays.toString(arr));
  }

  public static void changeArray(int[] a) { // a is a parameter
    a[0] = 10; // change the value of the first element of a
    System.out.println("Inside changeArray: a = " + Arrays.toString(a));
  }
}
```

Output:

```
Before calling changeArray: arr = [1, 2, 3]
Inside changeArray: a = [10, 2, 3]
After calling changeArray: arr = [10, 2, 3]
```