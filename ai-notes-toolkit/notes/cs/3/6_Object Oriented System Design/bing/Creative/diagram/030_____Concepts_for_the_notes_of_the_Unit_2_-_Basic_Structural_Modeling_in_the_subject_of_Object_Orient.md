Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some concepts for the notes of the unit 2 - Basic Structural Modeling in the subject of Object Oriented System Design:

### Basic Structural Modeling
- Structural modeling is the process of representing the static structure of a system using classes, objects, attributes, operations, and relationships.
- Structural modeling helps to define the system's data, behavior, and functionality, as well as the constraints and rules that govern the system.
- Structural modeling can be done at different levels of abstraction, from the conceptual level to the implementation level.
- The main structural modeling techniques in object oriented system design are:
  - Class-Responsibility-Collaboration (CRC) cards
  - Class diagrams
  - Object diagrams

#### Class-Responsibility-Collaboration (CRC) cards
- CRC cards are a simple and informal way of capturing the responsibilities and collaborations of classes in a system.
- A CRC card is a small index card that contains the name of a class, its responsibilities (what it knows and what it does), and its collaborators (other classes that it interacts with) .
- CRC cards are useful for identifying and organizing classes, as well as for discovering and verifying the relationships among classes.
- CRC cards can be created and modified collaboratively by a group of developers or stakeholders, using brainstorming and role-playing techniques.
- An example of a CRC card is shown below:

| Class: Student |
| -------------- |
| **Responsibilities** | **Collaborators** |
| - Knows name, ID, major, courses | - Course |
| - Registers for courses | - Registrar |
| - Drops courses | - Registrar |
| - Pays tuition | - Bursar |

#### Class diagrams
- Class diagrams are the most common and widely used structural modeling technique in object oriented system design.
- A class diagram is a graphical representation of the classes, attributes, operations, and relationships in a system.
- A class diagram shows the static structure of a system, as well as the constraints and rules that apply to the system.
- A class diagram can be used for various purposes, such as:
  - Modeling the domain concepts and terminology of a problem
  - Modeling the design of a software system and its components
  - Modeling the implementation of a software system and its classes
  - Modeling the database schema of a system
- A class diagram consists of the following elements:
  - Classes: A class is a template or blueprint that defines the common properties and behaviors of a set of objects. A class is represented by a rectangle with the class name at the top, followed by the attributes and operations in separate compartments.
  - Attributes: An attribute is a property or characteristic of a class that describes the state or data of its objects. An attribute is represented by a name, followed by an optional type and default value.
  - Operations: An operation is a function or method that defines the behavior or functionality of a class. An operation is represented by a name, followed by an optional list of parameters and return type.
  - Relationships: A relationship is a connection or association between two or more classes that specifies how they interact or depend on each other. There are different types of relationships, such as:
    - Association: An association is a relationship that indicates that two classes are linked or connected in some way. An association is represented by a solid line, optionally with a name, multiplicity, role, and direction.
    - Aggregation: An aggregation is a special type of association that indicates that one class is a part or component of another class. An aggregation is represented by a solid line with a hollow diamond at the end of the whole class.
    - Composition: A composition is a stronger form of aggregation that indicates that one class is a part or component of another class, and that the part cannot exist without the whole. A composition is represented by a solid line with a filled diamond at the end of the whole class.
    - Generalization: A generalization is a relationship that indicates that one class is a subclass or specialization of another class. A generalization is represented by a solid line with a hollow triangle at the end of the superclass.
    - Realization: A realization is a relationship that indicates that one class implements or realizes the interface or abstract class of another class. A realization is represented by a dashed