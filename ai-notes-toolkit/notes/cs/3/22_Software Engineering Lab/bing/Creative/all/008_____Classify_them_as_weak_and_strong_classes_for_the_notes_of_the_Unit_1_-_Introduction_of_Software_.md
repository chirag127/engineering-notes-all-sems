Hello, I am Sydney, your AI assistant. I can help you with your study material for the Software Engineering Lab subject. Here is the content for the topic you requested:

# Classify them as weak and strong classes for the notes of the Unit 1 - Introduction of Software Engineering Lab in the subject of Software Engineering Lab

- A class is a blueprint or template that defines the attributes and behaviors of the objects of that class.
- A weak class is a class that has low cohesion and high coupling, meaning that it has many unrelated responsibilities and depends on many other classes.
- A strong class is a class that has high cohesion and low coupling, meaning that it has a single, well-defined responsibility and minimizes its dependencies on other classes.
- Examples of weak classes are:
  - A class that performs both database operations and user interface operations, such as `CustomerManager`.
  - A class that inherits from multiple unrelated classes, such as `EmployeeStudent`.
  - A class that has many public fields and methods that expose its internal details, such as `Person`.
- Examples of strong classes are:
  - A class that encapsulates a single concept or entity, such as `Customer`.
  - A class that inherits from a single abstract class or interface that defines its contract, such as `Student`.
  - A class that has private fields and methods that hide its implementation details, and provides public methods that define its interface, such as `Person`.