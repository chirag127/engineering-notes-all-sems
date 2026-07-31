#### Methods & Classes in Core Java

- A method is a block of code that performs a specific task. A method can be invoked (called) by another method, by creating an object, or directly from a class.
- A class is a blueprint for creating objects. A class can contain fields (variables) and methods (functions) that define the properties and behaviors of the objects.
- The syntax for declaring a method is:

```java
modifier returnType methodName(parameters) {
  // method body
}
```

- The modifier specifies the access level of the method (public, private, protected, etc.).
- The returnType specifies the type of value the method returns, or void if the method does not return anything.
- The methodName is the name of the method, which should follow the naming conventions of Java.
- The parameters are optional and specify the input values for the method. Multiple parameters are separated by commas.
- The method body contains the statements that define what the method does.

- The syntax for declaring a class is:

```java
modifier class ClassName {
  // fields and methods
}
```

- The modifier specifies the access level of the class (public, private, protected, etc.).
- The ClassName is the name of the class, which should follow the naming conventions of Java.
- The class body contains the fields and methods that belong to the class.

- Some examples of methods and classes in core Java are:

```java
// A method that calculates the area of a circle
public double area(double radius) {
  return Math.PI * radius * radius;
}

// A class that represents a person
public class Person {
  // A field that stores the name of the person
  private String name;

  // A constructor that initializes the name field
  public Person(String name) {
    this.name = name;
  }

  // A method that returns the name of the person
  public String getName() {
    return name;
  }

  // A method that sets the name of the person
  public void setName(String name) {
    this.name = name;
  }
}
```