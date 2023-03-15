### Constructors and their types

- A constructor is a special method that is used to initialize an object of a class.
- A constructor has the same name as the class and does not have a return type.
- A constructor is invoked automatically when an object of the class is created using the `new` operator.
- A constructor can perform tasks such as setting the initial values of the object's attributes, allocating memory for the object, or calling other methods of the class or its superclasses.
- There are two types of constructors: parameterized and default.

#### Parameterized constructors
- A parameterized constructor is a constructor that takes one or more parameters to initialize the object's attributes.
- A parameterized constructor can be overloaded to provide different ways of creating an object of the class.
- A parameterized constructor can call another constructor of the same class using the `this` keyword, or a constructor of the superclass using the `super` keyword.
- Example of a parameterized constructor:

```java
// A class that represents a point in a 2D plane
class Point {
  // Attributes
  private double x;
  private double y;

  // Parameterized constructor
  public Point(double x, double y) {
    // Initialize the attributes with the parameters
    this.x = x;
    this.y = y;
  }

  // Another parameterized constructor
  public Point(Point p) {
    // Initialize the attributes with the values of another point
    this.x = p.x;
    this.y = p.y;
  }

  // Getters and setters
  public double getX() {
    return x;
  }

  public void setX(double x) {
    this.x = x;
  }

  public double getY() {
    return y;
  }

  public void setY(double y) {
    this.y = y;
  }
}
```

#### Default constructors
- A default constructor is a constructor that does not take any parameters and provides a default initialization for the object's attributes.
- A default constructor is implicitly provided by the compiler if no other constructor is defined in the class.
- A default constructor can call a constructor of the superclass using the `super` keyword.
- Example of a default constructor:

```java
// A class that represents a circle
class Circle {
  // Attributes
  private Point center; // A point object to store the center of the circle
  private double radius; // A double value to store the radius of the circle

  // Default constructor
  public Circle() {
    // Initialize the attributes with default values
    center = new Point(0, 0); // Create a point object at the origin
    radius = 1; // Set the radius to 1
  }

  // Getters and setters
  public Point getCenter() {
    return center;
  }

  public void setCenter(Point center) {
    this.center = center;
  }

  public double getRadius() {
    return radius;
  }

  public void setRadius(double radius) {
    this.radius = radius;
  }
}
```