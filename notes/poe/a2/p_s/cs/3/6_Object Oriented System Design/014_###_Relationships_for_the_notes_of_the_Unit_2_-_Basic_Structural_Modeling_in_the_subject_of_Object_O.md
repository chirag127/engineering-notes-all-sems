 Here is the content in markdown format for the given topic:

### Relationships for the notes of the Unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design

The following are the major relationships between classes in Object Oriented System Design:

1. Association: It represents a relationship between two classes that establishes through their objects. It indicates that objects of one class can reference objects of another class. For example, a Student and Course can have an association relationship.
2. Aggregation: It is a special type of association that represents a whole-part relationship between the aggregate (whole) and the aggregrate (part) class. The aggregated class cannot exist independently without the aggregate class. For example, a Team can have multiple Employees as aggregation.
3. Composition: It is a strong type of aggregation with stricter ownership between the composite and component classes. The life cycle of the component class is dependent on the composite class. For example, an Address can be a part of a Person through composition. If the Person is deleted, the Address is also deleted.
4. Inheritance: It represents an "is-a" relationship between a superclass and subclass. The subclass inherits the attributes and behaviors of the superclass. It allows code reusability and models hierarchical relationships. For example, a Dog can inherit from an Animal superclass.

The relationships can be shown in class diagrams using association lines, aggregation/composition symbols and generalization arrows respectively. They help in capturing the interactions and dependencies between classes in a system.

[Diagrams or examples can be added here to illustrate the relationships]

The advantages of establishing relationships between classes are:
- Increased reusability through inheritance
- Modeling of real-world relationships/hierarchies
- Maintain consistency by updating in one place

The disadvantages are:
- Can introduce tight coupling between classes
- Can be complex to understand and implement

[More points or details can be added here]