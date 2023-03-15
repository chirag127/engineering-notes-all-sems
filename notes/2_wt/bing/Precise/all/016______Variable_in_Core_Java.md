#### Variable in Core Java
A variable in Java is a container that holds a value. It is a named memory location that stores a value of a specific data type. The value of a variable can change during the execution of a program.

- **Declaration**: A variable must be declared before it can be used. The declaration specifies the data type of the variable and its name. For example, `int x;` declares a variable named `x` of type `int`.
- **Initialization**: A variable can be initialized, or assigned a value, at the time of declaration or later in the program. For example, `int x = 10;` declares and initializes a variable named `x` of type `int` with the value `10`.
- **Data Types**: Java has two categories of data types: primitive and reference. Primitive data types include `byte`, `short`, `int`, `long`, `float`, `double`, `char`, and `boolean`. Reference data types include arrays, classes, and interfaces.
- **Scope**: The scope of a variable refers to the part of the program where the variable can be accessed. The scope of a variable depends on where it is declared. For example, a variable declared within a method can only be accessed within that method.
- **Lifetime**: The lifetime of a variable refers to the duration for which the variable exists in memory. The lifetime of a variable depends on its scope. For example, a variable declared within a method is created when the method is called and destroyed when the method returns.

A mnemonic to remember the primitive data types in Java is `Be Careful, Boys Shouldn't Intimidate Little Fish`. The first letter of each word represents a primitive data type: `byte`, `char`, `boolean`, `short`, `int`, `long`, `float`, `double`. This mnemonic is easy to remember because it forms a sentence with a meaning.

Here is an example of declaring, initializing, and using a variable in Java:

```java
public class VariableExample {
    public static void main(String[] args) {
        int x; // declaration
        x = 10; // initialization
        System.out.println(x); // usage
    }
}
```

In this example, a variable named `x` of type `int` is declared, initialized with the value `10`, and then used to print its value to the standard output. The output of this program is `10`.