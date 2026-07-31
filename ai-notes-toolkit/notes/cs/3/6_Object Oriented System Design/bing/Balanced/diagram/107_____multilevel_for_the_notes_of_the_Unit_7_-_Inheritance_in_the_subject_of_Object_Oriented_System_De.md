Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of multilevel inheritance in object oriented system design.

### Multilevel inheritance

- Multilevel inheritance is a type of inheritance where a subclass inherits from another subclass that is also derived from a base class.
- In multilevel inheritance, the subclass can access the members of its immediate superclass as well as the members of its ultimate base class.
- Multilevel inheritance can be represented by a hierarchy of classes where each class is connected to its parent class by an arrow pointing upwards.
- For example, consider the following class diagram:

```
    +--------+
    | Animal |
    +--------+
         ^
         |
    +--------+
    |  Bird  |
    +--------+
         ^
         |
    +--------+
    | Parrot |
    +--------+
```

- In this example, the class Parrot is a subclass of the class Bird, which is a subclass of the class Animal. Therefore, Parrot inherits from both Bird and Animal.
- The class Parrot can access the members of the class Bird, such as the method fly(), as well as the members of the class Animal, such as the attribute name.
- The class Parrot can also override the inherited members or define new members of its own, such as the method talk().
- Multilevel inheritance allows the creation of more specific and specialized classes from general and abstract classes.
- Multilevel inheritance also enables code reuse and reduces redundancy by inheriting the common features from the base classes.