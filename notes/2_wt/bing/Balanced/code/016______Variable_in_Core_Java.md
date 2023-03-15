#### Variable in Core Java

A variable in core Java is a data container that stores the data values during Java program execution. Every variable is assigned a data type that designates the type and quantity of value it can hold. A variable is a name given to a memory location. It is the basic unit of storage in a program  .

Variables in Java can be defined anywhere in the code (inside a class, inside a method, or as a method argument) and can have different modifiers. Depending on these conditions, variables in Java can be divided into four categories:

- **Instance variable**: A variable that is declared inside a class but outside a method is known as an instance variable. It is not declared as static. It is called instance variable because its value is instance specific and is not shared among instances.
- **Static variable**: A variable that is declared as static is known as a static variable. It cannot be local. It is a single copy shared among all the instances of the class. Memory allocation for a static variable happens only once when the class is loaded in the memory.
- **Local variable**: A variable that is declared inside a method is known as a local variable. It cannot be declared with static keyword. It is only visible within the method and the other methods in the class cannot access the variable.
- **Parameter variable**: A variable that is declared as a method argument is known as a parameter variable. It is used to pass the values to the method during method call.

Some examples of variables in Java are :

```java
// String variable
String name = "John";

// int variable
int age = 25;

// float variable
float salary = 5000.50f;

// static variable
static int count = 0;

// instance variable
int id;

// local variable
public void display() {
  int x = 10; // local variable
  System.out.println(x);
}

// parameter variable
public void add(int a, int b) { // a and b are parameter variables
  int c = a + b;
  System.out.println(c);
}
```