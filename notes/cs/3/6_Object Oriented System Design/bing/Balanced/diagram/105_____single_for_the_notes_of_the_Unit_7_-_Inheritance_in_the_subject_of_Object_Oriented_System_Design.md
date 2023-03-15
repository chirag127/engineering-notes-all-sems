### Unit 7 - Inheritance

- Inheritance is one of the core concepts of object-oriented programming (OOP) languages.
- It is a mechanism where you can derive a new class from an existing class, and inherit its attributes and methods .
- The existing class is called the **base class** or **superclass**, and the new class is called the **derived class** or **subclass** .
- The derived class can reuse, extend, and modify the behavior defined in the base class .
- Inheritance can help to achieve code reusability, abstraction, and polymorphism.
- There are different types of inheritance, such as single, multiple, multilevel, hierarchical, and hybrid.
- Single inheritance is the simplest form of inheritance, where a derived class inherits from only one base class.
- For example, in the following diagram, class B is derived from class A, and inherits its attributes and methods. Class B can also add its own attributes and methods, or override the inherited ones.

```mermaid
classDiagram
    class A{
        +a1
        +a2
        +m1()
        +m2()
    }
    class B{
        +b1
        +b2
        +m1()
        +m3()
    }
    B -->|inherits| A
```
- Single inheritance can be implemented in many OOP languages, such as C++, Java, C#, and Python.