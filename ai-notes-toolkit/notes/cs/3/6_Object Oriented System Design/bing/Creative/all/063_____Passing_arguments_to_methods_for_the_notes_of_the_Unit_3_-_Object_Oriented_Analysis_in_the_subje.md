Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of passing arguments to methods for the notes of the Unit 3 - Object Oriented Analysis in the subject of Object Oriented System Design.

# Passing arguments to methods

- A method is a named group of statements that performs a specific task in a program.
- A method can have zero or more parameters, which are variables that receive values from the caller of the method.
- A method can also return a value to the caller, or perform some action without returning anything.
- A method can be invoked or called by using its name followed by a pair of parentheses, optionally containing arguments that match the parameters of the method.
- An argument is a value or expression that is passed to a method when it is invoked.
- There are two ways of passing arguments to methods in Java: by value and by reference.

## Passing arguments by value

- When an argument is passed by value, a copy of the argument's value is made and assigned to the corresponding parameter of the method.
- The original argument and the parameter are two separate variables that have the same value, but are stored in different memory locations.
- Any changes made to the parameter inside the method do not affect the original argument outside the method.
- Primitive data types, such as int, double, char, and boolean, are always passed by value in Java.

## Passing arguments by reference

- When an argument is passed by reference, the parameter of the method receives the reference or address of the argument, not a copy of its value.
- The original argument and the parameter are two variables that refer to the same object in memory.
- Any changes made to the parameter inside the method affect the original argument outside the method, as they both point to the same object.
- Reference data types, such as arrays, strings, and objects, are always passed by reference in Java.

## Example of passing arguments by value

```java
public class PassByValue {

    // A method that swaps the values of two int variables
    public static void swap(int a, int b) {
        int temp = a; // store the value of a in a temporary variable
        a = b; // assign the value of b to a
        b = temp; // assign the value of temp to b
        System.out.println("Inside swap method: a = " + a + ", b = " + b);
    }

    public static void main(String[] args) {
        int x = 10; // declare and initialize an int variable x
        int y = 20; // declare and initialize an int variable y
        System.out.println("Before swap method: x = " + x + ", y = " + y);
        swap(x, y); // call the swap method with x and y as arguments
        System.out.println("After swap method: x = " + x + ", y = " + y);
    }
}
```

Output:

```
Before swap method: x = 10, y = 20
Inside swap method: a = 20, b = 10
After swap method: x = 10, y = 20
```

Explanation:

- In the main method, two int variables x and y are declared and initialized with the values 10 and 20 respectively.
- The swap method is called with x and y as arguments. The values of x and y are copied and assigned to the parameters a and b of the swap method.
- Inside the swap method, the values of a and b are swapped using a temporary variable temp. The values of a and b are printed inside the method.
- After the swap method returns, the values of x and y are printed in the main method. The values of x and y are unchanged, as they are passed by value and not affected by the swap method.

## Example of passing arguments by reference

```java
public class PassByReference {

    // A method that swaps the elements of two int arrays
    public static void swap(int[] a, int[] b) {
        int temp = a[0]; // store the value of the first element of a in a temporary variable
        a[0] = b[0]; // assign the value of the first element of b to the first element of a
        b[0] = temp; // assign the value of temp to the first element of b
        System.out.println("Inside swap method: a[0] = " + a[0] + ", b[0] = " + b[0]);
    }

    public static void main(String[] args) {
        int[] x = {10}; // declare and initialize an int array x

```
