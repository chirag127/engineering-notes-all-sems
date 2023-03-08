 Here is the content in markdown format for the given topic:

### Common Mechanisms for Basic Structural Modeling

1. Inheritance:
- Inheritance is a mechanism in which a child class inherits properties and behaviors from its parent class.
- The child class can inherit, modify or extend the functionality of the parent class.
- This promotes code reusability and reduces duplication.
- Examples: Vehicle -> Car, Shape -> Circle, etc.

Advantages:
- Code reusability
- Modular design
- Reduces duplication

Disadvantages:
- Incorrect use can lead to tight coupling
- Excessive use can lead to complex hierarchies

2. Composition:
- Composition is a mechanism in which a class contains other classes as objects to reuse their functionality.
- The containing class does not inherit from the contained class, but simply uses it as an object.
- Examples: Car contains Engine, Student contains Address, etc.

Advantages:
- Promotes low coupling
- Flexible design

Disadvantages:
- May lead to complex designs if not implemented properly

3. Aggregation:
- Aggregation is a special type of composition in which the containing class and contained class have a mutually dependent "has-a" relationship.
- The contained object's lifecycle is not tied to the containing object. It can exist independently too.
- Examples: Department has Professors (Professors can exist without Department too).

Advantages:
- Even lower coupling than composition
- More flexible

Disadvantages:
- Can make designs more complex

[Detailed diagrams, code examples and other details can be added here for more clarity]