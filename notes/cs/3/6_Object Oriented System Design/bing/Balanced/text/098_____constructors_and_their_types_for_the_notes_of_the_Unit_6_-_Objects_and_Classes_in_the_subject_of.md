### Constructors and their types

- A constructor is a special method of a class or structure in object-oriented programming that initializes a newly created object of that type.
- Whenever an object is created, the constructor is called automatically.
- A constructor has the same name as the class or structure and does not have a return type.
- A constructor can have parameters to set the initial values of the object's attributes.
- There are different types of constructors depending on the number and type of parameters, the source of the object's data, and the inheritance relationship between classes .
- Some of the common types of constructors are:

  - Default constructor: A constructor that does not take any argument and sets the default values for the object's attributes. For example:

    ```c++
    class Point {
      int x;
      int y;
      public:
      // Default constructor
      Point() {
        x = 0;
        y = 0;
      }
    };
    ```

  - Parameterized constructor: A constructor that takes one or more arguments and sets the initial values for the object's attributes based on the arguments. For example:

    ```c++
    class Point {
      int x;
      int y;
      public:
      // Parameterized constructor
      Point(int a, int b) {
        x = a;
        y = b;
      }
    };
    ```

  - Copy constructor: A constructor that takes another object of the same class as an argument and copies the values of its attributes to the new object. This is useful for creating a duplicate of an existing object. For example:

    ```c++
    class Point {
      int x;
      int y;
      public:
      // Copy constructor
      Point(const Point &p) {
        x = p.x;
        y = p.y;
      }
    };
    ```

  - Conversion constructor: A constructor that takes an object of a different class as an argument and converts it to an object of the current class. This is useful for creating an object of one class from an object of another class that has some common attributes. For example:

    ```c++
    class Point {
      int x;
      int y;
      public:
      // Conversion constructor
      Point(const Vector &v) {
        x = v.x;
        y = v.y;
      }
    };
    ```

  - Move constructor: A constructor that takes an rvalue reference to another object of the same class as an argument and moves the values of its attributes to the new object. This is useful for creating an object of the same class from a temporary object that is no longer needed. For example:

    ```c++
    class Point {
      int x;
      int y;
      public:
      // Move constructor
      Point(Point &&p) {
        x = p.x;
        y = p.y;
        // Set p's attributes to null or default values
        p.x = 0;
        p.y = 0;
      }
    };
    ```

- A derived class constructor is a constructor that initializes an object of a subclass that inherits from a base class.
- A derived class constructor must initialize the derived class attributes, and provide instructions on how to initialize the base class object included in the derived class.
- The proper initialization normally happens without any extra code, but sometimes the derived class constructor may need to explicitly call the base class constructor using the `super` keyword in some languages, or the base class name in others. For example:

  ```c#
  class Shape {
    public int x;
    public int y;
    // Base class constructor
    public Shape(int x, int y) {
      this.x = x;
      this.y = y;
    }
  }

  class Circle : Shape {
    public int radius;
    // Derived class constructor
    public Circle(int x, int y, int radius) : base(x, y) {
      // Call the base class constructor with x and y
      this.radius = radius;
    }
  }
  ```