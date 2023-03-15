Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here are some notes on the topic of Methods & Classes for Unit 1 - Introduction.

### Methods & Classes

- A method is a set of instructions that performs a specific task or operation on some data or objects.
- A class is a blueprint or template that defines the attributes and behaviors of a type of object.
- In object-oriented programming, a class can contain one or more methods that implement the functionality of the object.
- A class can also have fields or properties that store the state or data of the object.
- An object is an instance or example of a class that has its own values for the fields and can invoke the methods of the class.
- To create an object from a class, we use the `new` keyword followed by the name of the class and optionally some arguments to initialize the object.
- To access the fields or methods of an object, we use the dot (`.`) operator followed by the name of the field or method.
- For example, in Java, we can define a class called `Person` with a field called `name` and a method called `greet` as follows:

```java
class Person {
  // A field to store the name of the person
  String name;

  // A constructor to initialize the name of the person
  Person(String name) {
    this.name = name;
  }

  // A method to greet the person
  void greet() {
    System.out.println("Hello, " + name + "!");
  }
}
```

- To create an object of the `Person` class, we can write:

```java
Person p = new Person("Alice");
```

- To access the field `name` of the object `p`, we can write:

```java
System.out.println(p.name); // Prints Alice
```

- To invoke the method `greet` of the object `p`, we can write:

```java
p.greet(); // Prints Hello, Alice!
```