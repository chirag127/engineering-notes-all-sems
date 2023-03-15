### Concept of Inheritance

- Inheritance is one of the core concepts of object-oriented programming (OOP) languages.
- It is a mechanism where you can derive a new class from an existing class, and inherit its attributes and methods .
- The existing class is called the **base class** or **super class**, and the new class is called the **derived class** or **sub class** .
- Inheritance allows you to reuse the code of the base class, and extend or modify its behavior in the derived class .
- Inheritance also helps to form a hierarchy of classes that share some common characteristics, and enables **polymorphism**, which is the ability of objects to behave differently depending on their type .

#### Example of Inheritance

- Suppose you have a base class called `Animal`, which has some attributes like `name`, `age`, `color`, and some methods like `eat()`, `sleep()`, `make_sound()`.
- You can create a derived class called `Dog`, which inherits all the attributes and methods of the `Animal` class, and also adds some new attributes like `breed`, `owner`, and some new methods like `fetch()`, `wag_tail()`.
- You can also create another derived class called `Cat`, which inherits from the `Animal` class, and adds some new attributes like `fur`, `litter`, and some new methods like `scratch()`, `purr()`.
- The `Dog` and `Cat` classes are both sub classes of the `Animal` class, and they share some common characteristics, but also have some unique features.
- The following diagram illustrates the concept of inheritance:

```
    +--------+
    | Animal |
    +--------+
    | name   |
    | age    |
    | color  |
    +--------+
    | eat()  |
    | sleep()|
    | make_sound()|
    +--------+
       / \
      /   \
     /     \
+-----+   +-----+
| Dog |   | Cat |
+-----+   +-----+
| breed|   | fur |
| owner|   | litter|
+-----+   +-----+
| fetch()| | scratch()|
| wag_tail()| | purr()|
+-----+   +-----+
```