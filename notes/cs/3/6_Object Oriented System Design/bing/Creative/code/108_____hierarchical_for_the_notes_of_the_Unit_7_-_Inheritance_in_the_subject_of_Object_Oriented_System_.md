# Hierarchical Inheritance

- Hierarchical inheritance is a way of transmitting features from a parent class to multiple child classes in object-oriented programming (OOP) languages .
- The parent class or superclass is the class from which the properties are taken, i.e. the features are inherited .
- The child classes or subclasses are the classes that inherit the properties from the parent class .
- In hierarchical inheritance, there is one base class and multiple derived classes.
- Several other classes can inherit the derived classes as well, forming a tree-like structure.
- Hierarchical inheritance allows code reusability, polymorphism, and abstraction.
- The inheritance hierarchy of an object is fixed at instantiation when the object's type is selected and does not change with time.
- For example, in the following diagram, the class Animal is the parent class of the classes Dog, Cat, and Bird. The classes Dog, Cat, and Bird are the child classes of the class Animal. The class Dog is also the parent class of the class Poodle, which is the child class of the class Dog.

```
    Animal
   /  |  \
  /   |   \
Dog  Cat  Bird
 |
 |
Poodle
```