#### Variable in Core Java

A variable in core Java is a name given to a memory location that can store data of a specific type. Variables are used to store and manipulate data in a Java program. Variables can be declared, initialized, and used in different ways depending on their scope and modifier.

There are four types of variables in core Java:

- **Local variables**: These are variables that are declared and used within a block, method, or constructor. They are created when the block or method is entered and destroyed when it exits. They have a local scope and cannot be accessed outside the block or method. They must be initialized before they can be used. For example:

```java
public void add(int a, int b) {
  int sum = a + b; // sum is a local variable
  System.out.println(sum);
}
```

- **Instance variables**: These are variables that are declared in a class, but outside any method, constructor, or block. They are also called non-static variables or fields. They are created when an object of the class is instantiated and destroyed when the object is garbage collected. They have a global scope and can be accessed by any method of the class or by other classes using the object reference. They can have access modifiers (public, private, protected, or default) that determine their visibility. They have a default value depending on their data type. For example:

```java
public class Student {
  String name; // name is an instance variable
  int age; // age is an instance variable
  // constructor
  public Student(String name, int age) {
    this.name = name;
    this.age = age;
  }
  // method
  public void display() {
    System.out.println(name + " is " + age + " years old.");
  }
}
```

- **Static variables**: These are variables that are declared in a class, but outside any method, constructor, or block, with the static keyword. They are also called class variables. They are created when the class is loaded and destroyed when the class is unloaded. They have a global scope and can be accessed by any method of the class or by other classes using the class name. They can have access modifiers (public, private, protected, or default) that determine their visibility. They have a default value depending on their data type. They are shared by all the objects of the class. For example:

```java
public class Math {
  static final double PI = 3.14; // PI is a static variable
  // method
  public static double areaOfCircle(double radius) {
    return PI * radius * radius;
  }
}
```

- **Parameters**: These are variables that are declared in the method signature and used to pass values to the method. They are also called arguments or formal parameters. They are created when the method is invoked and destroyed when the method returns. They have a local scope and can be accessed only within the method. They must be initialized by the caller of the method. For example:

```java
public void printMessage(String message) {
  System.out.println(message); // message is a parameter
}
```