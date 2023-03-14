 Here is the content in markdown format:

### Issues for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing

- **Inheritance**: When doing object oriented testing, inheritance can introduce complexity. Tests for parent classes may not adequately test subclasses which inherit and extend functionality. Additional tests may be needed for subclasses to ensure inherited methods are working correctly with new or changed functionality.
- **Polymorphism**: Polymorphism allows objects to take on different forms based on context. This can make testing challenging as the same method call may produce different results depending on the object type. Additional tests may be needed to call methods on different subtypes of objects to ensure correctness of results.
- **Encapsulation**: While encapsulation hides internal complexity, it can also make it more difficult to test individual components in isolation. Breaking encapsulation for the purposes of testing may be needed, but should be done carefully to avoid creating dependencies on internal structures that are subject to change.
- **Interfaces**: When testing interfaces, you are only testing the contract between objects - not the implementation details. Additional tests may be needed to test concrete implementations of interfaces to ensure objects are working as expected behind the interface.
- **Tight Coupling**: Tight coupling between objects can make it difficult to test objects in isolation. Dependency injection or other techniques to loosen coupling may be needed to enable effective testing of individual objects.
- **Use of design patterns**: The use of design patterns can introduce both benefits and challenges for testing. For example, the singleton pattern ensures only one instance of a class, which can make state-based testing challenging. Understanding how different patterns impact testability and applying necessary techniques is important for effective testing of object oriented software.

[Diagrams and examples can be added here if helpful for learning]

The key things to keep in mind for object oriented testing are:
- Understand impacts of OOP concepts on testability
- Apply necessary techniques to enable isolation and effective testing of objects
- Recognize that additional tests may be needed to fully test subclasses, interfaces, polymorphic behavior, etc.
- Choose test inputs carefully to exercise different paths through code