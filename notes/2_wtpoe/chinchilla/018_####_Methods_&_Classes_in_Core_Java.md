#### Methods & Classes in Core Java

In Java, methods and classes are fundamental building blocks that enable developers to create reusable code and organize it in a logical and efficient way. Methods are a collection of statements that perform a specific task, and classes are a blueprint for creating objects that encapsulate data and behavior. In this section, we will explore the key concepts and features of methods and classes in Core Java.

##### Methods

A method is a block of code that performs a specific task. It is defined within a class and can be called from other parts of the program. The syntax for defining a method in Java is as follows:

```java
access_modifier return_type method_name(parameter_list) {
    // method body
}
```

- Access modifier: determines the visibility of the method. It can be public, private, protected, or default.
- Return type: specifies the data type of the value returned by the method. If the method does not return a value, the return type is void.
- Method name: a unique identifier for the method.
- Parameter list: a comma-separated list of input parameters for the method.

##### Mnemonic: The acronym "AMPR" can be used to remember the order of elements in a method declaration: Access modifier, Method name, Parameter list, and Return type.

Java also provides several built-in methods, such as println() and parseInt(), which can be used to perform common tasks without having to write the code from scratch.

##### Classes

A class is a blueprint or template for creating objects that encapsulate data and behavior. It contains fields (variables) and methods that define the characteristics and actions of the objects created from it. The syntax for defining a class in Java is as follows:

```java
access_modifier class class_name {
    // class body
}
```

- Access modifier: determines the visibility of the class. It can be public, private, protected, or default.
- Class name: a unique identifier for the class.

##### Mnemonic: The phrase "All Cows Eat Grass" can be used to remember the order of elements in a class declaration: Access modifier, Class keyword, Class name, and Class body.

Java supports inheritance, which allows classes to inherit fields and methods from parent classes. This enables developers to create hierarchical class structures and reuse code across different parts of the program. The extends keyword is used to indicate that a class is inheriting from another class.

```java
class ChildClass extends ParentClass {
    // child class body
}
```

##### Advantages of Methods and Classes

- Reusability: Methods and classes enable developers to write code once and reuse it in different parts of the program, saving time and effort.
- Encapsulation: Classes allow data and behavior to be encapsulated within objects, making it easier to manage and control access to them.
- Hierarchical organization: Classes can be organized into a hierarchy, with parent classes providing functionality that is inherited by child classes, enabling code reuse and simplification.

##### Disadvantages of Methods and Classes

- Overhead: Creating and managing objects can add overhead to a program, which can impact performance.
- Complexity: As a program grows in size and complexity, managing classes and their relationships can become more challenging.

##### Examples

Here are some examples of methods and classes in Core Java:

```java
public class Rectangle {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int getArea() {
        return width * height;
    }
}

Rectangle rect = new Rectangle(5, 10);
int area = rect.getArea(); // returns 50
```

In this example, we define a Rectangle class with width and height fields and a getArea() method that calculates the area of the rectangle. We then create an instance of the class and call the getArea() method to obtain the area of the rectangle.

```java
public class MathUtils {
    public static int add(int a, int b) {
        return a + b;
    }

    public static int multiply(int a, int b) {
        return a * b;
    }
}

int sum = MathUtils.add(2, 3); // returns 5
int product = MathUtils.multiply(4, 5); // returns 20
```

In this example, we define a MathUtils class with add() and multiply() methods that perform basic arithmetic operations. We then call these methods with input parameters to obtain the desired results.

##### Applications

Methods and classes are used extensively in all types of Java applications, from small command-line tools to large-scale enterprise systems. They are essential for creating reusable and organized code that can be easily maintained and extended over time. Some common applications of methods and classes in Java include:

- Creating user interfaces with Swing and JavaFX.
- Implementing data structures and algorithms.
- Developing web applications with Java servlets and JSP.
- Building enterprise applications with Java EE frameworks like