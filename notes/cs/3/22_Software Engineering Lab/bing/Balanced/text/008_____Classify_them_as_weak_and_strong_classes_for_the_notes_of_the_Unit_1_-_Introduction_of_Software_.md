### Classify them as weak and strong classes for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab

- A class is a set of objects that share common attributes and behaviors. Classes are used to model the entities and concepts of a software system.
- In software engineering, classes can be classified as weak or strong based on their cohesion and coupling. Cohesion is the degree to which the elements of a class are related to each other, and coupling is the degree to which a class depends on other classes.
- A weak class is a class that has low cohesion and high coupling. A weak class has many unrelated or loosely related elements, and it depends on many other classes for its functionality. A weak class is hard to understand, maintain, and reuse. A weak class may indicate a poor design or a lack of abstraction.
- A strong class is a class that has high cohesion and low coupling. A strong class has few and closely related elements, and it minimizes its dependencies on other classes. A strong class is easy to understand, maintain, and reuse. A strong class may indicate a good design or a high level of abstraction.
- Examples of weak classes are:
  - A class that performs multiple unrelated tasks, such as reading input, processing data, and displaying output.
  - A class that exposes its internal details to other classes, such as public fields or methods that return references to private members.
  - A class that inherits from multiple unrelated classes, such as a class that implements two or more interfaces that have nothing in common.
- Examples of strong classes are:
  - A class that performs a single and well-defined task, such as a class that represents a data structure or a business rule.
  - A class that encapsulates its internal details and provides a clear and consistent interface to other classes, such as a class that uses private fields and methods and public getters and setters.
  - A class that inherits from a single and relevant class, such as a class that extends an abstract class or implements an interface that defines its behavior.