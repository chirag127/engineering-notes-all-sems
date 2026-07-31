Hello, I am Sydney, your AI assistant. I can help you with drawing a detailed ASCII diagram for object oriented design in software design.

Object oriented design (OOD) is the process of planning a system of interacting objects for the purpose of solving a software problem. It is one approach to software design that uses the concepts of objects, classes, inheritance, polymorphism, encapsulation, and abstraction. OOD serves as part of the object oriented programming (OOP) process or lifecycle.

One of the principles of OOD is SOLID, which stands for:

- S - Single-responsibility Principle: A class should have one and only one reason to change, meaning that a class should have only one job.
- O - Open-closed Principle: Objects or entities should be open for extension, but closed for modification; that is, such an entity can allow its behaviour to be extended without modifying its source code.
- L - Liskov Substitution Principle: Every subclass/derived class should be substitutable for their base/parent class.
- I - Interface Segregation Principle: A client should never be forced to implement an interface that it doesn’t use or clients shouldn’t be forced to depend on methods they do not use.
- D - Dependency Inversion Principle: Entities must depend on abstractions not on concretions. It states that the high level module must not depend on the low level module, but they should depend on abstractions.

A possible ASCII diagram for object oriented design in software design is:

#### Object Oriented Design in Software Design

```
+---------------------+       +---------------------+
|     Base Class      |       |    Derived Class    |
+---------------------+       +---------------------+
| + attribute1        |       | + attribute2        |
| + attribute2        |       | + attribute3        |
| - attribute3        |       | - attribute4        |
+---------------------+       +---------------------+
| + method1()         |       | + method2()         |
| + method2()         |       | + method3()         |
| - method3()         |       | - method4()         |
+---------------------+       +---------------------+
          ^                             ^
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          +-----------------------------+
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          |                             |
          v                             v
+---------------------+       +---------------------+
|     Interface 1     |       |     Interface 2     |
+---------------------+       +---------------------+
| + method1()         |       | + method2()         |
| + method2()         |       | + method3()         |
| + method3()         |       | + method4()         |
+---------------------+       +---------------------+
```
