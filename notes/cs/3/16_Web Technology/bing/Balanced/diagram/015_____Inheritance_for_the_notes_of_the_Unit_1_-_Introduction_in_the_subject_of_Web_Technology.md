Hello, I am Sydney, your AI assistant. I can help you with your notes on web technology. Here is some content on inheritance for the notes of the unit 1 - introduction.

### Inheritance

- Inheritance is a concept in object-oriented programming that allows one class to inherit the properties and methods of another class.
- Inheritance enables code reuse and reduces redundancy by allowing a subclass to use the common features of its superclass without having to redefine them.
- Inheritance also supports polymorphism, which is the ability of an object to behave differently depending on its type or context.
- Inheritance can be implemented in different ways depending on the programming language, such as single inheritance, multiple inheritance, hierarchical inheritance, multilevel inheritance, hybrid inheritance, etc.
- Inheritance can be represented by a class diagram, which shows the relationship between classes using a notation of boxes and lines. A subclass is connected to its superclass by a line with an arrow pointing to the superclass. The subclass inherits all the attributes and operations of the superclass, unless they are overridden or hidden by the subclass.

Here is an example of a class diagram that shows inheritance:

```
+-----------------+
|    Vehicle      |
+-----------------+
| +speed          |
| +color          |
+-----------------+
| +start()        |
| +stop()         |
| +accelerate()   |
| +decelerate()   |
+-----------------+
       ^
       |
+-----------------+
|     Car         |
+-----------------+
| +model          |
| +doors          |
+-----------------+
| +honk()         |
+-----------------+
```

In this example, the class Car inherits from the class Vehicle. This means that a Car object has all the attributes and methods of a Vehicle object, such as speed, color, start, stop, etc. In addition, the Car class has its own attributes and methods, such as model, doors, and honk. The Car class can override or hide some of the inherited features of the Vehicle class, such as changing the implementation of the accelerate method or hiding the color attribute.