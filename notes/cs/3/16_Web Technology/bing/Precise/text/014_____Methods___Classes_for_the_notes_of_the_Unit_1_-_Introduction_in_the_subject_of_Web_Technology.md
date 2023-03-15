### Methods & Classes

#### Unit 1 - Introduction

- **Methods** are functions that are associated with an object and can be called using the dot notation. For example, `object.method()`.
- **Classes** are templates for creating objects. They define the properties and methods that an object will have.
- In **Web Technology**, classes and methods are used to create and manipulate objects that represent elements on a web page, such as buttons, text fields, and images.
- Classes are defined using the `class` keyword, followed by the class name and a set of curly braces `{}` that contain the class's properties and methods.
- Methods are defined within a class using the `function` keyword, followed by the method name and a set of parentheses `()` that contain any parameters the method takes.
- An object is created from a class using the `new` keyword, followed by the class name and a set of parentheses `()`.
- Once an object is created, its methods can be called using the dot notation, as mentioned earlier.

For example, here is a simple class that represents a point in two-dimensional space:

```javascript
class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  distanceToOrigin() {
    return Math.sqrt(this.x * this.x + this.y * this.y);
  }
}

let point = new Point(3, 4);
let distance = point.distanceToOrigin();
```

In this example, the `Point` class has two properties, `x` and `y`, and one method, `distanceToOrigin`. The `constructor` method is a special method that is called when an object is created from the class. In this case, it takes two parameters, `x` and `y`, and assigns them to the object's properties. The `distanceToOrigin` method calculates the distance from the point to the origin (0, 0) using the Pythagorean theorem. An object is created from the `Point` class using the `new` keyword, and its `distanceToOrigin` method is called to calculate the distance from the point to the origin.