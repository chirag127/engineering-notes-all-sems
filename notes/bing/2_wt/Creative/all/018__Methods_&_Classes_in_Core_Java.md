#### Methods & Classes in Core Java

- A method is a block of code that performs a specific task. A method can be invoked (called) by another method, by an object, or by itself.
- A class is a blueprint or template for creating objects. A class defines the properties (attributes) and behaviors (methods) of its objects.
- A class can have one or more methods. A method can have zero or more parameters. A parameter is a variable that receives a value when the method is invoked.
- A method can have zero or more return statements. A return statement ends the execution of the method and returns a value to the caller.
- A method can be public, private, protected, or default. The access modifier determines who can access the method.
- A method can be static or non-static. A static method belongs to the class and can be invoked without creating an object. A non-static method belongs to the object and can be invoked only by the object.
- A method can be abstract or concrete. An abstract method has no body and must be overridden by a subclass. A concrete method has a body and can be inherited or overridden by a subclass.
- A method can be final or non-final. A final method cannot be overridden by a subclass. A non-final method can be overridden by a subclass.
- A method can be overloaded or overridden. Overloading means defining multiple methods with the same name but different parameters. Overriding means redefining a method in a subclass that already exists in the superclass.
- A class can be public, private, protected, or default. The access modifier determines who can access the class.
- A class can be static or non-static. A static class can only have static members and cannot be instantiated. A non-static class can have both static and non-static members and can be instantiated.
- A class can be abstract or concrete. An abstract class cannot be instantiated and must have at least one abstract method. A concrete class can be instantiated and can have both abstract and concrete methods.
- A class can be final or non-final. A final class cannot be inherited by a subclass. A non-final class can be inherited by a subclass.
- A class can be a superclass or a subclass. A superclass is a class that is inherited by another class. A subclass is a class that inherits from another class.
- A class can implement one or more interfaces. An interface is a collection of abstract methods that a class must implement.
- A class can have one or more constructors. A constructor is a special method that is invoked when an object is created. A constructor can be public, private, protected, or default. A constructor can be overloaded but not overridden.

Here is an example of a class and a method in Core Java:

```java
// A class named Rectangle
public class Rectangle {
  // A private attribute named length
  private double length;
  // A private attribute named width
  private double width;
  
  // A public constructor with two parameters
  public Rectangle(double length, double width) {
    // Assign the parameters to the attributes
    this.length = length;
    this.width = width;
  }
  
  // A public method named getArea that returns the area of the rectangle
  public double getArea() {
    // Return the product of length and width
    return length * width;
  }
  
  // A public method named getPerimeter that returns the perimeter of the rectangle
  public double getPerimeter() {
    // Return the sum of twice the length and twice the width
    return 2 * (length + width);
  }
}
```

Here is an example of how to use the class and the methods:

```java
// Create an object of the Rectangle class with length 10 and width 5
Rectangle r1 = new Rectangle(10, 5);
// Invoke the getArea method and print the result
System.out.println("The area of the rectangle is " + r1.getArea());
// Invoke the getPerimeter method and print the result
System.out.println("The perimeter of the rectangle is " + r1.getPerimeter());
```