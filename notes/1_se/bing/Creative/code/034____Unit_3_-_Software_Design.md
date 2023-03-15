## Unit 3 - Software Design

Software design is the process of defining the architecture, components, interfaces, and other characteristics of a software system. Software design is a creative and iterative activity that involves various methods and tools to produce a solution that meets the requirements and constraints of the problem domain.

One of the methods for software design is the object-oriented approach, which focuses on identifying and modeling the entities, attributes, behaviors, and relationships in the problem domain as classes and objects. Object-oriented design also applies the principles of abstraction, encapsulation, inheritance, and polymorphism to achieve modularity, reusability, and extensibility of software.

Another method for software design is the functional approach, which focuses on defining and composing the functions that transform the inputs to the outputs of the software system. Functional design also applies the principles of purity, immutability, recursion, and higher-order functions to achieve simplicity, predictability, and testability of software.

A common tool for software design is the Unified Modeling Language (UML), which is a graphical notation that can be used to represent various aspects of a software system, such as the structure, behavior, and interaction of its components. UML consists of different types of diagrams, such as class diagrams, use case diagrams, sequence diagrams, and state diagrams, that can be used to communicate and document the software design.

An example of a UML class diagram for a simple calculator software is shown below:

```markdown
+-----------------+
|    Calculator   |
+-----------------+
| - result: int   |
+-----------------+
| + add(x: int, y: int): void    |
| + subtract(x: int, y: int): void |
| + multiply(x: int, y: int): void |
| + divide(x: int, y: int): void   |
| + getResult(): int               |
+-----------------+
```

This diagram shows that the Calculator class has one attribute, result, which stores the current value of the calculation, and five methods, add, subtract, multiply, divide, and getResult, which perform the arithmetic operations and return the result. The + sign indicates that the attribute and methods are public, meaning that they can be accessed by other classes. The - sign indicates that the attribute is private, meaning that it can only be accessed by the Calculator class itself. The : sign indicates the type of the attribute or the parameters and return value of the methods. The void type means that the method does not return any value.